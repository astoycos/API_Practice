import io
import os
import PIL
from tqdm import tqdm
import mysql.connector
import pymongo
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from prettytable import PrettyTable


pic_directory_mongo = 'pic_directory_MONGODB/'

# My_sql database API 
class mysql_tweet: 

    def __init__(self,username,password,database):
        self.user = username
        self.database = database
        self.pic_directory_mysql = 'pic_directory_MYSQL/'
        self.mydb = mysql.connector.connect(
            user=username,
            passwd=password,
            database=username + "_mysql_twitter_db",
            auth_plugin='mysql_native_password'
        )
        
    def show_info(self):
        base_cursor = self.mydb.cursor()
        tab_cursor = self.mydb.cursor()
        data_cursor = self.mydb.cursor()

        base_cursor.execute("show tables")

        tables = base_cursor.fetchall()

        info = PrettyTable(['Twitter_Handles', '# of Pictures','Most Popular descriptor (word,count)'])
        
        for (table_name,) in tables:
            tab_cursor.execute('select * from ' + table_name)
            
            records = tab_cursor.fetchall()

            data_cursor.execute('SELECT pic_caption, COUNT(pic_caption) AS value_occurrence FROM ' + table_name + ' GROUP BY pic_caption ORDER BY value_occurrence DESC LIMIT 1')

            commons = data_cursor.fetchall()[0]

            commons = (str(commons[0]),commons[1])

            info.add_row([str(table_name),str(tab_cursor.rowcount),str(commons)])
        print info

    def find_des(self,description): 
        base_cursor = self.mydb.cursor()
        tab_cursor = self.mydb.cursor()
        data_cursor = self.mydb.cursor()

        base_cursor.execute("show tables")


        tables = base_cursor.fetchall()

        print('Finding pictures with the description: ' + description)

        for (table_name,) in tables:
            data_cursor.execute(''' SELECT * FROM ''' + table_name + ''' WHERE (pic_caption LIKE '%''' + description + '''%')''')

            try:
                out = data_cursor.fetchall()[0]
                if (len(out) == 0):
                    pass
                else: 
                    filename = str(out[0])

                    print('Twitter Account : %s' % str(table_name))

                    print('Picture: %s' % filename)

                    im = Image.open(self.pic_directory_mysql + str(table_name) + '/labeled_' + str(filename))

                    im.show()
            except:
                pass


#Mongo database API 
class mongo_tweet:

    def __init__(self,username):
        self.user = username
        self.pic_directory_mongo = 'pic_directory_MONGODB/'
        self.myclient = pymongo.MongoClient('localhost', 27017)
        self.database = username + '_mongo_twitter_db'
        self.mydb = self.myclient[self.database]

    def show_info(self):
        print("Below is your " + self.database +" and the various twitter handles that were queryed ")

        collist = self.mydb.list_collection_names()

        tab = PrettyTable(['Twitter_Handles', '# of Pictures','Most Popular descriptor (word,count)'])
        
        for handles in collist:
            coll = self.mydb[str(handles)]
            for most_used in coll.aggregate([{"$sortByCount":"$pic_caption"},{"$limit":1}]):
                tab.add_row([str(coll.name),str(coll.count()),(str(most_used["_id"]),most_used["count"])])
        
        print tab

    def find_des(self,description): 
        collist = self.mydb.list_collection_names()

        for handles in collist:
            coll = self.mydb[str(handles)]

            find_filter = {'pic_caption':description}

            cursor = coll.find(find_filter)

            for documents in cursor:
                print('Twitter Account : %s' % str(coll.name))

                print('Picture: %s' % documents['filename'])

                im = Image.open(self.pic_directory_mongo + str(coll.name) + '/labeled_' + str(documents['filename']))

                im.show()

'''
if __name__ == '__main__':

    mysql_database = mysql_tweet('root', 'password','root')

    mysql_database.show_info()

    mysql_database.find_des('wave')

    mongo_database = mongo_tweet('andrew')

    mongo_database.show_info()

    mongo_database.find_des('wave')

'''








    
