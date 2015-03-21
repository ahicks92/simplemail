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

    #This establishes .thread and .latest.
    latest=models.ForeignKey('self', related_name ='thread', null= True, default = None)

    #The message_id is used for constructing reply chains and is extracted from a mail header.
    message_id=models.TextField()

    subject =models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    #From is a Python key word.
    from_address = models.TextField()
    #This is a very ugly concatenation of a bunch of stuff.
    #The result is a comma-separated list of e-mail addresses plus some extra data.
    all_addresses = models.TextField()

class UserProfile(models.Model):

    #The user's e-mail address, not including anything after the @ symbol.
    email = models.CharField(max_length=255)

    first_name=models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    signature= models.TextField()
    owned_emails = models.ManyToManyField(Email, related_name ='for_users')

    #This establishes a link with the user account for this profile.
    #It also adds a .profile to all users under this Django project.
    user= models.OneToOneField(User)
