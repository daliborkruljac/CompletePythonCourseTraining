friends = ['Rolf', 'ruth','charlie','Jen']
guests = ['jose','Bob','Rolf','Charlie','michael']

present_friends = [
    name.title() for name in guests if name.title() in [f.title() for f in friends]
]
#don't do this usually as this makes code harder to read/understand

print(present_friends)
