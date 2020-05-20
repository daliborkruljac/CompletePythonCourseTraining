books = []

with open('books_list.txt','w') as f:
    for line in books:
        f.write('%s\n' % line)
    print("List saved.")
