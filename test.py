friends = ['Rolf', 'ruth','charlie','Jen']
guests = ['jose','Bob','Rolf','Charlie','michael']

present_friends = [
    name.title() for name in guests if name.title() in [f.title() for f in friends]
]

print(present_friends)
