# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".


for x in range (1, 101):
    if x%15 == 0:
        print ('FizzBuzz')
    elif x%3 == 0 :
        print ('Fizz')
    elif x%5 == 0 :
        print ('Buzz')
    else:
        print(x)
