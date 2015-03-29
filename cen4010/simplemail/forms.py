from django import forms
from flanker.addresslib import address

class MultiEmailField(forms.CharField):
    def to_python(self, value):
        return address.parse_ist(value, as_tuple=True)[0]

    def validate(self, value):
        super(MultiEmailField, self).validate(value)
        parsed_addresses, unparsed_addresses = address.parse_list(value, as_tuple =True)
        if len(unparsed_addresses)> 0:
            if len(unparsed_addresses)== 1:
                message= "{} is not a valid e-mail address".format(unparsed_addresses[0])
            else:
                "{} and {} are not valid e-mail addresses".format(",".join(unparsed_addresses[:-1]), unparsed_addresses[-1])
            raise forms.ValidationError(message)
        if len(parsed_addresses)==0:
            raise forms.ValidationError("You must provide an e-mail address.")

class SendEmailForm(forms.Form):
    #We want to allow comma separated e-mails.
    #To that end, we can't use the Django e-mail field because it only takes one address.
    to =MultiEmailField(help_text ="Enter the e-mail address(s) of the recipients. To enter multiple addresses, separate them with , (comma).")
    subject =forms.CharField()
    message=forms.CharField(widget=forms.Textarea(attrs={'rows': 50, 'cols': 80}),
    help_text= "Enter the body of your message.")

#This inherits all the above stuff, except that it contains a hidden field that we use to funnel an In-Reply-To header.
class ReplyToEmailForm(SendEmailForm):
    in_reply_to=forms.CharField(widget=forms.HiddenInput())
