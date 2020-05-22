import json
import os


'''
Concerned with storing and retreiving books from a list
'''

books_file = 'books.json'                   #here is defined filename where our records are stored

#function to check if file is empty
def check_file():
    if os.stat(books_file).st_size == 0:        #if json is empty, add empty list to it 
            with open(books_file, 'w') as file:
                json.dump([], file)

#function for reading books from the file
def read_books():
    check_file()
    with open(books_file, 'r') as file:
        return json.load(file)               
    

#function for saving books to the file
def save_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


#function for adding book record to the file
def add_book(name,author):
    books = read_books()
    books.append({'name': name, 'author': author, 'read': False})
    save_books(books)


#function for marking book as read in the file
def mark_book_read(name):
    books = read_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    save_books(books)



#function for removing book record from the file
def delete_book(name):
    books = read_books()
    books = [book for book in books if book['name'] != name]
    save_books(books)
   

