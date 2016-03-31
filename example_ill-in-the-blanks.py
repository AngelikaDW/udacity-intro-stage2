# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/


## Questions and answers - inputs
easy_quiz =     '''You have chosen level easy. Here is your text.Fill in the blanks.\n
                In Python we often write programs that need to make comparsions between values\n
                We can do comparsions with signs like < > in math and equality comparsions\n
                with ___ (not equal) and ___ (equal).\n
                These always return a Boolean value (which can be ___ or ___ )''' 
                
easy_answers =  ['!=', '==', 'True', 'False']

medium_quiz =   '''You have chosen level medium. Here is your text.,\n
                Fill in the blanks!\n
                Here are some definitons:\n
                We sometimes call numbers without a variable ___\n
                Programming is grounded in ___ so it is important to know how\n
                programming languages do simple math.\n
                ___ (also known as methods) take input and return an output.\n
                A ___ is used to map or associate things you want to store\n
                to keys you need to get them. We can implement one by using just that.''' 
                        
medium_answers = ['magic numbers', 'arithmetic', 'functions', 'False']
        
hard_quiz =     '''You have chosen hard level. Here is your text.,\nFill in the blanks! Python is called an ___ programming language. This means there is a construct in Python called a class. It is usefule as a ___.\nIn Python, a class can implement certain operations that are invoked by ___(such as arithmetic operations or  ___ and slicing)''' 
                
hard_answers =  ['object-oriented', 'modeling tool', 'special syntax', 'subscripting']

## Code (Logic)

## behavior: return quiz and its answers upon difficulty level, input: the quizes and
## the matching answers, output: the appropriate quiz
def get_quiz(level):
    if level == "easy":
        return easy_quiz
    if level == "medium":
        return medium_quiz
    if level == "hard":
        return hard_quiz
    
## Return the correct answer list 
def get_answers(level):
    if level == "easy":
        return easy_answers
    if level == "medium":
        return medium_answers
    if level == "hard":
        return hard_answers
    
## behavior: this function evaluates the answers, inputs are: the user answers, the right
## quiz answers, output: C
def evaluate_answers(user_answers, quiz_answers):
    if user_answers == quiz_answers:
        return "Correct. Congratulations! You have successfully completed the quiz!"
    else:
        return "Incorrect. Please try again."

##Run a game
def game():
    print "Hello. This is a quiz."
    ## Ask for the game level. (User input)
    difficulty_level = raw_input ("Choose your difficulty level(easy, medium, hard):")
    ## Load quiz depending on user input.
    quiz = get_quiz (difficulty_level)
    print quiz
    ## Ask for the answers (User input)
    user_answers = []
    for i in range(1,5):
        answer = raw_input("Answer blank " + str(i) + ":")
        user_answers.append(answer)
        print user_answers
    quiz_answers = get_answers(difficulty_level)
    result = evaluate_answers(user_answers, quiz_answers)  
    print result

## run game
game()

