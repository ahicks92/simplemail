from django.db import models
from django.contrib.auth.models import User
import datetime


#This is a model of an e-mail which includes all of the information we need from it, flattened into a giant e-mail table.
#The stuff about replying won't be used for a while if at all, but adding it later may be somewhat difficult.
#Also, there's basically no limits on lengths by the e-mail specs. Consequently we have to overuse TextField.
class Email(models.Model):
    #The Mailgun API sends us blobs of text. We pull out the really important info for database queries.
    #Even so, keeping this around lets us do post-processing on it in the future, if we need to.
    mailgun_json =models.TextField()

    #The message_id is used for constructing reply chains and is extracted from a mail header.
    message_id=models.TextField()

    subject =models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    #From is a Python key word.
    from_address = models.TextField()
    #This is a very ugly concatenation of a bunch of stuff.
    #The result is a comma-separated list of e-mail addresses plus some extra data.
    all_addresses = models.TextField()
    to_addresses =models.TextField()

    #E-mail body.
    body = models.TextField()
    body_stripped=models.TextField()
    signature =models.TextField(default = '')

class UserProfile(models.Model):

    #The user's e-mail address, not including anything after the @ symbol.
    email = models.CharField(max_length=255)

    first_name=models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    signature= models.TextField(default = '')
    #This establishes a link with the user account for this profile.
    #It also adds a .profile to all users under this Django project.
    user= models.OneToOneField(User, related_name= 'profile')

    #inbox, outbox, and trash.
    #Technically these should be folder models, but we only have 3 and the special case is faster:
    inbox=models.ManyToManyField(Email, related_name='inbox_users')
    outbox=models.ManyToManyField(Email, related_name= 'outbox_users')
    trash=models.ManyToManyField(Email, related_name='trash_users')
    #This lets us tell if a message was sent or inbox after it was deleted:
    trash_sent = models.ManyToManyField(Email, related_name = 'trash_sent_users')

