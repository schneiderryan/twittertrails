import tweepy
import logging
import time
import config


def create_api():
    # Authenticate to Twitter

    auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
    auth.set_access_token(config.access_token, config.access_secret)

    # Create API object
    api = tweepy.API(auth)
    return api


# Create a tweet
# api.update_status("Hello Tweepy")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
                               since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")

            if not tweet.user.following:
                tweet.user.follow()

            api.update_status(
                status='My status update',
                in_reply_to_status_id=tweet.id,
                auto_populate_reply_metadata=True
            )
    return new_since_id


def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, ["trail", "running, biking"], since_id)
        logger.info("Waiting...")
        time.sleep(60)


if __name__ == "__main__":
    main()
