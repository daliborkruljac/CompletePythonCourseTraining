import sys                              #Needed for exit program function

#Version 1
# Save movies to text file later in version 2, use dataabase in version 3
#Version 4 - add smarter menu input (accepp Add, add, a and ADD for input for example)
movies = []                             #Define Movies as a list (dictionary key value pairs are inside this list)
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
        exit()                        #This is so that our app stops on 'q' and does not go in MenuPrompt again (import sys was required for this command)


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
    MenuPrompt()                            #After movie input go back to MenuPrompt to ask user what to do next


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
    titleentered = input('Enter title: ')
    print('These movies fit your search parameters: \n')
    moviefound = 0                              #First we define there are no movies with that name in the list
    for movie in movies:
        if titleentered == movie['title']:
            print('Title: ' + movie['title'])
            print('Director:' + movie['director'])
            print('Year: ' + movie['year'])
            print('\n')                         #line break after one movie is listed
            moviefound = 1                      #movie with that name is found so we will not print next statement 
    if moviefound == 0:
        print('No movie found with that title.')
    MenuPrompt()                                #after lisiting found movies, go to MenuPrompt


MenuPrompt()                               #MenuPrompt - all actions decided based on this input

