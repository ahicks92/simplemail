from django.shortcuts import render
from django.db import transaction
import requests

#Downloads all messages from Mailgun and returns success.
def get_all_mailgun_messages(request):
    return render(request, 'simplemail/mailgun_got_messages.html')
