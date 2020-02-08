from boxsdk import OAuth2
from boxsdk import Client
import sys

def save(access_token,refresh_token):
    print("EE")
    with open("token.txt"+".temp",'w') as token:
       str1=access_token+" "+refresh_token
       token.write(str1)
    #os.remove("token.txt")
    #os.rename("token.txt.temp","token.txt")

         
oauth=OAuth2(client_id="ab74l1nzq1xckhfakzcdyb3ayd9f1kfw",client_secret="IuElcUeNWHGCB2OLUFM7gNr2p3N4YlXZ",store_tokens=save)
auth_url,csrf_token=auth_url, csrf_token = oauth.get_authorization_url('https://google.com/')
#print(auth_url,csrf_token)
#CSRF=auth_url.split('?')[1].split('&')[0].split('=')[1]
#print(CSRF)
#assert CSRF==csrf_token
OAUTH=sys.argv[1]
access_token, refresh_token = oauth.authenticate(OAUTH)
client = Client(oauth)
folder = client.folder(folder_id='48549145105').get()
print(f'Folder "{folder.name}" name')
