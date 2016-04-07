## Quizes and answers - inputs
easy_quiz =     '''Fill in the missing terms:\n Here are some of the most common string methods: s.__1__(), s.upper() -- returns the lowercase or uppercase version of the string. \n s.___2___() -- returns a string with whitespace removed from the start and end \n s.___3___('other'), s.endswith('other') -- tests if the string starts or ends with the given other string \n s.___4___('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -one if not found \n s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'\n s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars..\n''' 
                
easy_answers =  ['lower', 'strip', 'startswith', 'find']

medium_quiz =   '''Medium level: Fill in the missing terms:\n  It is the most useful container ever: the dictionary. \n Python calls them "___1___." Other languages call them hashes. \n    Dictionaries are another example of a data structure, and like lists they are one of the most commonly used data structures in programming. A dictionary is used to ___2___ or associate things you want to store to ___3___ you need to get them. The contents of a dict can be written as a series of key:value pairs within ___4___ braces { }.\n'''
                        
medium_answers = ['dict', 'map', 'keys', 'curly']
        
hard_quiz =     '''Hard level. Fill in the missing terms:\n The power of regular ___1___ is that they can specify patterns, not just fixed ___2___. Here are the most basic patterns which match single chars: \n .(a period) -- matches any single character except newline '\n' \w -- (lowercase w) matches a "___3___" character: a letter or digit or underbar [a-zA-Z0-9_]. Note that although "word" is the mnemonic for this, it only matches a single word char, not a whole word. \W (upper case W) matches any non-word character. ___4___ = start, $ = end -- match the start or end of the string.\n''' 
                
hard_answers =  ['expressions', 'characters', 'word', '^']

#Convert text into list 
def prep_text(quiz):
    quiz=quiz.split()
    return quiz

# Input: level Behavoir: Create list of placeholders; Output list of placeholders (1-number of placeholders)
def prep_palceholders(level):
    placeholders= list(range(1, len(get_answers(level))+1))
    placeholders = [str(x) for x in placeholders]
    return placeholders    

## Return quiz upon difficulty level, input: difficulty level
## output: the appropriate quiz
def get_quiz(level):
    if level == "easy":
        return easy_quiz
    if level == "medium":
        return medium_quiz
    if level == "hard":
        return hard_quiz

## Return correct answers upon difficulty level, input: difficulty level, output: the matching answers
def get_answers(level):
    if level == "easy":
        return easy_answers
    if level == "medium":
        return medium_answers
    if level == "hard":
        return hard_answers


## Checks if a word/letter in placeholders is a substring of the word/letter passed in.
def word_in_placeholders(word,placeholders):
    for i in placeholders:
        if i in word:
            return i
    return None

<<<<<<< HEAD
## Input: nbr of games, replacements, correct answer, and quiz with replacements so far. Behavior: asks for user input, compares user input with correct answer, returns correct/not correct. Output: quiz with user answers (Correct or wrong "XXX") iso the replacement numbers.
def validate_answers(nbr_games,replacement, correct_answer, replaced_quiz):
    while nbr_games >0:
        user_guess =  raw_input("Type in your guess for __" + replacement +"__!     \n")
        nbr_games = nbr_games-1
        
        if user_guess == correct_answer:
                print "You are right:__", user_guess, "__ is the correct answer!"
                word = user_guess.replace(replacement, user_guess)
                replaced_quiz.append(word)
                break
        else:
            if nbr_games == 0:
                print "You didn't guessed correctly. The correct_answer was:___", correct_answer,"__!\n"
                word = "XXXXXX".replace(replacement, user_guess)

                replaced_quiz.append(word)
                #break ## If I wanted to break the for loop to stop the game, how would I need to do that??
            else:
                print '\nTry again. You still got', nbr_games, 'time(s) left!\n'            

    return replaced_quiz


## Input quiz, placeholders, answers, nbr_games. Behavior: iterates over quiz text to identify placeholders; calls correct answer based on index and takes the user input (if correct with answer, if not XXX) for every placeholder in the quiz; rest of text is filled with words out of original text. Output: complete quiz text with correct answers/placeholders XXXX
def write_quiz(quiz, placeholders, answers, nbr_games):
    replaced_quiz=[]
    for word in quiz:
        replacement = word_in_placeholders(word, placeholders)
        if replacement != None:
            # link placeholder to correct answer
            correct_answer = answers[int(replacement)-1]
            
            validate_answers(nbr_games,replacement, correct_answer, replaced_quiz)   ##outputs the word XXX or correct one
                     
        else:
            replaced_quiz.append(word)
    replaced_quiz = "".join(replaced_quiz)
    return replaced_quiz

##Behavior: starts the game, asks for user input on difficulty level, runs the game. Output: completed quiz
=======

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



>>>>>>> 24730f54fc485c9da7daed94098a1526efa71b14
def play_game():
       
    print "\nHello! Let's play a Python quiz together. "
    difficulty_level= raw_input("Which level do you want to play? Enter: easy OR medium OR hard\n")
    nbr_games = int(raw_input("How many times do you want to guess?   \n"))
    quiz = get_quiz(difficulty_level)
    
    prep_text(quiz)
    
    answers=get_answers(difficulty_level)
    
    placeholders = prep_palceholders(difficulty_level)

    print quiz
<<<<<<< HEAD
    #print answers ##uncomment if you'd like to cheat
    print write_quiz(quiz, placeholders, answers, nbr_games)

=======
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
>>>>>>> 24730f54fc485c9da7daed94098a1526efa71b14
play_game()
