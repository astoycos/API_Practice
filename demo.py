# -*- coding: utf-8 -*-

import API
import subprocess
from getpass import getpass
import os 

### This program is used to test the API.py file, it loads two existing databases included in the github and 
### exexutes some operations on them 

### Following use of demo you can add to the databases using Vision_module_(MYSQL or MONGODB).py but If you would 
### like to make new databases be sure to delete the ones used for the demo 

## The databases created by this program will be:
	## Mongo -> user + '_mongo_twitter_db'
	## MySQL -> username + '_mysql_twitter_db'

# DEMO of MONGODB
user = str(raw_input("Enter Mongo_DB username: "))

#populate database from mongo dump 
import_mongo = ['mongorestore','--host', 'localhost' ,'--port' ,'27017' ,'--db',user + '_mongo_twitter_db','astoycos_mongo_twitter_db']

subprocess.call(import_mongo)

#make sure pic directories are correctly named

customized_pics = ['mv','pic_directory_MONGODB_astoycos','pic_directory_MONGODB_' + user]

subprocess.call(customized_pics,stdout=open(os.devnull, 'wb'),stderr=open(os.devnull, 'wb'))

print("Demo of mongoDB implementation close picture windows to continue")

#call API 
mongo_database = API.mongo_tweet(user)

mongo_database.show_info()

#change second argument to True to display labeled pictures

mongo_database.find_des('wave',False)

#DEMO OF MYSQL
print('\n')
print("Demo of MySQL")

username = str(raw_input("Enter your MySQL username: "))

password = str(getpass("Enter your MySQl password: "))

#make sure pic_directories are correctly used  
customized_pics = ['mv','pic_directory_MYSQL_root','pic_directory_MYSQL_' + username]

subprocess.call(customized_pics,stdout=open(os.devnull, 'wb'),stderr=open(os.devnull, 'wb'))

#make database to load .sql file into
proc = subprocess.Popen(["mysql", "-u" + username, "-p" +password],
	stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr = subprocess.PIPE)

output, errors = proc.communicate("CREATE DATABASE " + username + "_mysql_twitter_db;")

#populate database from "mysql_twitter.sql"

proc = subprocess.Popen(["mysql", "-u" + username, "-p" +password, username + "_mysql_twitter_db"],
	stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr = subprocess.PIPE)

output, errors = proc.communicate(file("mysql_twitter.sql").read())

#use API

mysql_database = API.mysql_tweet(username, password)

mysql_database.show_info()

#change second field to True to show found pictures 

mysql_database.find_des('wave',False)


