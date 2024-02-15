import requests
import pandas as pd
import json

app_id = "724647526404032"
app_token = "949bf118e7fd1690a47bd036e7d4c95c"
page_id = "100069074211251"
post_id = "716403620672105"
access_token = "EAAKTECZAmD8ABOy4z6ZAwEBw384lEEx8lP6C3tB1DLRsH5ZCLdcSJu5y1LB8NVNrULZAg8Efs8ZAIpdYdyr5Qd8vAbfW3XZCoC5cCxKTtogVVAq6SagpGXScwtb9VexnGzEDTVNuaXBhaHpIJKQJGZB6OdwuIZAi44kZApk3FoNAt17V5RZBPs0wb0RnXUwR2pfq7He2hJGKkRDxR4CZCuy2sTzmKoXHSeoJwqpZBZABGnfnmAQZDZD"


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
