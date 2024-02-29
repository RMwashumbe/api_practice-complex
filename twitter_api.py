import tweepy

consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)


def get_tweets(username):
    tweets = api.user_timeline(screen_name=username, count=10)
    for tweet in tweets:
        print(tweet.text)


username = input("Enter Twitter username: ")
get_tweets(username)
