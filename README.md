# Youtube playlist synchronizer

## Motivated and built on top of pytube
<div align="center">
  <p>
  <img src="https://github.com/nficano/pytube/blob/master/images/pytube.png?raw=true" width="350" height="328" alt="pytube logo" />
  </p>
  <p align="center">
	  <a href="https://pypi.python.org/pypi/pytube/"><img src="https://img.shields.io/pypi/pyversions/pytube.svg" /></a>
  </p>
</div>

## Motivation
We always have a habbit of structuring our content based on the genre of file/video.
Yotube playlist is one of them, where we love to group videos based on our interests.

Lets says if i gonna hit zim, I will create a workout playlist,
I will create one for healing music on a rainy day,
We started creating a great playlist and suddenly one day author of video, might delete that video or it might be deleted of           coopyrights. sometimes you never know what was deleted becoz you wont keep track of all playlists

Whatever the reasons might be, we lose a lovely song/video.

So This youtube synchronizer helps you in synchronizing the playlist to your local computer drive.
You just need to install this app and it helps in following possible ways 
1.  sync your gmail wehich you have linked to youtube 
2.  Download youtube playlist or youtube video downloader

# steps to setup local development

### Pre-Requisites for setting up DEV Environment
1. Install anaconda version 
2. clone this repo to your system with ssh or https
3. conda env create --file environment_win.yml 
4. Open vscode and add python interprerter from ctrl+shift+p and add conda env.
    
### Running the project 
1. Run Google-login.py and it creates user_playlist.json file
2. Run utils.py and it creates folders and started syncing viedos in selected parent directory 

Note: It is always better to run this program in vpn network.


please go throuugh for more details 
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually
change code as per python pytube C:\Users\bhara\.conda\envs\youtube-playlist-sync\Lib\site-packages\pytube

```python
>>> #to create a environment file, it will overide the existing env file
>>> conda env export  >  environment_win.yml
>>> #update
>>> conda env update --prefix --file environment_win.yml  --prune
```

to create a execuatble follow the bleow mentioned process

```python
 >>> # to create exe
 >>> pyinstaller --onefile youtube-playlist-synchronizer.py
 >>> # to re-create from spec file after exe is created
 >>> pyinstaller youtube-playlist-synchronizer.spec
```
