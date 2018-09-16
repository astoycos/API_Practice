#!/usr/bin/env python

import ffmpy 
import subprocess

VID = ['ffmpeg', '-r', '1','-f', 'image2', '-s', '1920x1080', '-i','/Users/andrewstoycos/Documents/Classes_Fall_2018/EC601/Project_1/Mini_Project1/pic_downloads/%d.jpg', '-vcodec', 'libx264', '-crf',  '25', 'tweet_video.mp4']

subprocess.call(VID)


