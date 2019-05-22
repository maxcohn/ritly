import mysql.connector
import json


"""
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    passwd="yourpassword"
)
"""

import os
def read_config():
    """Read in DB config file

    Read in configuration file that contains the host, username, and passowrd
    for the MySQL database.
    """
    # path to config.json. Always one directory above 'ritly' package
    CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.json")
    print(os.path.abspath(__file__))
    with open(CONFIG_PATH) as json_file:  
        data = json.load(json_file)
        print(data['user'])
        print(data['passwd'])
        print(data['host'])

read_config()