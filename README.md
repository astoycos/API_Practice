# Mini_Project1

The Project is Split into three modules and should be run in the following order 

1.twitter_module.py
	The first module works by downloading the pictures to a newly created diretory, pic_downloads, using module #1, which interacts with the twitter API using a python wrapper tweepy

2.vision_module.py
	The second module works by using the google vision API in order to find a list of labels for the pictures stored in 'pic_downloads' by the previous module.  It then uses the python API Pillow in order to resize all the images and caption them using the labels created from the google vision API.  It then resaves the images while also errorchecking the process

3.ffmpeg_module.py 
	The finial module is relatively simple, it uses the a python subprocess to access the FFmpeg API, which then concatinates all the pictures into a video, 'tweet_video.mp4'.  It then deletes the directory 'pic_downloads' and all its children files 

