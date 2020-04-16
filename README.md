# Messenger-Spotify-Bot
A python facebook messenger chat bot using fbchat and Spotipy that automatically adds music tracks sent in the conversation to the user's playlist. It is especially made for messenger groups where people post Spotify tracks (using the share-button on spotify). It runs 24/7 on Heroku.

## Dependencies

The dependencies for this python application are defined in the `requirements.txt` file. Heroku will automatically install the packages. If you want to install them automatically on your own device, use this command in bash.

```bash
pip3 install -r requirements.txt
```

## Usage

### Locally
Open the folder where the app.py file is located. Open it and it will be clear. It automatically creates a new directory inside the directory where the app.py is located where the episodes will be stored.

```bash
python3 app.py
```
### On Heroku

Make sure you have the Heroku CLI (https://devcenter.heroku.com/articles/heroku-cli) installed. Clone this repository and install it to your Heroku account. Make sure your bash window is navigated in the folder where you cloned this repository.

```bash
heroku login
git init
```

Then create a new app on Heroku. Go to the settings of your created app, go to "Buildpacks" and choose Python. Then go "Config vars" and add the needed config variables. These are: `FACEBOOK_LOGIN`, `FACEBOOK_PASSWORD`, `FACEBOOK_THREAD`, ``, ``, ``
to Save the changes and copy the name of your new app. Open your bash window:

```bash
heroku git:remote -a <name of your app>
git add .
git commit -am "<message>"
git push heroku master
```

### Example how it will look like

![Example](https://github.com/othellodesutter/VRT-NU-Downloader/blob/master/img/example1.png)

## Contributing
You can do whatever you want with this repository! Let me know if something is wrong or if you want to help.
