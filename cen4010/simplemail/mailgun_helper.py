#These functions are convenience functions for app-level mailgun request getting and posting.
import requests
import requests.auth
import os
import json

mailgun_key=os.getenv('mailgun_key')
domain ="simplemail.camlorn.net"
base_url="https://api.mailgun.net/v3/{0}/".format(domain)
auth=requests.auth.HTTPBasicAuth('api', mailgun_key)

def mget(endpoint):
    return requests.get(base_url+endpoint, auth =auth)

def mpost(endpoint, data):
    """Data is a dict which is encoded to JSON by this function."""
    return requests.post(base_url+endpoint, json=json.dumps(data), auth=auth)
