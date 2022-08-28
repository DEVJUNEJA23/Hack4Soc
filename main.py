import tweepy as twitter
import time,datetime

API_KEY = "TcBIaNyX4Y4kbdqN8fe1TxF3P"
API_SECRET_KEY = "ayDmV53D4kLKewfYJiDv3F1iN1HMeGbGFPbrZuwdvpOeb8f1e9"
ACCESS_TOKEN = "1563058515706802177-PgOee9SPuyPbuhf70mTiLcUv1kl6Fv"
SECRET_ACCESS_TOKEN = "3zl50tYyAy6nUOWOhrgGcucjHWhphtl9uCTKFcG9WThm2"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAACSJgQEAAAAAtAPHPKBaYjY3PuIBql%2F4GLEEDnM%3DYukS22hT8xgIhA4ZrG4XhcU9XZPEODPcaCsgdBZ3xWA89wYTzH"
TWITTER_USERNAME = "AayushGoyaal"


#client = tweepy.Client(BEARER_TOKEN,API_KEY,API_SECRET_KEY,ACCESS_TOKEN,SECRET_ACCESS_TOKEN)
auth = twitter.OAuthHandler(API_KEY,API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,SECRET_ACCESS_TOKEN)
api = twitter.API(auth)


file = open("file.txt", mode="a")

def search_tweet(hashtag,delay):
    while True:
        print(f"\n{datetime.datetime.now()}\n")

        for tweet in twitter.Cursor(api.search_tweets, q=hashtag, rpp=4).items(4):

            try:
                #print(tweet.text)

                tweet_text = dict(tweet._json)["text"]
                #print(tweet_text)
                review = tweet_text.replace("#ourngo","")
                review = review.replace("#dphelpedme","")

                file.write(f"{review},\n")
                print(review)




            except twitter.errors.TweepyException as error:

                print(error)


        time.sleep(delay)



search_tweet("#ourngo",18)