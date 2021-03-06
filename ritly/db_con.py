import mysql.connector
import json
import os

#TODO throw all of this into a class?
class RitlyDB():

    def __init__(self):
        self.db = self.read_config()
        self.cur = self.db.cursor()

    def read_config(self):
        """Read in DB config file

        Read in configuration file that contains the host, username, and passowrd
        for the MySQL database.
        """
        # path to config.json. Always one directory above 'ritly' package
        CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.json")

        with open(CONFIG_PATH) as json_file:  
            data = json.load(json_file)
            # connect to database 'linkstore' with given config info
            db = mysql.connector.connect(
                host=data['host'],
                user=data['user'],
                passwd=data['passwd'],
                database="linkstore"
            )
        
        return db

    def add_link(self, url: str, link: str):
        """Insert new URL, link pair into the database"""

        cmd = "INSERT INTO links (Url, Link) VALUES (%s, %s);"
        self.cur.execute(cmd, (url, link))
        self.db.commit()

    def lookup(self, url:str):
        # build and exectute lookup query for link associated with URL
        cmd = "SELECT Link FROM links WHERE Url = %s;"
        self.cur.execute(cmd, (url,))

        # fetch results from last query
        ret = self.cur.fetchall()

        # if the return value is an empty list, that means we had no results
        if ret == []:
            return None #TODO maybe throw error


        return ret[0][0]


    
