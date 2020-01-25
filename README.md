# Youtube playlist synchronizer

### steps to setup local development

please go throuugh for more details 
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually
change code as per python pytube C:\Users\bhara\.conda\envs\youtube-playlist-sync\Lib\site-packages\pytube

```
to create a environment file it will overide the existing env file
conda env export --from-history >  environment_win.yml
update
conda env update --prefix --file environment_win.yml  --prune
```