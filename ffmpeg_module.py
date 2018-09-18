#!/usr/bin/env python
#Source
#https://stackoverflow.com/questions/44947505/how-to-make-a-movie-out-of-images-in-python
#https://stackoverflow.com/questions/6996603/delete-a-file-or-folder
#http://hamelot.io/visualization/using-ffmpeg-to-convert-a-set-of-images-into-a-video/

import ffmpy 
import subprocess
import shutil

VID = ['ffmpeg', '-r', '1','-f', 'image2', '-s', '1920x1080', '-i','pic_downloads/%d.jpg', '-vcodec', 'libx264', '-crf',  '25',  '-pix_fmt', 'yuv420p', 'tweet_video.mp4','-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2']

subprocess.call(VID)

shutil.rmtree('pic_downloads') 

