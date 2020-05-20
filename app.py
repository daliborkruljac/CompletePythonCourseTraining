import sys
from utils.common import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 's' save your list of all books
- 'q' to quit

Your choice:"""

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == "a":
            add_book()
        elif user_input == "l":
            listbooks()             
        elif user_input == "r":
            readbook()
        else user_input == "d":
            deletebook()
        else user_input == "s":
            save_books_list()
        else:
            print('Unknown command. Please try again.')
            MenuPrompt()
    if user_input == 'q':
        print ('Ok, quitting the app')
        exit()                        #This is so that our app stops on 'q' and does not go in MenuPrompt again (import sys was required for this command)



# def prompt_add_book()     ask for book name
# def prompt_list_books()   show all the books
# def prompt_read_book()    ask for book name and change it to "read" in our list
# def prompt_delete_book()  ask for book name and remove book from the list
# def save_books_list()     bonus points: save books list to a file
# for extra bonus, autosave list on every change (add save function cls to each function)