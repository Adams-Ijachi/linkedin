## STEP 4
import os
import requests
from  dotenv import load_dotenv

load_dotenv()

# GET THE ID FOR YOUR PROFILE AND COPY THE ID FOR AND PROCEED TO POST.PY


#scope: w_member_social,r_liteprofile
access_token =os.getenv('access_token')

url = "https://api.linkedin.com/v2/me"

headers = {'Authorization': 'Bearer ' + access_token}


response = requests.get(url, headers=headers)

print(response.json()["id"])



MY_ENV_VAR = os.getenv('MULTILINE_VAR')

print(MY_ENV_VAR)