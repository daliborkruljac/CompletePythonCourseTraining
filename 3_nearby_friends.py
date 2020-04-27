nearby_people = {'Rolf', 'Jen', 'Anna'}

user_friends = set() 
#Empty curly braces {} will make an empty dictionary in Python. 
# To make a set without any elements we use the set() function without any argument.

# Ask the user for the name of a friend

friend = input ('Enter your friend name: ')

# Add the name to the empty set

user_friends.add(friend)


# Print out the intersection between both sets. This gives us a set with those friends that are nearby.

nearby_friends = user_friends.intersection(nearby_people)


if nearby_friends == set():
    print('No nearby friends')
else:
    print(''.join(nearby_friends) + ' is online')


