import praw, creds, settings, search, respond, json, traceback, querypushshift
from datetime import datetime, timedelta

# Connect bot to reddit and create reddit instance
reddit_client = praw.Reddit(client_id = creds.client_id,
        client_secret = creds.client_secret,
        refresh_token = creds.refresh_token,
        user_agent = settings.user_agent)

# Get blacklist information.
with open('blacklist.json') as blacklist_file:
    blacklist = json.load(blacklist_file)


# Get starting time to filter only comments made since the bot launched.
search_time = int(datetime.now().timestamp())

# The last comment we processed
last_comment = None

while True:
    try:
        # Set the search_time to be a bit after the last comment we processed so we don't process comments twice.
        if last_comment:
            last_comment_datetime = datetime.fromtimestamp(last_comment.created_utc) 
            new_datetime = last_comment_datetime + timedelta(seconds = 1) 
            search_time = int(new_datetime.timestamp())

        # Get data from pushshift beta api.
        for data in querypushshift.get_pushshift_comments(min_created_utc = search_time, q = 'sus'):
            comment = reddit_client.comment(data['id'])
            
            # Check if comment matches trigger, and if so, respond.
            if comment.subreddit.name.lower() not in blacklist['disallowed']:
                username = search.check_trigger(comment.body)
                if username:
                    comment.reply(respond.build_reply(username))

            last_comment = comment
    except Exception as e:
        traceback.print_exc()
