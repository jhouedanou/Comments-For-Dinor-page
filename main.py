
page_id='100069074211251'
post_id='716403620672105'  
access_token='EAAKTECZAmD8ABO2goOQbIJp5ZApoobVwC9zwZA5oYWFVRbnDcZCZAo3XB4Nr5hb10PXoCyBcZAEEJrCXzDaGBuZBORXAFuwX4A9ZAkFz4JpAZAac6rja0GJjY8VQuDg3AuNVHZAk9HXjAZA94p9J7cFYY0rwFZC8MseEyRypBv08qHVTZC2nOCsw1zAMp4r2zsq4JkA1eNAOtuVv8'

#access the comments using graph api v19
url=f'https://graph.facebook.com/v19.0/{page_id}_{post_id}/comments?access_token={access_token}'

response = requests.get(url)
# save name, time, message in excel file
data = json.loads(response.text)
# create object with only name, time, message
def get_comment(comment):
    return {
        'name': comment['from']['name'],
        'time': comment['created_time'],
        'message': comment['message'],
        'likes': comment['like_count'] 
    }

excel_data = list(map(get_comment, data['data']))
df = pd.DataFrame(excel_data)
df.to_excel('comments.xlsx', index=False)