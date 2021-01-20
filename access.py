## STEP 3
import os
import requests
import requests
from  dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('client_id')
redirect_uri = "http://localhost:8000/auth/linkedin/callback"
code = ""##put the code gotten from the url
access_token = requests.post(
    'https://www.linkedin.com/oauth/v2/accessToken',
    params = {
        'grant_type': 'authorization_code',
        # This is code obtained on previous step by Python script.
        'code':code,
        # This should be same as 'redirect_uri' field value of previous Python script.
        'redirect_uri':redirect_uri,
        # Client ID of your created application
        'client_id':client_id,
        # Client Secret of your created application
        
        'client_secret': os.getenv('client_secret')
    },
).json()
print(access_token["access_token"])
