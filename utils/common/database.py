'''
Concerned with storing and retreiving books from a list
'''

books = []

def add_book(name,author):
    books.apend({'name':name, 'author':author, 'read':False})


#define all the functions
def list_books():
    print(f'')

def read_book(name):
    pass


def delete_book(name):
    book = [book for book in books if book['name'] != name]

def save_books_list():
    with open('books_list.txt','w') as f:
        f.write(books)

