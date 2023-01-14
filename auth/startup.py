from auth.flask_spotify_auth import getAuth, refreshAuth, getToken

CLIENT_ID = ""
CLIENT_SECRET = ""

PORT = "8081"
CALLBACK_URL = "http://localhost"

#Add needed scope from spotify user
SCOPE = "streaming user-read-recently-played user-top-read user-read-recently-played playlist-read-private user-library-read user-read-email user-read-private"
#token_data will hold authentication header with access code, the allowed scopes, and the refresh countdown 
TOKEN_DATA = []


def getUser(client_id, client_secret):
    global CLIENT_ID
    global CLIENT_SECRET
    CLIENT_ID = client_id
    CLIENT_SECRET = client_secret
    return getAuth(CLIENT_ID, "{}:{}/callback/".format(CALLBACK_URL, PORT), SCOPE)

def getUserToken(code):
    global TOKEN_DATA
    TOKEN_DATA = getToken(code, CLIENT_ID, CLIENT_SECRET, "{}:{}/callback/".format(CALLBACK_URL, PORT))
 
def refreshToken():
    TOKEN_DATA = refreshAuth()

def getAccessToken():
    return TOKEN_DATA
