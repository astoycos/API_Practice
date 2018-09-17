#export GOOGLE_APPLICATION_CREDENTIALS="/Users/andrewstoycos/Documents/Classes_Fall_2018/EC601/Project_1/Mini_Project1/miniproject1-3785356094c8.json"

import io
import os
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

picfiles = []

for filename in os.listdir('/Users/andrewstoycos/Documents/Classes_Fall_2018/EC601/Project_1/Mini_Project1/pic_downloads'):
	statinfo = os.stat('/Users/andrewstoycos/Documents/Classes_Fall_2018/EC601/Project_1/Mini_Project1/pic_downloads/' + filename)	
	print(statinfo.st_size)
	if statinfo.st_size > 0:
		picfiles.append(filename)

del picfiles[0]
picfiles.sort(key = lambda f: int(filter(str.isdigit, f)))


for pics in picfiles:

	# The name of the image file to annotate
	file_name = os.path.join(
	    os.path.dirname(__file__),
	    '/Users/andrewstoycos/Documents/Classes_Fall_2018/EC601/Project_1/Mini_Project1/pic_downloads/' + pics)

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
	    content = image_file.read()

	image = types.Image(content=content)

	# Performs label detection on the image file
	response = client.label_detection(image=image)
	labels = response.label_annotations
	
	
	print(pics)
	
	if len(labels) > 1:
		print(labels[0].description)
			
		font = ImageFont.truetype("/Users/andrewstoycos/Documents/Classes_Fall_2018/EC601/Project_1/Mini_Project1/Crimson-BoldItalic.ttf",25)
		 
		# Opening the file gg.png
		imageFile = '/Users/andrewstoycos/Documents/Classes_Fall_2018/EC601/Project_1/Mini_Project1/pic_downloads/' + pics
		im1=Image.open(imageFile)
			 
		# Drawing the text on the picture
		draw = ImageDraw.Draw(im1)
		draw.text((0, 0),labels[0].description,(255,255,0),font=font)
		draw = ImageDraw.Draw(im1)

		im1.save('/Users/andrewstoycos/Documents/Classes_Fall_2018/EC601/Project_1/Mini_Project1/pic_downloads/' + pics)
	else: 
		continue 


