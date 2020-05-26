import sqlite3

connection = sqlite3.connect('data.db')         #opening db connection

cursor = connection.cursor()                

cursor.execute('YOUR SQL QUERY HERE')           #all operations are made by (multiple) cursors
connection.commit()                             #save the result of this query to the disk (until then it is kept in memory)

connection.close()                              #closing db connection
