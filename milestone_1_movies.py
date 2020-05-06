import sys                              #Needed for exit program function

# Define movies as a list:
# Save movies to text file later in version 2, use dataabase in version 3
movies = []                             #Define Movies as a list
MENU_PROMPT = ''                        #Not needed really, just to satisfy debugger

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
            MenuPrompt()
    if selection == 'q':
        print ('Ok, quitting the app')
        exit()                        #This is so that our app stops on 'q' and does not go in MenuPrompt again (import sys required)


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
    MenuPrompt()


# function for Movie Listing
def MovieList():
    print("This is your movie list:\n")
    for movie in movies:
        print('Title: ' + movie['title'])
        print('Director:' + movie['director'])
        print('Year: ' + movie['year'])
        print('\n')                         #line break after one movie listed
    MenuPrompt()                            #After listing movies go back to MenuPrompt  (otherwise app will list movies all the time#


# function for Movie Finding
def MovieFind():
    pass


MenuPrompt()                               #MenuPrompt - all actions decided based on this input

