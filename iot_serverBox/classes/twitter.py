from twython import Twython
from datetime import datetime

consumer_key        = 'TBD'
consumer_secret     = 'TBD'
access_token        = 'TBD'
access_token_secret = 'TBD'

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
def tweet():
    message = "Test ouverture " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    twitter.update_status(status=message)
    print("Tweeted: %s" % message)

def tweetList():
    user_tweets = twitter.get_user_timeline(screen_name='lazuryte1',include_rts=True)
    for tweet in user_tweets:
        tweet['text'] = Twython.html_for_tweet(tweet)
        print(tweet['text'])