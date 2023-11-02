import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '7492'
)

#prepare a cursor object
#used to connect with my sql for sql queries in python

cursorObject = dataBase.cursor()

#create databse
cursorObject.execute("CREATE DATABASE applicationsDB")

print("All Done!")