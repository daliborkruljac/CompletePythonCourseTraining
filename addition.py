#The Addition module can do one simple task,
#adding two numbers.

class Addition:
    @classmethod
    def add(cls, num1, num2):
        return num1 + num2

'''
We can make use of it in our code like this:
    from addition import Addition

    result = Addition.add(100, 200) #use Addition.add method
'''