# -*- coding: utf-8 -*-

'''
Filename: services.py
Created Date: Saturday, December 1st 2018, 9:24:49 pm
Author: bharathmuppa

Copyright (c) 2020 Entangled Cognition
'''

from flask import Flask, request, jsonify, stream_with_context
from utils import downloadVideo, downloadPlaylist,downloadVideoForMobile
app = Flask(__name__)

@app.route('/api/videos/video', methods=['GET', 'POST'])
def videoDispatcher():
    content = request.get_json(force=True)
    for url in content['urls']:
        downloadVideo(url)
    return jsonify({"message":"video downloaded succesfully"})

@app.route('/api/videos/playlist', methods=['GET', 'POST'])
def playlistDispatcher():
    content = request.get_json(force=True)
    for playlist in content['urls']:
        downloadPlaylist(playlist)
    return jsonify({"message":"playlist downloaded succesfully"})

@app.route('/api/mobile/videos/video', methods=['GET', 'POST'])
def mobileVideoDispatcher():
    content = request.get_json(force=True)
    for url in content['urls']:
        videoStream=downloadVideoForMobile(url)
        return stream_with_context(videoStream)

@app.route('/api/mobile/videos/playlist', methods=['GET', 'POST'])
def mobilePlaylistDispatcher():
    content = request.get_json(force=True)
    for playlist in content['urls']:
        playlistStream=downloadPlaylist(playlist)
        return stream_with_context(playlistStream)

if __name__ == '__main__':
    app.run(port=int("9090"), debug=True)
