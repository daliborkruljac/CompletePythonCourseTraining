
# Define a PrimeGenerator class
class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop                            # stop defines the range (exclusive upper bound) in which we search for the primes
        self.start = 2                              # start defines first number to work with
    
    def __next__(self):                             #always search from current start (inclusive) to stop (exclusive)
        n = self.start
        for x in range(2, self.stop):
            for n in range (self.start, self.stop):
                for x in range (2, n):
                    if n % x == 0:                  #not prime
                        break
            else:                                   #n is prime, because we've gone through the entire loop without having a non-prime situation
                self.start = n + 1                  #next time we need to start from n + 1, otherwise we will be trapped on n
                return n                            #return n for this round
        raise (StopIteration)                       #this is what tells Python we've reached the end of the generator

'''
#need to define __iter__ to return itself like any iterable function (don't know how)


    def __iter__(self):
        return self




#TEST
#Please don't go much over 10000

g = PrimeGenerator(77)
print(list(g))

'''


