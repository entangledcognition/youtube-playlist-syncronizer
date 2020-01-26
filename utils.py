from pytube import YouTube,Playlist
from pprint import pprint
import json
import sys,os

def createFolderForPlaylist(rootDir):
    with open('user_playlist.json') as playlist:
        playlist_serilaized = json.load(playlist)
        for playlist in playlist_serilaized['items']:
            snippet = playlist['snippet']
            title = snippet['title']
            id= playlist['id']
            baseFolder = rootDir+'/'+title
            print(baseFolder)
            if not os.path.exists(baseFolder):
                os.makedirs(baseFolder)     
            url= 'https://www.youtube.com/playlist?list='+id
            downloadPlaylistFromDirectUrl(url,baseFolder)
    
    
def downloadVideo(url):
    YouTube(url).streams.first().download('C:\Downloads')

def downloadPlaylist(playlistUrl):
     pl = Playlist(playlistUrl['url'])
     folder = playlistUrl['folder-name']
     baseFolder = 'C:\\Downloads\\'
     if not os.path.exists(baseFolder + folder):
         os.makedirs(baseFolder + folder)
     pl.download_all(baseFolder + folder)

def downloadPlaylistFromDirectUrl(playlistUrl,baseFolder):
     pl = Playlist(playlistUrl)
     if not os.path.exists(baseFolder):
         os.makedirs(baseFolder)
     pl.download_all(baseFolder)

def downloadVideoForMobileOnComplete(stream, chunk, file_handle, bytes_remaining):
    pprint(chunk)
    #return chunk;

def downloadVideoForMobile(url):
    YT=YouTube(url)
    YT.register_on_progress_callback(downloadVideoForMobileOnComplete)
    return YT.streams.first()
def downloadPlaylistForMobileOnComplete(stream, file_handle):
    pprint(stream)
def downloadPlaylistForMobile(url):
    YT=YouTube(url).streams.first()
    YT.register_on_complete_callback(downloadVideoForMobileOnComplete)

"""
yt.set_filename(sys.argv[2])
pprint(yt.get_videos())
format=input("enter video format: ")
pixel=input("enter pixels from list: ")
video = yt.get(format,pixel)
video.download('c://Downloads');
"""
if __name__ == "__main__":
    createFolderForPlaylist()