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

## Quizes and answers - inputs
easy_quiz =     '''Fill in the missing terms:\n Here are some of the most common string methods: s.__1__(), s.upper() -- returns the lowercase or uppercase version of the string. \n s.___2___() -- returns a string with whitespace removed from the start and end \n s.___3___('other'), s.endswith('other') -- tests if the string starts or ends with the given other string \n s.___4___('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -one if not found \n s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'\n s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars..\n''' 
                
easy_answers =  ['lower', 'strip', 'startswith', 'find']

medium_quiz =   '''Medium level: Fill in the missing terms:\n Python's efficient key/value hash table structure is called a "___1___". The contents of a ___1___ can be written as a series of ___2___:___3___ pairs within ___4___ braces { }, e.g. dict = {key1:value1, key2:value2, ... }. The "empty dict" is just an empty pair of ___4___ braces {}.\n'''
                        
medium_answers = ['dict', 'key', 'value', 'curly']
        
hard_quiz =     '''Hard level. Fill in the missing terms:\n The power of regular ___1___ is that they can specify patterns, not just fixed ___2___. Here are the most basic patterns which match single chars: \n .(a period) -- matches any single character except newline '\n' \w -- (lowercase w) matches a "___3___" character: a letter or digit or underbar [a-zA-Z0-9_]. Note that although "word" is the mnemonic for this, it only matches a single word char, not a whole word. \W (upper case W) matches any non-word character. ___4___ = start, $ = end -- match the start or end of the string.\n''' 
                
hard_answers =  ['expressions', 'characters', 'word', '^']

#Convert text into list and remove duplicates from the list so that the user is not asked multiple time for input for one replacement 
def prep_text(quiz):
    quiz_multiple=quiz.split()
    [quiz.append(item) for item in quiz_multiple if item not in quiz]
    return quiz

#and create list of placeholders
def prep_palceholders(level):
    placeholders= list(range(1, len(get_answers(level))+1))
    placeholders = [str(x) for x in placeholders]
    return placeholders    

## Return quiz and its answers upon difficulty level, input: the quizes and
## the matching answers, output: the appropriate quiz
def get_quiz(level):
    if level == "easy":
        return easy_quiz
    if level == "medium":
        return medium_quiz
    if level == "hard":
        return hard_quiz

## get the correct answer list
def get_answers(level):
    if level == "easy":
        return easy_answers
    if level == "medium":
        return medium_answers
    if level == "hard":
        return hard_answers


# Checks if a word/letter in placeholders is a substring of the word/letter passed in.
def word_in_placeholders(word,placeholders):
    for i in placeholders:
        if i in word:
            return i
    return None


def validate_answers(quiz, placeholders, answers, nbr_games):
    replaced_quiz=[]
    user_answers =[]
    for word in quiz:
        replacement = word_in_placeholders(word, placeholders)
        if replacement != None:
            #print replacement
        # link placeholder to correct answer
            correct_answer = answers[int(replacement)-1]
            #print correct_answer - ##uncomment for cheating
        #Loop through the placeholders, ask for user input and check if correct. Display message.    
            while nbr_games >0:
                user_guess =  raw_input("Type in your guess for __" + replacement +"__!     \n")
                if user_guess == correct_answer:
                    user_answers.append(user_guess)
                    print "Congratulations. The correct answer was indeed:__", correct_answer,"__!\n"
                    word = word.replace(replacement, user_guess)
                    replaced_quiz.append(word)
                    #print replaced_quiz
                    break                 
                else:
                    if nbr_games == 1:
                        replaced_quiz.append(word)
                        print "You didn't guessed correctly. The correct_answer was:___", correct_answer,"__ Start another game!\n"
                    else:             
                        print '\nTry again. You still got:', nbr_games-1, 'times left!\n'
                nbr_games = nbr_games - 1
            replaced_quiz= " ".join(replaced_quiz)
            return replaced_quiz



def play_game():
    user_answers=[]
    
    print "\nHello! Let's play a Python quiz together. "
    difficulty_level= raw_input("Which level do you want to play? Enter: easy OR medium OR hard\n")
    nbr_games = int(raw_input("How many times do you want to guess?   \n"))
    quiz = get_quiz(difficulty_level)
    
    prep_text(quiz)
    
    answers=get_answers(difficulty_level)
    
    placeholders = prep_palceholders(difficulty_level)

    print quiz
    print answers
    print validate_answers(quiz, placeholders, answers, nbr_games)
"""
    for word in quiz:
        replacement = word_in_placeholders(word, placeholders)
        if replacement != None:
            #print replacement
        # link placeholder to correct answer
            correct_answer = answers[int(replacement)-1]
            #print correct_answer - ##uncomment for cheating
        #Loop through the placeholders, ask for user input and check if correct. Display message.    
            while nbr_games >0:
                user_guess =  raw_input("Type in your guess for __" + replacement +"__!     \n")
                if user_guess == correct_answer:
                    user_answers.append(user_guess)
                    print "Congratulations. The correct answer was indeed:__", correct_answer,"__!\n"
                    break                 
                else:
                    if nbr_games == 1:
                        print "You didn't guessed correctly. The correct_answer was:___", correct_answer,"__ Start another game!\n"
                    else:             
                        print '\nTry again. You still got:', nbr_games-1, 'times left!\n'
                nbr_games = nbr_games - 1
"""
play_game()
