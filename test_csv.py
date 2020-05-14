import csv

movies=[
    {'name':'The Matrix','director':'Wachowski'},
    {'name':'Green Book','director':'Farelly'},
    {'name':'Amadeus','director':'Forman'}

]
'''
def write_to_file(output):
    with open('csv_file.csv','w') as f:
        writer=csv.writer(f)
        f.write('name,director\n')
        writer.writerows([elem.values() for elem in output])


def read_from_file():
    with open('csv_file.csv','r') as f:
        reader=csv.reader(f)
        for line in reader:
            print(f'Name: {line[0]}\tDirector: {line[1]}')


read_from_file()
write_to_file(movies)
'''
'''
below is the same with DictReader/DictWriter function
'''
def write_to_file(output):
    with open('csv_file.csv','w') as f:
        writer=csv.DictWriter(f, fieldnames=['name','director'])
        writer.writeheader()
        writer.writerows(output)


def read_from_file():
    with open('csv_file.csv','r') as f:
        reader=csv.DictReader(f)
        for line in reader:
            print(f'Name: {line["name"]}\t\tDirector: {line["director"]}')
        #if you want it returned to the list:
        return list(reader) #returns an ordered list of dictionaries

read_from_file()