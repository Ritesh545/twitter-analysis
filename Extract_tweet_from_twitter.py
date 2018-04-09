# importing the module
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
#import tweepy
count=0
# personal details
consumer_key ="xxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret ="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token ="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret ="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
 
class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
        print((username,tweet))
        
        global count
        
        count=count+1
        if count==50:
            return False
        else :
            return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, listener(count))
twitterStream.filter(track=["obama"])