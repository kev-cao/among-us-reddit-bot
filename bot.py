import praw, creds, settings, search, respond, json

# Connect bot to reddit and create reddit instance
reddit_client = praw.Reddit(client_id = creds.client_id,
        client_secret = creds.client_secret,
        refresh_token = creds.refresh_token,
        user_agent = settings.user_agent)

# Get blacklist information.
with open('blacklist.json') as blacklist_file:
    blacklist = json.load(blacklist_file)


while True:
    try:
        for comment in reddit_client.subreddit('DefCodingBots').stream.comments(skip_existing = True):
            if comment.subreddit.name not in blacklist['disallowed']:
                username = search.check_trigger(comment.body)
                if username:
                    comment.reply(respond.build_reply(username))
    except Exception as e:
        traceback.print_exc()

