# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:


# Output should look like:
# [{"club": "Manchester United", "country": "UK", "city": "Manchester"}, {"club":  ... ""}]

import csv
import json

#function for returning dictionary from 
def read_from_csv():
    with open('csv_file.txt','r') as f:  #it's not a dictionary so I need to load
        reader=csv.DictReader(f, fieldnames=['club','city','country'])
        csv_list = []
        for line in reader:
            csv_list.append(line)
        return csv_list

#function for writing data to json file
#def write_to_json():
def write_to_json():
    file = open('json_file.txt','w')
    json.dump(read_from_csv(), file)
    file.close()

read_from_csv()
write_to_json()


