from django.shortcuts import render
from django.db import transaction
from .mailgun_helper import *
from . import models
import email
import re
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required
import json

#Downloads all messages from Mailgun and returns success or failure.
@transaction.atomic
def get_all_mailgun_messages(request):
    result =mget("events").json()
    events=result['items']
    message_urls=[i['storage']['url'] for i in events if i['event']=='stored']
    messages_request = [mget(i, prepend=False) for i in message_urls]
    messages_dict=[i.json() for i in messages_request]
    messages_json=[i.text for i in messages_request]
    count = 0
    #For each message, we make an e-mail model and save it.
    for i, json_raw  in zip(messages_dict, messages_json):
        #We first extract the message id, which is supposed to be unique for all e-mails everywhere.
        headers=i['message-headers']
        #Nothing actually stops someone sending a message with multiple headers of the same type.
        ids=[j[1] for j in headers if j[0] == 'Message-Id']
        id=ids[0]
        #This ID may already be in the database. If it is, we bail out now.
        exists=models.Email.objects.filter(message_id= id).count()
        if exists >0:
            continue
        #The other pieces of important information we need out of the e-mail is the In-Reply-To header and the references header.
        #Together, these form a list of ids which we use to build threads, later.
        in_reply_to =[j[1] for j in headers if j[0]== 'In-Reply-To']
        references=[j[1] for j in headers if j[0]=='References']
        #The in_reply_to field is one id only so we start with that.
        in_thread = list(in_reply_to)
        for j in references:
            in_thread +=re.findall(r"<[^<]+>", j)
        in_thread= set(in_thread) #remove duplicates.
        #We now have enough info to build the message itself as follows.
        new_message=models.Email(
            was_sent=False,
            mailgun_json = json_raw,
            message_id=id,
            subject=i['subject'],
            from_address=i['from'],
            body =i['body-plain'],
            body_stripped = i['stripped-text'] if 'stripped-text' in i else i['body-plain'],
            signature= i['stripped-signature'] if 'stripped-signature' in i else "",
        )
        #Build up a ist of all the e-mail addresses involved in this e-mail.
        all_addresses = i['from']+","+i['To']
        new_message.all_addresses= all_addresses
        new_message.save()
        #Next, build the thread by pointing all messages at the latest.
        for j in models.Email.objects.filter(message_id__in = list(in_thread)):
            j.latest = new_message
            j.save()
        #Finally, handle users.
        user_emails= [j.strip() for j in i['recipients'].split(",")]
        users=list(models.UserProfile.objects.filter(email__in = user_emails))
        new_message.for_users = users
        new_message.save()
        for u in users:
            u.save()
        count +=1
    return render(request, 'simplemail/mailgun_got_messages.html', {'count': count})

@login_required
def inbox(request):
    messages= request.user.profile.emails.all().order_by('-date')
    return render(request, "simplemail/inbox.html", {'messages': messages})

@login_required
def view_message(request, message_id):
    message=request.user.profile.emails.get(pk=message_id)
    return render(request, "simplemail/view_message.html", {'message': message})

def index(request):
    """ This View will be the home page to the application"""
    return render(request, 'registration/index.html')
