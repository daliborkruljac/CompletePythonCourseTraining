# Incomplete app!
# Define movies as a list:
# Save movies to text file later (version 2, use dataabase in version 3)
movies = []
selection = ''

#function for Menu Prompt
def MenuPrompt():  
    MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            MovieInput()
        elif selection == "l":
            MovieList()             
        elif selection == "f":
            MovieFind()
        else:
            print('Unknown command. Please try again.')


# function for Movie Input
def MovieInput ():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })
    selection == ''             #change selection to avoid infinite loop

# function for Movie Listing
def MovieList():
    pass

# function for Movie Finding
def MovieFind():
    pass

MenuPrompt()


# Remember to run the user menu function at the end!