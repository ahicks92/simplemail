#this is a test script that sends messages for you.
import requests
import requests.auth
import os

key=os.getenv("mailgun_key")
if key is None:
    print "You didn't run authenticate.bat first."
domain ="simplemail.camlorn.net"
request_url='https://api.mailgun.net/v3/{0}'.format(domain)

auth=requests.auth.HTTPBasicAuth('api', key)

print "Enter e-mails, separate with comma"
emails=raw_input()
emails=emails.split(',')

print "Enter subject:"
subject=raw_input()

print "Enter body. Terminate with . on a line by itself:"
body= []

while True:
    inp=raw_input()
    if inp==".":
        break
    body.append(inp)

body = "\n".join(inp)

data = {
'to': emails,
'from': 'test@simplemail.camlorn.net',
'text': body,
'subject': subject,
}
r=requests.post(request_url+"/messages", auth =auth, data= data)
