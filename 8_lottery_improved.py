import random

# This line creates a set with 6 random numbers
# Note: original solution suggests (range(22), 6) - I changed it so that 0 is not included

lottery_numbers = set(random.sample(range(1,22), 6))
print(f'Lottery numbers are: {lottery_numbers}')

# Here are your players; find out who has the most numbers matching lottery_numbers!

players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

#Make first player the winner for the start
top_player = players[0]
#Number of guessed numbers (0 for the start)
max_guessed_numbers = 0

for player in players:
    guessed_numbers = len(lottery_numbers.intersection(player['numbers']))  #checking how many numbers from player are in lottery numbers 
    if guessed_numbers > max_guessed_numbers:
        top_player = player                         #this is our new top player
        max_guessed_numbers = guessed_numbers       #don't forget to change number of guessed numbers to new value here

winnings = 100 ** max_guessed_numbers
#winning is 100 USD to the potency of guessed numbers

#if you want it make it clear:
print('{} got {} numbers right'.format(top_player['name'] , max_guessed_numbers ))


print (f'{top_player.get('name')} got {max_guessed_numbers} right')


# Then print out—here in Udemy we have to use .format, but normally you'd want to use f-strings.

print (f'Player {top_player.get('name')} got {winnings} right')
