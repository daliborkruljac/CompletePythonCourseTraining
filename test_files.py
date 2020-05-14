#Ask the user for a list of 3 friends
#For each friend, we'll tell the user whether they are nearby
#For each nearby friend, we'll save their name to 'nearby_friends.txt'

#hint: readlines()

print ('Please enter 3 friends:')
myfriend1 = input ('Please enter 1st friend name: ')
myfriend2 = input ('Please enter 2nd friend name: ')
myfriend3 = input ('Please enter 3rd friend name: ')

myfriendslist = [myfriend1,myfriend2,myfriend3]
myfriendsset = set(myfriendslist)
print (myfriendsset)  #to be removed


peoplefile = open('people.txt','r')
peoplelist = [line.strip() for line in peoplefile.readlines()]      #I lost hours on this syntax
peoplefile.close()


peopleset = set(peoplelist)    
print(peopleset)    #to be removed

friendsnearbyset = myfriendsset.intersection(peopleset)
print(friendsnearbyset)#to be removed

friendsnearbyfile = open('nearby_friends.txt','w')

for friend in friendsnearbyset:
    friendsnearbyfile.write(f'{friend}\n')

