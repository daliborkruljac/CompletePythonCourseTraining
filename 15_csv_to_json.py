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

def csv_to_json():
    with open('csv_file.txt','r') as f:
        reader=csv.DictReader(f, fieldnames=['club','city','country'])
        csv_list = []
        for line in reader:
            csv_list.append(line)
    with open('json_file.txt','w') as f:
        json.dump(csv_list, f)
    
csv_to_json()




