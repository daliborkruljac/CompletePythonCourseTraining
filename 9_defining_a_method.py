# We've already defined a movie class like this:
class MovieListing:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director

    # let's try to add a method `print_info()` here:
    def print_info(self):
        print(f'<<{self.name}>> by {self.director}')

# You only need to finish the method, we will take care of the object creation and call your method for you!

# Code below is not needed in the taks

my_movie = MovieListing ('The Matrix', 'Wachowski')

MovieListing.print_info(my_movie)



