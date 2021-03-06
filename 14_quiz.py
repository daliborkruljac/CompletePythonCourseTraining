"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:

guessed = 0
numberofquestions = 0
quiz = open('questions.txt', 'r')
            #each question is a str "1+1=2\n"

#solution below my code shows easier way to do it
for line in quiz:
    quizline = line.rstrip("\n")        #remove the line break at the end
    quizline = quizline.split('=')      #now our line is a list ['1+1','2']
    numberofquestions +=1            #counting number of questions
    #Let's show user first list member, then ask for second and compare second 
    useranswer = input (f'{quizline[0]}: ')
    if useranswer == quizline[1]:
        guessed += 1

print (f'You final score is {guessed}/{numberofquestions}.')
quiz.close()


#let's print to file also
results = open('results.txt','w+')
results.write (f'You final score is {guessed}/{numberofquestions}.')
results.close()


'''
#Proposed solution:

# read from questions.txt and append each line into a list
questions = open('questions.txt', 'r')  # read from questions.txt
question_list = [line.strip() for line in questions.readlines()]    # read all lines and get rid of line break for each line, then append each stripped line to a list
questions.close()
 
score = 0   # initialize score
total = len(question_list)      # set total score
 
for line in question_list:
    q, a = line.split('=')  # split equation with `=` into question and answer
    ans = input('{}='.format(q))    # print question and wait for user to input their answer
    if a == ans:    # if user input matches answer
        score += 1  # increase score
 
result = open('result.txt', 'w')    # open result.txt
result.write('Your final score is {}/{}.'.format(score, total))     # write final score to result.txt
result.close()

'''