# - define a UncountableError that takes in wrong_value as the only argument
# - the UncountableError should inherit ValueError
# - the UncountableError should indicate an error message like this:
#    'Invalid value for n, WRONG_VALUE. n must be greater than 0.'
#    where WRONG_VALUE should be replaced by the given value in the argument
# define your UncountableError here:


class UncountableError (ValueError):
    """ 
    This is UncountableError which takes all data from parent (ValueError) and adds wrong value to new object called Uncountable error.
    It returns a message as we defined it below.
    """
    def __init__(self, wrong_value):
        super().__init__('Invalid value for n, {}. n must be greater than 0'.format(wrong_value))


# do not change anything in the count_from_zero_to_n() function
# you may expect your UncountableError work in the following way
def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)


# TESTING BELOW, try entering a string and error is generic, while if negative integer is entered, our error message is shown.

n = int(input('Enter n: '))
count_from_zero_to_n(n)

