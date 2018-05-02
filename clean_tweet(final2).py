# importing the module
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import re
import tweepy
import codecs
#import tweepy
count=0
# personal details
consumer_key=""
consumer_secret =""
access_token =""
access_token_secret =""

def processTweet2(tweet):
    # process the tweets
    #Convert to lower case
    tweet = tweet.lower()
    tweet = re.sub(r'\s?[0-9]+\.?[0-9]*','',tweet)
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
                       #remove rt
    tweet = re.sub("rt|RT",'', tweet) # remove Retweet
    
    #trim
    tweet = tweet.strip('\'"')
    tweet = re.sub('[^a-zA-Z0-9 \n\.]', '', tweet)
   

    return tweet    
 
class listener(StreamListener):

    '''def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
       # username = all_data["user"]["screen_name"]
        #for tweet in tweepy.Cursor(api.search,q="Modi",count=10,lang="en").items(10):'''
    def on_status(self,status):
        if hasattr(status,'retweeted_status'):
            try:
                tweet=status.retweeted_status.extended_tweet["full_text"]
            except:
                tweet = status.retweeted_status.text
        else:
            try:
                tweet = status.extended_tweet["full_text"]
            except AttributeError:
                tweet = status.text
                
                
                    
        
        x=processTweet2(tweet)
        print(x)
        savefile = open('C:\\Users\\Ritesh\\Desktop\\txt\\tweet_extracted26.txt', 'a',encoding='utf-8') 
        
        savefile.write(x+'\n')
        
        
        savefile.close()

        
        global count
        
        count=count+1
        if count==10:
            return False
        else :
            return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


twitterStream = Stream(auth, listener(count))
twitterStream.filter(track=["dhoni"],languages=['en'])
