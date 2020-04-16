import os
import sys
import spotipy
import webbrowser
import spotipy.util as util
from fbchat import  Client
from fbchat.models import *
from urllib.parse import urlparse

#SPOTIFY VARIABLES
username = os.environ.get('SPOTIFY_USERNAME')
playlist_id = os.environ.get('SPOTIFY_PLAYLIST')
scope = 'playlist-modify-public'    

#FACEBOOK VARIABLES
FLogin = os.environ.get('FACEBOOK_LOGIN')
FPassword = os.environ.get('FACEBOOK_PASSWORD')
FThread = os.environ.get('FACEBOOK_THREAD')

def get_token():
    try:
        token = util.prompt_for_user_token(username, scope)
        os.environ['SPOTIPY_CACHE'] = '.cache-{username}'
        if token:
            sp = spotipy.Spotify(auth=token)
            sp.trace = False
            return sp
        else:
            print("Can't get token for", username)
    except:
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope)
        if token:
            sp = spotipy.Spotify(auth=token)
            sp.trace = False
            return sp
        else:
            print("Can't get token for", username)

class Facebook(Client):
    def onMessage(self, author_id=None, message_object=None, thread_id=FThread, thread_type=ThreadType.GROUP, **kwargs):
        self.markAsRead(author_id)
        msgText = message_object.text
        mid = message_object.uid
        metadata = self._forcedFetch(thread_id, mid).get("message")
        try:
            if "open.spotify.com" in msgText:
                sp = get_token()
                TrackID = (urlparse(msgText)).path
                tracks = [TrackID]
                sp.user_playlist_add_tracks(username, playlist_id, tracks, position=None)
                print("\n****************************************\nAdding track to chosen playlist...\n****************************************\n")
        except:
            try:
                uri = metadata['extensible_attachment']
                uri = uri['story_attachment']
                uri = uri['url']
                uri = uri.replace("https://l.facebook.com/l.php?u=https%3A%2F%2Fopen.spotify.com%2Ftrack%2F","")

                sp = get_token()
                counter = 0
                track_id_uri = []
                for i in uri:
                    if counter < 22:
                        counter += 1
                        track_id_uri.append(i)
                TrackID = ''.join(track_id_uri)
                tracks = [TrackID]
                sp.user_playlist_add_tracks(username, playlist_id, tracks, position=None)
                print("\n****************************************\nAdding track to chosen playlist...\n****************************************\n")
            except:
                print("\n****************************************\nNot a (valid) Spotify track.\n****************************************\n")
                
client = Facebook(FLogin, FPassword)
client.listen()