# Mini_Project3

This project was used as a way of gaining experience with both APIs(twitter and google vision) and relational(MySQL) and nonrelational(MongoDB) databases. It downloads pictures from a specified twitter handle and then labels them using the google Vision API. Then it saves the pictutes and accompying data in local intances of both Mysql and Mongo databases. Finally the provided API creates some basic functions to query these databases.

## Module Descriptions

### Prerequsites 

This program was created using Python2.7, MySQL 8.0.13, and Mongo_DB 4.04

MySQL community server must be installed via the following [instructions](https://dev.mysql.com/doc/mysql-getting-started/en/)

MongoDB must be installed and connected following these [instructions](https://docs.mongodb.com/manual/installation/#tutorial-installation)

All credentials must be your own i.e twitter and google vision keys. For tweepy they can be manually entered at the heady of twitter_module.py, for google vision the user must run the following command line 
		
	- MAC -> export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
	- PC -> $env:GOOGLE_APPLICATION_CREDENTIALS="[PATH]" 

The Project is split into three different modules, all add on python libaries can be installed using 
	
	PIP install <library>
	
	Required add on Libraries: 
	tweepy
	google-cloud-vision 
	mysql-connector 
	pymongo 
	wget
	shutil
	Pillow
	tqdm
	prettytable
	getpass

### twitter_module.py

The first module interacts with the twitter API using a python wrapper,tweepy, in order to download the user entered number of tweets with the function "get_all_tweets()". It then pulls the pictures from the tweet objects and stores them in a new directory, "Pic_downloads_(mongo or mysql)/twitter_handle". If twitter handle is invalid it returns an error and propts the user to enter another one.  It is called by the other two modules.  
	YOU MUST ENTER YOUR OWN TWITTER CREDENTIALS 
	

### vision_module_MYSQL.py

This module prompts the user to enter their MySQL credentials, and creates a database with the name 'useername_mysql_twitter_db', and if correct asks for a twitter handle to query. If a valid handle is entered twitter_module.get_all_tweets() is called.  Once all the pictures are downloaded the google vision API finds a list of labels for the pictures stored in 'pic_downloads_mysql/'.  It then uses the python API Pillow in order to resize all the images and caption them using the labels created from the google vision API.  Following picture labeling, it creates a table called 'twitter handle' in the database, where the picture filenames, captions and caption confidences are stored. It will continue to prompt the user to enter twitter handles, and create new database entries until 'ctl-d' is hit. Finally the program will exit showing a quck summary reguarding the newly created database.

![MYSQL example](https://raw.githubusercontent.com/astoycos/Mini_Project1/Mini_Project3/mysql_ex.png)


### vision_module_MONGODB.py 
	
This module prompts the user to enter a mongo database name, and creates a database with the name 'name_mongo_twitter_db', and if correct asks for a twitter handle to query. If a valid handle is entered twitter_module.get_all_tweets() is called.  Once all the pictures are downloaded the google vision API finds a list of labels for the pictures stored in 'pic_downloads_mongo/'.  It then uses the python API Pillow in order to resize all the images and caption them using the labels created from the google vision API.  Following picture labeling, it creates a collection called 'twitter handle' in the database, where the picture filenames, captions and caption confidences are stored as documents. It will continue to prompt the user to enter twitter handles, and create new database entries until 'ctl-d' is hit. Finally the program will exit showing a quck summary reguarding the newly created database.

![MONGODB example](https://raw.githubusercontent.com/astoycos/Mini_Project1/Mini_Project3/mongo_ex.png)

### API.py

This module provides an API to interact with the databases created by twitter_module.py and vision_module_MYSQL.py. It contains two main funtions, show_info() which shows some quick statistics about a database, and find_des(description) which allows the user to search the database for a specific picture caption. If a picture is found with the description, it will print the twitter handle it was downloaded from and then display the image. 

a quick demo is provided in demo.py 


## DEMO

**The only erroneous files in the github is a font file for the labels and a Readme
