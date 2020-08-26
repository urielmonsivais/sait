import mysql.connector
import os
from mysql.connector import Error
from dotenv import load_dotenv
load_dotenv()

class DB():
    connection = None
    def __init__(self):
        super().__init__()        

    def open(self):
        try:
            self.connection = mysql.connector.connect(host=os.getenv('DB_HOST'),
                                                  database=os.getenv('DB_NAME'),
                                                  user=os.getenv('DB_USER'),
                                                  password=os.getenv('DB_PASSWORD'))
        except expression as Error:
            print("Connection error")
        print("Successfully Connection")


    def get_connection(self):
        return self.connection
        
    def is_connected(self):
        self.connection.is_connected()

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")
