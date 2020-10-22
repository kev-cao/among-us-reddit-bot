# Among Us Reddit Bot
A Reddit script that makes an Among Us meme in response to triggering comments.

## Context
Most of the applications I've made so far have been local, and do not really use outside APIs (except for the Discord bots).
Since I've already made a couple of Discord bots, I figured I should try other APIs, which lead me Reddit. The bot seemed fairly simple at first,
and I was just using `praw` to connect my script to the bot account and to fetch the data from /r/all.

However, I was noticing a lot of problems with that, as `praw` was unable to keep up with the load and would often skip comments. A bit of research led
me to /u/Stuck_In_The_Matrix's PushShift.io API, which was more reliable when fetching comments. At the time of development, the released version was slow with
updating the database with new comments, so I used the beta version instead, which was much faster. This gave me more experience with using simple `GET` requests 
to fetch the data I wanted.

## What does it do?
Upon finding a comment that matches one of the triggering regular expressions, the bot will respond to the comment with 

. 　　　。　　　　•　 　ﾟ　　。 　　.

　　　.　　　 　　.　　　　　。　　 。　. 　

.　　 。　　　　　 ඞ 。 . 　　 • 　　　　•

 ﾟ   /u/Username was not an Impostor.     。 .

　　'　　　 2 Impostors remain 　 　　。

ﾟ　　　.　　　.     , 　 　 　.         .

(Whether or not the user is an imposter is chosen randomly)

## Relevant Links
[Beta PushShift API](https://beta.pushshift.io/redoc)

[Praw API](https://praw.readthedocs.io/en/latest/)

[Reddit API Rules](https://github.com/reddit-archive/reddit/wiki/API#rules)

## How to Setup
You will need to have Python's `pip` installed on your machine. [Instructions here.](https://pip.pypa.io/en/stable/installing/)

Run `pip install -r requirements.txt` while in the cloned repository to install required libraries.

You will also need some files to store sensitive information. I've labeled mine as `creds.py` and `settings.py`, both of which are gitignore'd.

In `creds.py`, set up the following variables:

```py
# creds.py
client_id = 'client-id'
client_secret = 'secret-key'
```

To get the `client_id` and `client_secret`, create a bot application on Reddit and the information will be stored there. To create a bot, go to
https://www.reddit.com/prefs/apps/ while signed in on the bot account. Select *Create App*. Give the bot a name, and make sure it is selected as a script.
The redirect URI is required, and set it to `http://localhost:8080`. Create the application, and you should see the information needed for your bot.

![client info](https://i.imgur.com/U8vrP47.png)

You will also need to retrieve a refresh token for OAuth. Once you've created the `creds.py` file, run `python setup.py` and follow the instructions. You will
be given a refresh token. Add that refresh token to the `creds.py` file with the variable `refresh_token`. So your `creds.py` file should look something like this:

```py
# creds.py
client_id = 'client-id'
client_secret = 'secret-key'
refresh_token = 'refresh-token'
```

You'll also need to create a `settings.py` file. In here, you will need to create variables for `scopes`, `redirect_uri`, and `user_agent`. `scopes` and `redirect_uri`
should be set to the values seen below, but the `user_agent` should be a secret name for your bot. According to the Reddit API rules, **you must not lie about your user_agent**, and others should not know the name. If the name is ever stolen, change the `user_agent` name. 

```py
# settings.py
user_agent = 'Secret'
scopes = ['identity', 'submit', 'read']
redirect_uri = 'http://localhost:8080'
```

Once you have the above files set up, you should be good to go. Run the script with the command `python bot.py`.
