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
import mysql.connector
from getpass import getpass
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from prettytable import PrettyTable

pic_directory = 'pic_directory_MYSQL/'


#make MYSQL DATAbase 
username = str(raw_input("Enter your MySQL username: "))

incorrectpass = True

pic_directory = 'pic_directory_MYSQL_' + username + '/'

#if password is incorrect prompt user again 
while(incorrectpass):
	password = str(getpass("Enter your MySQl password: "))

	database_name = username + "_mysql_twitter_db"

	try:
		mydb = mysql.connector.connect(
			user=username,
			passwd=password,
			auth_plugin='mysql_native_password'
		)
		incorrectpass = False

	except mysql.connector.errors.ProgrammingError:
		incorrectpass = True

mycursor = mydb.cursor()

#create new database if one does not exist 
try: 
    mycursor.execute("USE " + database_name)
except mysql.connector.Error as err:
	mycursor.execute("CREATE DATABASE IF NOT EXISTS " + database_name)

mydb.commit()

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
			twitter_module.get_all_tweets(tw_hdl, int(numtweets),True,username)
		except:
			print("Invalid twitter handle")


		#Make new table in database correlating to twitter handle in question  

		mydb = mysql.connector.connect(
			user=username,
			passwd=password,
			database=database_name,
			auth_plugin='mysql_native_password'
		)

		mycursor = mydb.cursor()


		mycursor.execute("CREATE TABLE IF NOT EXISTS " + tw_hdl[1:] + " (pic_filenames VARCHAR(255) PRIMARY KEY, pic_caption VARCHAR(255), pic_caption_weight VARCHAR(255))")

		mydb.commit()

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
				
				#resize image so that all images approximately match  
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
			try:
				values = (str(pics),str(labels[0].description),str(labels[0].score))

				mycursor.execute("INSERT INTO " + tw_hdl[1:] + " (pic_filenames,pic_caption,pic_caption_weight) VALUES (%s, %s, %s)",values)

				mydb.commit()
			except mysql.connector.errors.IntegrityError:
				pass
		print('\n')
except EOFError:
	# on exit show some database statistics
	print('\n')
	print("Below is your " + database_name +" and the various twitter handles that were queryed ")
	
	#print(mycursor.execute("SHOW TABLE STATUS"))

	mydb = mysql.connector.connect(
			user=username,
			passwd=password,
			database=database_name,
			auth_plugin='mysql_native_password'
		)

	mycursor = mydb.cursor()

	my_pics = mydb.cursor()

	my_des = mydb.cursor()

	mycursor.execute("show tables")

	tables = mycursor.fetchall()

	tab = PrettyTable(['Twitter_Handles', '# of Pictures','Most Popular descriptor (word,count)'])
	
	for (table_name,) in tables:
		my_pics.execute('select * from ' + table_name)
		
		records = my_pics.fetchall()

		my_des.execute('SELECT pic_caption, COUNT(pic_caption) AS value_occurrence FROM ' + table_name + ' GROUP BY pic_caption ORDER BY value_occurrence DESC LIMIT 1')

		commons = my_des.fetchall()[0]

		commons = (str(commons[0]),commons[1])

		tab.add_row([str(table_name),str(my_pics.rowcount),str(commons)])
	
	print tab
	



