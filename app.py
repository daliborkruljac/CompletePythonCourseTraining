import sys
from utils.common import database

#multiline string defined here
USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 's' save your list of all books
- 'q' to quit

Your choice: """                            #space added after question

#function for user menu input
def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':                        #go through the loop if q is not pressed:
        if user_input == "a":
            prompt_add_book()
        elif user_input == "l":
            list_books()             
        elif user_input == "r":
            prompt_read_book()
        elif user_input == "d":
            prompt_delete_book()
        else:
            print('Unknown command. Please try again.')
            menu()
    if user_input == 'q':                       #q is pressed - print a message and exit
        print ('Ok, quitting the app')
        exit()                                  #this is so that our app stops on 'q' and does not go in MenuPrompt again (import sys was required for this command)  


#function for reading books
def list_books():
    books = database.read_books()
    print('\nList of your books: \n')
    for book in books:
            print (f"\n{book['name']} by {book['author']} - Book read: {read}")
    menu()

#function for adding books
def prompt_add_book():                 
    name = input("Book name: ")
    author = input("Author: ")
    database.add_book(name, author)
    print (f'\nBook {name} by {author} added to your list\n')
    menu()                         #When done adding book, go back to menu
                              

def prompt_read_book():
    name = input('Enter book name: ')
    database.mark_book_read(name)
    print(f'Book {name} marked as read')
    menu()

def prompt_delete_book():
    name = input('Enter book name: ')
    database.delete_book(name)
    print(f'\nBook {name} deleted\n')
    menu()

books = database.read_books()                   #load books
menu()   