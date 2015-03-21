#this is a test script that asks mailgun for al messages it has and prints json to the console.
import requests
import requests.auth
import os

key=os.getenv("mailgun_key")
if key is None:
    print "You didn't run authenticate.bat first."

domain='simplemail.camlorn.net'
request_url='https://api.mailgun.net/v3/{0}'.format(domain)
auth=requests.auth.HTTPBasicAuth('api', key)

request=requests.get(
request_url+"/events", auth=auth)

messages=[]
for i in request.json()['items']:
    if i['event'] =='stored':
        r=requests.get(i['storage']['url'], auth=auth)
        messages.append(r.json())
