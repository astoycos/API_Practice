#!/usr/bin/env python
# encoding: utf-8
#Sources:
#https://stackoverflow.com/questions/16211703/how-to-make-a-folder-in-python-mkdir-makedirs-doesnt-do-this-right
#https://miguelmalvarez.com/2015/03/03/download-the-pictures-from-a-twitter-feed-using-python/


import tweepy #https://github.com/tweepy/tweepy
import json
import wget
import os
import shutil


#Twitter API credentials
consumer_key = "V7yRfImaW76l7x1YJlqZqugtx"
consumer_secret = "5mHVgrxA280I97JVK0EpNluBIMBJK9p6FEMfvmeNND0pqxoy7n"
access_key = "1039252626829963270-fdMfABc65z4oTfh6t8WbHelgjrmONM"
access_secret = "QbKfrq7J4uMv292kdIhQpZqbJvpuW49ZRILQCGJwFgxST"


def get_all_tweets(screen_name):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    mediatweets = set()
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=20)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=20,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print("...%s tweets downloaded so far" % (len(alltweets)))
    
    print(len(alltweets))


    pictures = set()

    for tweet in alltweets:
        #ensures the media is a picture 
        pic = tweet.entities.get('media',[])
        if(len(pic)>0):
            pictures.add(pic[0]['media_url'])
        else:
            continue

    if os.path.exists('pic_downloads') : 
        shutil.rmtree('pic_downloads') 
        os.mkdir('pic_downloads')
    else:
        os.mkdir('pic_downloads')

    for index, picture in enumerate(pictures):
        wget.download(picture, ("pic_downloads/" + str(index) + ".jpg"))
        

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@photoblggr")
