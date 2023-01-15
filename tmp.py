import base64, json, requests
HEADER = 'application/x-www-form-urlencoded'
client_id = "d56abac37e7c47b78c50654f8a257fa3"
client_secret = "2b59bfb0d5c340cfb052ba9b458c72b8"
api_url = 'https://accounts.spotify.com/api/token'
auth_token = "{}:{}".format(client_id, client_secret)
encoded = base64.b64encode(bytes(auth_token, 'utf-8'))
headers = {"Content-Type" : HEADER, "Authorization" : "Basic {}".format(encoded.decode('utf-8'))} 
body = {
    "grant_type": 'client_credentials',
}
post = requests.post(api_url, params=body, headers=headers)
print(json.loads(post.text))
