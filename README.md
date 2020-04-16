# Messenger-Spotify-Bot
A python facebook messenger chat bot using fbchat and Spotipy that automatically adds music tracks sent in the conversation to the user's playlist. It is especially made for messenger groups where people post Spotify tracks (using the share button on Spotify). It runs 24/7 on Heroku.

## Dependencies

The dependencies for this python application are defined in the `requirements.txt` file. Heroku will automatically install the packages. If you want to install them automatically on your own device, use this command in bash.

```bash
pip3 install -r requirements.txt
```

## Usage

First go to the Spotify for Developers website (https://developer.spotify.com/). Go to your dashboard and create a new application. Change the redirect-uri of your app to 'http://google.com/', you will need it later. You will also need the `Client ID` and `Clien Secret`. You will also need your Spotify `user id` and `playlist id` which you can find by copying your profile or playlist. The last thing you need is the Facebook `thread id`, which can be found if you go to the following link: https://www.facebook.com/messages/t/. It is the long number after the /t/.

### Locally
Clone this repository and make sure your bash window is navigated in the folder where you cloned this repository. Add the correct environment variables like this:

```bash
export FACEBOOK_LOGIN="value"
export FACEBOOK_PASSWORD="value"
export FACEBOOK_THREAD="value"
export SPOTIFY_USERNAME="value"
export SPOTIFY_PLAYLIST="value"
export SPOTIPY_CLIENT_ID="value"
export SPOTIPY_CLIENT_SECRET="value"
export SPOTIPY_REDIRECT_URI="value"
```

After you have set the environment variables, launch the bot like this:

```bash
python3 app.py
```
### On Heroku

Make sure you have the Heroku CLI (https://devcenter.heroku.com/articles/heroku-cli) installed. Clone this repository and install it to your Heroku account. Make sure your bash window is navigated in the folder where you cloned this repository.

```bash
heroku login
git init
```

Then create a new app on Heroku. Go to the settings of your created app, go to "Buildpacks" and choose Python. Then go "Config vars" and add the needed config variables. These are: `FACEBOOK_LOGIN`, `FACEBOOK_PASSWORD`, `FACEBOOK_THREAD`, `SPOTIFY_USERNAME`, `SPOTIFY_PLAYLIST`, `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET` and `SPOTIPY_REDIRECT_URI`. 

![Choose the python buildpack](https://github.com/othellodesutter/Messenger-Spotify-Bot/blob/master/img/buildpack.png)

![Set the correct environment variables](https://github.com/othellodesutter/Messenger-Spotify-Bot/blob/master/img/config_variables.png)

Save the changes and copy the name of your new app. Open your bash window:

```bash
heroku git:remote -a <name of your app>
git add .
git commit -am "<message>"
git push heroku master
```

If everything went right, your python script is now running online. Test it by pasting a the link to a Spotify track in the group chat, for example https://open.spotify.com/track/3VqMzQp2hso8CQpYNKxNNy?si=Wm7BsHHkRzCrK6npN6CKLQ.

## Contributing
You can do whatever you want with this repository! Let me know if something is wrong or if you want to help.
