
# Youtube playlist synchronizer

<img src="https://github.com/entangledcognition/youtube-playlist-syncronizer/blob/master/share.png?raw=true" alt="pytube logo" />

## Motivated and built on top of _[pytube](https://github.com/nficano/pytube)_

## Motivation

We always have a habbit of structuring our content based on the genre of file/video.
Yotube playlist is one of them, where we love to group videos based on our interests.

Lets says if i gonna hit zim, I will create a workout playlist,
I will create one for healing music on a rainy day,
We started creating a great playlist and suddenly one day author of video, might delete that video or it might be deleted of           coopyrights. sometimes you never know what was deleted becoz you wont keep track of all playlists

Whatever the reasons might be, we lose a lovely song/video.

So This youtube synchronizer helps you in synchronizing the playlist to your local computer drive.
You just need to install this app and it helps in following possible ways 
1.  sync your google which you have linked to youtube 
2.  Download youtube playlist or youtube video downloader
3.  Re-sync the playlist whenever there are updates.

## Executables
1. Windows - [here](https://github.com/entangledcognition/youtube-playlist-syncronizer/releases/download/v1.0.0-beta.1/youtube-playlist-synchronizer.exe)

## Local Installation guide

### Pre-Requisites for setting up DEV Environment
1. Install anaconda version 
2. clone this repo to your system with ssh or https
3. conda env create --file environment_win.yml 
4. Open vscode and add python interprerter from ctrl+shift+p and add conda env.
    
### Running the project 

Once you are done with setup run the below commands from root directory

```bash
#to create a environment file, it will overide the existing env file
conda env export  >  environment_win.yml
#update
conda env update --prefix --file environment_win.yml  --prune
# Install your top level package myproject using pip. The trick is to use the -e flag when doing the install. This way it is installed in an editable state, and all the edits made to the .py files will be automatically included in the installed package.
pip install -e .
pip freeze
```

to create a execuatble follow the below mentioned process

```bash
# to create exe
pyinstaller --onefile --noconsole .\youtube_synchronizer\interfaces\youtube-playlist-synchronizer.py
# to re-create from spec file after exe is created
pyinstaller youtube-playlist-synchronizer.spec
```

> Note: It is always better to run this program in vpn network.

