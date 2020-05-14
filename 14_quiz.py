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

for line in quiz:
    quizline = line.rstrip("\n")        #remove the line break at the end
    quizline = quizline.split('=')      #now our line is a list ['1+1','2']
    numberofquestions +=1            #counting number of questions
    #Let's show user first list member, then ask for second and compare second 
    useranswer = input (f'{quizline[0]}: ')
    if useranswer == quizline[1]:
        guessed += 1

print (f'You final score is {guessed}/{numberofquestions}.')

#let's print to file also
results = open('results.txt','w+')
results.write (f'You final score is {guessed}/{numberofquestions}.')
results.close()

'''

'''