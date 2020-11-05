import praw, creds, settings, search, respond, json, traceback, querypushshift, logging, time
from datetime import datetime, timedelta
from logging.handlers import RotatingFileHandler

# Set up logger.
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
log_file = 'among_us.log'

log_handler = RotatingFileHandler(log_file,
        mode='a',
        maxBytes=5 * 1024 * 1024,
        backupCount=2,
        encoding=None,
        delay=0)
log_handler.setFormatter(log_formatter)
log_handler.setLevel(logging.INFO)

logger = logging.getLogger('root')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

logger.info('Bot starting up...')

# Connect bot to reddit and create reddit instance
reddit_client = praw.Reddit(
    client_id=creds.client_id,
    client_secret=creds.client_secret,
    refresh_token=creds.refresh_token,
    user_agent=settings.user_agent
    )

logger.info(f'Logged in as {reddit_client.user.me()}.')

# Get blacklist information.
with open('blacklist.json') as blacklist_file:
    blacklist = json.load(blacklist_file)


# Get starting time to filter only comments made since the bot launched.
search_time = int(datetime.now().timestamp())

# The time of the latest comment we processed.
latest_comment_time = 0

while True:
    try:
        # Set the search_time to be a bit after the last comment we processed so we don't process comments twice.
        if latest_comment_time != 0:
            last_comment_datetime = datetime.fromtimestamp(latest_comment_time) 
            new_datetime = last_comment_datetime + timedelta(seconds = 15) 
            search_time = int(new_datetime.timestamp())

        # Get data from pushshift beta api.
        for data in querypushshift.get_pushshift_comments(min_created_utc=search_time, q='sus'):
            comment = reddit_client.comment(data['id'])

            if comment.created_utc > latest_comment_time:
                logger.debug('Found new latest comment.')
                latest_comment_time = comment.created_utc

            # Check if comment matches trigger, and if so, respond.
            if comment.author.name != reddit_client.user.me() and comment.subreddit.display_name.lower() not in blacklist['disallowed']:
                username = search.check_trigger(comment.body)
                if username:
                    response = respond.build_reply(username)

                    logger.info(f"Responding to {comment.author.name}'s comment...\n"
                            + f"Link: {comment.permalink}\n"
                            + f"---\n{comment.body}\n---\n")

                    comment.reply(respond.build_reply(username))
                    logger.info('Response successful.')


        time.sleep(.05)
    except Exception as e:
        logger.exception('Ran into error. Continuing loop.')

logger.error('Loop broken. Bot shutting down...')
