import requests
import pandas as pd
import json


page_id = "100069074211251"
post_id = "716403620672105"
access_token = "EAAKTECZAmD8ABO0DpiyF0TKihwn5sRuGIyTbFwZBjN1ubbve5waxSKqTRHSTQtemOPjJBSM2qNus2jyVDckN5RTzMy8xiceZA3tjXHhxbYQrvTXFXxgsRB01J8cNVBLgxsVtHM5iIf3DoNBgwrq5gspeGXI28ZCOIT2GwiRxdJ6wlAtIvfizpydB8E6ECTzZBXtJaYvK2e44SWvfC7K03kZAgcz56edkhpti961rcn"


url = f"https://graph.facebook.com/v19.0/{page_id}_{post_id}/comments?limit=500&fields=from,message,like_count&access_token={access_token}"

response = requests.request("GET", url)

# save name, time, message in excel file
data = json.loads(response.text)

print(data)


# create object with only name, time, message
def get_comment(comment):
    return {
        "name": comment["id"],
        "message": comment["message"],
        "likes": comment["like_count"],
    }


excel_data = list(map(get_comment, data["data"]))
df = pd.DataFrame(excel_data)
df.to_excel("comments.xlsx", index=False)
