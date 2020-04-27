lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""
players = [
    {
        'name': 'Dejan',
        'numbers' : {3,8,12,21,29}
    },
    {
        'name': 'Danijel',
        'numbers' : {5,9,12,21,22}
    }
]

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers. We still cannot use f-strings in this exercise.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""

name = players[0]['name']
numbers = players[0]['numbers'].intersection(lottery_numbers)
print('Player {name} got {amount} numbers right.'.format(name=name, amount=len(numbers)))
 
name = players[1]['name']
numbers = players[1]['numbers'].intersection(lottery_numbers)
print('Player {name} got {amount} numbers right.'.format(name=name, amount=len(numbers)))
