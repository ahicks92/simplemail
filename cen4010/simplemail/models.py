from django.db import models
from django.contrib.auth.models import User
import datetime

#This is a model of an e-mail which includes all of the information we need from it, flattened into a giant e-mail table.
#The stuff about replying won't be used for a while if at all, but adding it later may be somewhat difficult.
#Also, there's basically no limits on lengths by the e-mail specs. Consequently we have to overuse TextField.
class Email(models.Model):
    #An e-mail is either in the inbox or outbox.
    #E-mails are in the outbox if it was sent, so we record that value.
    #We also need sent e-mails for the ability to follow the reply chain back as necessary.
    was_sent=models.BooleanField(default=False)

    #The Mailgun API sends us blobs of text. We pull out the really important info for database queries.
    #Even so, keeping this around lets us do post-processing on it.
    #There is no body field in this model.  We get it from here.
    mailgun_json =models.TextField()

    #The next message in the reply chain.
    #If there isn't one, this returns None when accessed.
    in_reply_to = models.OneToOneField('self', null=True)

    #The message_id is used for constructing reply chains and is extracted from a mail header.
    message_id=models.TextField()

    subject =models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    #From is a Python key word. We apply the same naming scheme to to in order to avoid special cases.
    from_address = models.TextField()
    to_address =models.TextField()

#This is a user's profile.
class userProfile(models.Model):

    #The user's e-mail address, not including anything after the @ symbol.
    email = models.CharField(max_length=255)

    first_name=models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    signature= models.TextField()


    #This establishes a link with the user account for this profile.
    #It also adds a .profile to all users under this Django project.
    user= models.OneToOneField(User)
