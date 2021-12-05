from app.twitter.crawler.parser import tweetParse
import tweepy
import json
from twitter.models import *

class TwitterTimeline():
    def __init__(self):
        self.api = self.auth()

    def auth(self):
        api = API.objects.get()
        auth = tweepy.AppAuthHandler(
            api.acess_token,
            api.acess_token_secret
        ) 
        return tweepy.API(auth, wait_on_rate_limit=True)

    def getTimeline(self,user_id):
        data = []
        lastid = Status.objects.filter(user__id=user_id).order_by('-id')[0].id
        
        try:
            for status in tweepy.Cursor(self.api.user_timeline, user_id=user_id,tweet_mode="extended",since_id=lastid,count=200).items():
                data.append(status._json)

        except:
            print('except', id)
        
        tweetParse(data)
            
