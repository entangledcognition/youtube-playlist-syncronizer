# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlists.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import json
import pickle
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.auth.transport.requests import Request
from youtube_synchronizer.secrets.client_secret import get_client_secrets,get_scope
from pathlib import Path


scopes = get_scope()

def loginToGoogle():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = get_client_secrets()
    credentials = ""
    Path("./youtube_synchronizer/temp").mkdir(parents=True, exist_ok=True)
    if os.path.exists('./youtube_synchronizer/temp/token.pickle'):
        with open('./youtube_synchronizer/temp/token.pickle', 'rb') as token:
            unpickler = pickle.Unpickler(token)
            credentials = unpickler.load()
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            # Get credentials and create an API client
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_config(
                client_secrets_file, scopes)
            credentials = flow.run_local_server(port=0)
        with open('./youtube_synchronizer/temp/token.pickle', 'wb') as token:
            pickle.dump(credentials, token)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    request = youtube.playlists().list(
        part="snippet,contentDetails",
        maxResults=50,
        mine=True
    )
    response = request.execute()
    file = open("./youtube_synchronizer/temp/user_playlist.json", "w+")
    file.write(json.dumps(response))
    file.close()


if __name__ == "__main__":
    loginToGoogle()
