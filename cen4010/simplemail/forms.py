from django import forms
from django.core import urlresolvers
from django.shortcuts import render
from flanker.addresslib import address
import simplemail.models
import django.contrib.auth.models

class MultiEmailField(forms.Field):
    empty_values=([])

    def to_python(self, value):
        parsed_addresses, unparsed_addresses = address.parse_list(value, as_tuple =True)
        if len(unparsed_addresses)> 0:
            if len(unparsed_addresses)== 1:
                message= u"{} is not a valid e-mail address".format(unparsed_addresses[0].to_unicode())
            else:
                message=u"{} and {} are not valid e-mail addresses".format(u",".join(unparsed_addresses[:-1]), unparsed_addresses[-1])
            raise forms.ValidationError(message)
        if len(parsed_addresses)==0:
            raise forms.ValidationError(u"You must provide an e-mail address.")
        return parsed_addresses


class SendEmailForm(forms.Form):
    #We want to allow comma separated e-mails.
    #To that end, we can't use the Django e-mail field because it only takes one address.
    to =MultiEmailField(help_text ="Enter the e-mail address(s) of the recipients. To enter multiple addresses, separate them with , (comma).")
    subject =forms.CharField(min_length= 1, max_length= 200)
    message=forms.CharField(widget=forms.Textarea(attrs={'rows': 50, 'cols': 80}),
    help_text= "Enter the body of your message.")

#This inherits all the above stuff, except that it contains a hidden field that we use to funnel an In-Reply-To header.
class ReplyToEmailForm(SendEmailForm):
    in_reply_to=forms.CharField(widget=forms.HiddenInput())

class AccountCreationForm(forms.Form):
    user_name= forms.RegexField(min_length= 5, regex = r"[a-zA-Z1-90_]+", help_text ="Your user name for Simplemail.  Your e-mail address will be <username>@simplemail.camlorn.net.")
    password=forms.CharField(widget = forms.PasswordInput, min_length=5)
    confirm_password=forms.CharField(widget= forms.PasswordInput, min_length =5)
    first_name = forms.CharField(min_length = 1)
    last_name=forms.CharField(min_length= 1)

    def clean(self):
        username=self.cleaned_data.get("user_name")
        if django.contrib.auth.models.User.objects.filter(username= username).exists():
            raise validationError("Your username is already in use.  Please try another.")
        if self.cleaned_data.get("password") !=self.cleaned_data.get("confirm_password"):
            raise ValidationError("Your password does not match with the password entered in 'confirm password'.  Please re-enter it in both fields and try again.")

def render_account_creation_form(request, form = None):
    if form is None:
        form = AccountCreationForm()
    context = {
        'form': form,
        'form_title': "Create an account",
        'submit_label': "Create Account",
        'next_url': urlresolvers.reverse("create_account"),
    }
    return render(request, "registration/create_account.html", context)

def render_send_message_form(request, form = None):
    if form is None:
        form = SendEmailForm()
    context = {
        'form': form,
        'form_title': "Send Message",
        'submit_label': "Send",
        'next_url': urlresolvers.reverse("send_message"),
    }
    return render(request, "simplemail/form.html", context)

def render_reply_to_message_form(request, form = None, in_reply_to = None):
    """in_reply_to should be a database model representing a message"""
    if form is None:
        form = ReplyToEmailForm({\
        'in_reply_to': in_reply_to.message_id,
        'subject': "Re:" + in_reply_to.subject if not in_reply_to.subject.startswith("Re:") else in_reply_to.subject,
        'to': in_reply_to.from_address})
    context = {
        'form': form,
        'form_title': "Reply To Message",
        'submit_label': "Reply",
        'next_url': urlresolvers.reverse("reply_to_message", args= (in_reply_to.id, )),
    }
    return render(request, "simplemail/form.html", context)
