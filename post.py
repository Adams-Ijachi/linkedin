## STEP 5
import os
import requests
from  dotenv import load_dotenv

load_dotenv()


profile_id = '??' ## PUT IN THE PROFILE ID

###IT READS FROM THE TXT FILE
f = open("text.txt", "r")
post = f.read()

#scope: w_member_social,r_liteprofile
access_token = os.getenv('access_token')

url = "https://api.linkedin.com/v2/ugcPosts"

headers = {'Authorization': 'Bearer ' + access_token}


post_data = {
    "author": "urn:li:person:"+profile_id,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": post
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

response = requests.post(url, headers=headers, json=post_data)

print(response.json())
