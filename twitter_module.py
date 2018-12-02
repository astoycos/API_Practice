#!/usr/bin/env python

#CopyRight 2018 Andrew Stoycos astoycos@bu.edu

# encoding: utf-8

#Sources:
#https://stackoverflow.com/questions/16211703/how-to-make-a-folder-in-python-mkdir-makedirs-doesnt-do-this-right
#https://miguelmalvarez.com/2015/03/03/download-the-pictures-from-a-twitter-feed-using-python/
#Prateek Mehta file tweetAPIexample 

import tweepy 
import json
import wget
import os
import shutil


#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""



def get_all_tweets(screen_name, tweetnum, db,name):
    
    if(db):
        pic_directory = 'pic_directory_MYSQL_' + name + '/'
    else: 
        pic_directory = 'pic_directory_MONGODB_' + name +'/'

    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    mediatweets = set()
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=(tweetnum/2))
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=(tweetnum/2),max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
    
    #create a set to hold all the media from the tweets 
    pictures = set()

    #loops though all the downloaded tweets 
    for tweet in alltweets:
        
        pic = tweet.entities.get('media',[])
        #pic attempts to grab picture, if there is a picture (i.e len(pic) > 0 ) then it adds it to our set of media
        if(len(pic)>0):
            pictures.add(pic[0]['media_url'])
        else:
            continue
    
    print("%s pictures found in %s tweets" % (len(pictures),tweetnum))

    #creates a folder to store the media in working directory, if it already exists remove it and rewrite 
    if os.path.exists(pic_directory + screen_name[1:]) : 
        pass
    else:
        os.makedirs(pic_directory + screen_name[1:])

    #only download pictures that havent been in database yet 
    for picture in pictures:
        if os.path.exists(pic_directory + screen_name[1:] + '/' + 'labeled_' + str(picture.rsplit('/',1)[1])): 
            #shutil.rmtree('pic_downloads')    
            #os.mkdir('pic_downloads'
            pass
        else:
            wget.download(picture, (pic_directory + screen_name[1:] + '/'))

