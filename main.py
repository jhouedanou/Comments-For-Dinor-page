import requests
import pandas as pd
import json
import config

app_id = config.app_id
app_token = config.app_token
page_id = config.page_id
post_id = config.post_id
access_token = config.access_token

url = f"https://graph.facebook.com/v19.0/{page_id}_{post_id}/comments?limit=250&fields=from,message,like_count&access_token={access_token}"

response = requests.get(url)
json_data = response.content
data = json.loads(json_data)


def get_comment(comment):
    return {
        "name": comment["id"],
        "message": comment["message"],
        "likes": comment["like_count"],
    }


excel_data = list(map(get_comment, data["data"]))
df = pd.DataFrame(excel_data)
df.to_excel("comments.xlsx", index=False)
