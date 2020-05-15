import json

file = open('friends_json.txt','r')
filecontents = json.load(file)       #reads file and turns it to dictionary
file.close()

print (filecontents['friends'][0])
print (filecontents)

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

file = open('cars.txt','w')
json.dump(cars, file)
file.close()

