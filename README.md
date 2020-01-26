# Youtube playlist synchronizer

### steps to setup local development

#### pre-Requisites for setting up DEV Environment
1. Install anaconda version 
2. clone this repo to your system wither ssh or https
3. conda env create --file environment_win.yml 
4. Open vscode and add python interprerter from ctrl+shift+p and add conda env.
    
#### Running the project 
1. Run Google-login.py and it creates user_playlist.json file
2. Run utils.py and it creates folders and started syncing viedos in selected parent directory 

Note: It is always better to run this program in vpn network.


please go throuugh for more details 
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually
change code as per python pytube C:\Users\bhara\.conda\envs\youtube-playlist-sync\Lib\site-packages\pytube

```
to create a environment file it will overide the existing env file
conda env export --from-history >  environment_win.yml
update
conda env update --prefix --file environment_win.yml  --prune
```


```
 #to create exe
 pyinstaller --onefile youtube-playlist-synchronizer.py
 # to re-create from spec file after exe is created
 pyinstaller youtube-playlist-synchronizer.spec
```