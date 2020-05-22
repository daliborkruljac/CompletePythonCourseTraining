'''
Concerned with storing and retreiving books from a list
'''

def read_books_list():
    books = []
    with open('books_list.txt','r') as f:
        for line in f:
            currentPlace = line[:-1]
            books.append(currentPlace)
    return books


def add_book(books, name,author):
    books.append({'name': name, 'author': author, 'read': False})
    print('Book added.\n')
    save_books_list(books)


def save_books_list(books):
    with open('books_list.txt','w') as f:
        for book in books:
            f.write('%s\n' % book)


def list_books(books):
    for book in books:
        dict.get


def read_book(books,name):        #go over list items and change read to True where name matches  #does not work (yet)
    books = read_books_list()
    for book in books:
        if book['name'] == name :
            book['read'] = True


def delete_book(name):
    books = read_books_list()
    book = [book for book in books if book['name'] != name]



