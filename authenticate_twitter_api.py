# Twitter API authentication

import json

credFile = open('secrets.json', "r")
data = json.loads(credFile.read())

api_key = data['api_key']
api_secret_key = data['api_secret_key']
access_token = data['access_token']
access_token_secret = data['access_token_secret']

credFile.close()
