from auth.flask_spotify_auth import getAuth, refreshAuth, getToken

CLIENT_ID = ""
CLIENT_SECRET = ""

PORT = "8081"
CALLBACK_URL = "http://localhost"

#Add needed scope from spotify user
SCOPE = "user-library-read user-read-playback-position playlist-modify-public playlist-modify-private"
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
 
def refreshToken(time):
    time.sleep(time)
    TOKEN_DATA = refreshAuth()

def getAccessToken():
    return TOKEN_DATA