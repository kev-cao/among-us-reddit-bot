import praw
import creds
import settings
import search
import respond

# Connect bot to reddit and create reddit instance
reddit_client = praw.Reddit(client_id = creds.client_id,
        client_secret = creds.client_secret,
        refresh_token = creds.refresh_token,
        user_agent = settings.user_agent)

while True:
    try:
        for comment in reddit_client.subreddit('all').stream.comments(skip_existing = True):
            if username := search.check_trigger(comment.body):
                comment.reply(respond.build_reply(username))
    except Exception as e:
        traceback.print_exc()

