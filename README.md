# Mini_Project1

The Project is Split into three modules and should be run in the following order 

# 1.twitter_module.py
The first module interacts with the twitter API using a python wrapper tweepy in order to download the user entered number of tweets. It then pulls the pictures from the tweet objects and stores them in a new directory, "Pic_downloads". 
	YOU MUST ENTER YOUR OWN TWITTER CREDENTIALS 

	Required add on Libraries: tweepy, wget

# 2.vision_module.py
The second module works by using the google vision API in order to find a list of labels for the pictures stored in 'pic_downloads' by the previous module.  It then uses the python API Pillow in order to resize all the images and caption them using the labels created from the google vision API.  It then resaves the images while also errorchecking the process
	YOU MUST ENTER YOUR OWN GOOGLE API CREDENTIALS IN TERMINAL
		- MAC -> export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
		- PC -> $env:GOOGLE_APPLICATION_CREDENTIALS="[PATH]"

	Required add on Libraries: google-cloud-vision, Pillow 

# 3.ffmpeg_module.py 
The finial module is relatively simple, it uses the a python subprocess to access the FFmpeg API, which then concatinates all the pictures into a video, 'tweet_video.mp4' that can be played with any video player.  It then deletes the directory 'pic_downloads' and all its children files 

	Required add on Libraries: ffmpeg


# EXECUTION:
In order to create a new video simply clone the github and run 1. Python twitter_module.py, 2. Python vision_module.py, and finally 3.Python ffmpeg_module.py 

**The only erroneous files in the github are a .ttf font file for the labels and a Readme
