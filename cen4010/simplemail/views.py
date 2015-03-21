from django.shortcuts import render
from django.db import transaction
from .mailgun_helper import *

#Downloads all messages from Mailgun and returns success.
@transaction.atomic
def get_all_mailgun_messages(request):
    result =mget("events").json()
    events=result['items']
    message_urls=[i['storage']['url'] for i in events if i['event']=='stored']
    messages= [mget(i) for i in message_urls]
    count =len(messages)
    return render(request, 'simplemail/mailgun_got_messages.html', {'count': count})
