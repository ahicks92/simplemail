from django import forms

class SendEmailForm(forms.Form):
    #We want to allow comma separated e-mails.
    #To that end, we can't use the Django e-mail field because it only takes one address.
    to =forms.CharField()
    subject =forms.CharField()
    message=forms.CharField(widget=forms.Textarea(attrs={'rows': 50, 'cols': 80}))

#This inherits all the above stuff, except that it contains a hidden field that we use to funnel an In-Reply-To header.
class ReplyToEmailForm(SendEmailForm):
    in_reply_to=forms.CharField(widget=forms.HiddenInput())
