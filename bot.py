import praw, creds, settings, search, respond, json, time, traceback
from psaw import PushshiftAPI

# Connect bot to reddit and create reddit instance
reddit_client = praw.Reddit(client_id = creds.client_id,
        client_secret = creds.client_secret,
        refresh_token = creds.refresh_token,
        user_agent = settings.user_agent)

# Use pushshift_api to retrieve comments
pushshift_api = PushshiftAPI(reddit_client)

# Get blacklist information.
with open('blacklist.json') as blacklist_file:
    blacklist = json.load(blacklist_file)


# Get starting time to filter only comments made since the bot launched.
search_time = int(time.time())

while True:
    try:
        for comment in pushshift_api.search_comments(limit = 500, after = search_time):
            if comment.subreddit.name.lower() not in blacklist['disallowed']:
                username = search.check_trigger(comment.body)
                if username:
                    comment.reply(respond.build_reply(username))
    except Exception as e:
        traceback.print_exc()
