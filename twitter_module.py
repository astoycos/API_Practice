#!/usr/bin/env python
# encoding: utf-8


import tweepy #https://github.com/tweepy/tweepy
import json
import wget


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
    new_tweets = api.user_timeline(screen_name = screen_name,count=50)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=50,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print("...%s tweets downloaded so far" % (len(alltweets)))
    '''   
    #write tweet objects to JSON
    file = open('tweet.json', 'w') 
    print("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        json.dump(status._json,file,sort_keys = True,indent = 4)
    
    #close the file
    print("Done")
    print(len(alltweets))
    file.close()
    '''
    print(len(alltweets))

    pictures = set()

    for tweet in alltweets:
        for media in tweet.entities.get("media",[{}]):
            #get media from tweets
            if(media.get("type",None) == "photo"):
                #ensures the media is a picture 
                pic = tweet.entities.get('media',[])
                pictures.add(pic[0]['media_url'])


         

    """if status.entities["media"][0]["type"] == "photo":
        pic = status.entities.get("media", [])
        mediatweets.add(pic[0]["media_url"]) """



    for index, picture in enumerate(pictures):
        wget.download(picture, ("/Users/andrewstoycos/Documents/Classes_Fall_2018/EC601/Project_1/Mini_Project1/pic_downloads/" + str(index + 1) + ".jpg"))
        

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@photoblggr")
