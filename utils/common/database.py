import sqlite3

'''
Concerned with storing and retreiving books to db
'''

#defined filename where our records are stored


#creating database
def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS  books(name text, author text, read integer)')
    connection.commit()
    connection.close()
    
        
#adding book record to database
def add_book(name,author):
    #do not use f string in sql statements to avoid SQL inject
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
    connection.commit()
    connection.close()


#retrieve all books from the table (db)
def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    #books = cursor.fetchall()           #returns a list of tuples [(name, author, read),(name, author, read)]
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]   #this will give us a dictionary from the tuples lists
    #connection.commit()                 #commit not needed as we were not writing anything to db
    connection.close()
    return books                        #return books dictionary  (list function works)

#marking book as read in db
def mark_book_read(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read = 1 WHERE name = ?',(name, ))     #comma after name as we want to make sure it is tupple
    connection.commit()
    connection.close()


#function for removing book record from the file
def delete_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM  books WHERE name = ?',(name, ))     #comma after name as we want to make sure it is tupple
    connection.commit()
    connection.close()
   

