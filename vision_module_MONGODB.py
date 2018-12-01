#CopyRight 2018 Andrew Stoycos astoycos@bu.edu

# coding: utf-8

#Sources: 
#https://stackoverflow.com/questions/6996603/delete-a-file-or-folder
#http://www.xappsoftware.com/wordpress/2013/04/25/how-to-add-a-text-to-a-picture-using-python/
#https://opensource.com/life/15/2/resize-images-python
#https://cloud.google.com/vision/docs/quickstart-client-libraries#client-libraries-usage-python
#https://pillow.readthedocs.io/en/3.0.x/reference/ImageDraw.html
#https://www.w3schools.com/python/python_mysql_insert.asp
#https://dev.mysql.com/doc/refman/8.0/
#https://stackoverflow.com/questions/12235595/find-most-frequent-value-in-sql-column/35081385

#export GOOGLE_APPLICATION_CREDENTIALS="/Users/andrewstoycos/Documents/Classes_Fall_2018/EC601/Project_1/Mini_Project1/miniproject1-600511521a1c.json"

import twitter_module 
import io
import os
import PIL
from tqdm import tqdm
import pymongo
from getpass import getpass
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from prettytable import PrettyTable

pic_directory = 'pic_directory_MONGODB/'


#make MONGODB DATAbase and  
user = str(raw_input("Enter Mongo_DB username: "))

pic_directory = 'pic_directory_MONGODB_' + user + '/'

myclient = pymongo.MongoClient('localhost', 27017)

dbname = user + '_mongo_twitter_db'

mydb = myclient[dbname]

#continue prompting the user to get tweets and entries to database 
try:
	while True:
		try:
			tw_hdl = str(raw_input("Enter a twitter handle to get tweets from: "))
			numtweets = int(raw_input("Enter number of tweets to be downloaded (Must be 20 or more): "))
		except ValueError:
			print('\nYou did not enter a valid number')
			sys.exit(0)
			#pass in the username of the account you want to download

		try:
			twitter_module.get_all_tweets(tw_hdl, int(numtweets),False,user)
		except:
			print("Invalid twitter handle")
			continue

		#Make new table in database for 

	
		mycol = mydb[tw_hdl[1:]]

		# Instantiates a client
		client = vision.ImageAnnotatorClient()

		picfiles = []

		#makes sure none of the pictures are not currupted and sorts them based on filename 
		for filename in os.listdir(pic_directory+ tw_hdl[1:]):
			statinfo = os.stat(pic_directory + tw_hdl[1:] + '/' + filename)	
			if statinfo.st_size > 0:
				if "labeled_" in filename:
					pass
				else:
					picfiles.append(filename)
			else:
				os.remove(pic_directory + tw_hdl[1:] + '/' + filename)

		#picfiles.sort(key = lambda f: int(filter(str.isdigit, f)))

		#loops throgh pictures 
		for pics in tqdm(picfiles):

			# The name of the image file to annotate
			file_name = os.path.join(
			    os.path.dirname(__file__),
			    pic_directory + tw_hdl[1:] + '/' + pics)

			# Loads the image into memory
			with io.open(file_name, 'rb') as image_file:
			    content = image_file.read()

			image = types.Image(content=content)
				
			# Performs label detection on the image file
			response = client.label_detection(image=image)
			labels = response.label_annotations	

			#makes sure the API did respond with a label 
			if len(labels) > 1:	
				font = ImageFont.truetype('Crimson-BoldItalic.ttf',30)
				 
				# Opening the file gg.png	
				imageFile = pic_directory + tw_hdl[1:] + '/' + pics
				im1=Image.open(imageFile)
				
				#resize image so that all images approximately match in video 
				basewidth = 600 
				wpercent = (basewidth / float(im1.size[0]))
				hsize = int((float(im1.size[1]) * float(wpercent)))
				#ensures video dimensions are even for ffmpeg
				if hsize % 2 == 1:
					hsize = hsize + 1

				im1 = im1.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

				# Drawing the text on the picture
				draw = ImageDraw.Draw(im1)
				draw.text((0,0),labels[0].description,fill = "red",font=font)
				draw = ImageDraw.Draw(im1)
				
				try:		
					im1.save(pic_directory + tw_hdl[1:] + "/" + 'labeled_' + pics)
					os.remove(pic_directory + tw_hdl[1:] + "/" + pics)
				except: 
					os.remove(pic_directory + tw_hdl[1:] + "/" + pics)
			else:
				os.remove(pic_directory + tw_hdl[1:] + "/" + pics) 
				continue 


			#insert filename,caption, caption weight into database 
			filter = {'filename':str(pics)}
			entry = {'$set' : {'filename':str(pics),'pic_caption':str(labels[0].description),'pic_caption_weight':str(labels[0].score)}}

			mycol.update_many(filter,entry,upsert=True)
		print('\n')

except EOFError:
	# on exit show some database statistics
	print('\n')
	print("Below is your " + dbname +" and the various twitter handles that were queryed ")

	collist = mydb.list_collection_names()

	tab = PrettyTable(['Twitter_Handles', '# of Pictures','Most Popular descriptor (word,count)'])
	
	for handles in collist:
		coll = mydb[str(handles)]
		for most_used in coll.aggregate([{"$sortByCount":"$pic_caption"},{"$limit":1}]):
			tab.add_row([str(coll.name),str(coll.count()),(str(most_used["_id"]),most_used["count"])])
	
	print tab
	

