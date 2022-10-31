import tweepy
import pandas
import csv

from tweepy.models import Status

consumer_key = "3XLPR6xDhUhfTBdx75iRqb5z3"
consumer_secret = "FuTUkC1g3CKITYY0fWwnMQvTCWpaXqr3crD9npatvDsCcZl96O"
access_token = "447844712-VVWhhzGCRfg2o5mbhxpOnP8Riy5GPebhWB785EQ1"
access_token_secret = "IxowplC7iI3iGZRcVM0TZXu409nfwkcMPL5STuynNl56e"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
data = tweepy.Cursor(api.search_tweets, q="vaksin booster", lang="id", count=250, until="2022-05-24", tweet_mode="extended").items()


outfile = open('D:/datasetTA/datasetCov44.csv','w', encoding='utf-8')
out = csv.writer(outfile)

for tweet in data:
    status = api.get_status(tweet.id, tweet_mode="extended")
    try:
        text = status.retweeted_status.full_text
    except AttributeError:  # Not a Retweet
        text= status.full_text
    # text = tweet.full_text
    id = tweet.id
    user = tweet.user.name
    created = tweet.created_at 

    dataset = [id, user, text, created]
    out.writerows([dataset])
out = csv.writer(outfile)
outfile.close()
    
