'''
Concerned with storing and retreiving books from a list
'''

books= []
with open('books_list.txt','r') as f:
    for line in f:
        currentPlace = line[:-1]
        books.append(currentPlace)


def read_books_list():
    books = []
    with open('books_list.txt','r') as f:
        for line in f:
            currentPlace = line[:-1]
            books.append(currentPlace)
    return books


def add_book(name,author):
    books.append({'name':name, 'author':author, 'read':False})
    print('Book added.\n')
    save_books_list()


def read_book(name):
    pass

#define all the functions
def list_books():
    print(f'')


def delete_book(name):
    book = [book for book in books if book['name'] != name]

def save_books_list():
    with open('books_list.txt','w') as f:
        for line in books:
            f.write('%s\n' % line)


