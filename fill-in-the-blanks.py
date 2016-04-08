## Quizes and answers - inputs
easy_quiz =     """Fill in the missing terms:\n 
    Here are some of the most common string methods: s.  ___1___ ( ), s.upper() -- returns the lowercase or uppercase version of the string. \n 
    s.  ___2___  () -- returns a string with whitespace removed from the start and end \n 
    s.   ___3___   ('other'), s.endswith('other') -- tests if the string starts or ends with the given other string \n 
    s.  ___4___  ('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -one if not found \n 
    s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'\n 
    s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars..\n"""
                
easy_answers =  ['lower', 'strip', 'startswith', 'find']

medium_quiz =   '''Medium level: Fill in the missing terms:\n  It is the most useful container ever: the dictionary. \n Python calls them " ___1___ ." Other languages call them hashes. \n    Dictionaries are another example of a data structure, and like lists they are one of the most commonly used data structures in programming. A dictionary is used to  ___2___  or associate things you want to store to   ___3___   you need to get them. The contents of a dict can be written as a series of key:value pairs within  ___4___  braces { }.\n'''
                        
medium_answers = ['dict', 'map', 'keys', 'curly']
        
hard_quiz =     '''Hard level. Fill in the missing terms:\n The power of regular  ___1___  is that they can specify patterns, not just fixed  ___2___ . Here are the most basic patterns which match single chars: \n .(a period) -- matches any single character except newline '\n' \w -- (lowercase w) matches a "  ___3___  " character: a letter or digit or underbar [a-zA-Z0-9_]. Note that although "word" is the mnemonic for this, it only matches a single word char, not a whole word. \W (upper case W) matches any non-word character.  ___4___  = start, $ = end -- match the start or end of the string.\n''' 
                
hard_answers =  ['expressions', 'characters', 'word', '^']

## Return quiz upon difficulty level, input: difficulty level
## output: the appropriate quiz
def get_quiz(level):
    if level == "easy":
        return easy_quiz, easy_answers
    if level == "medium":
        return medium_quiz, medium_answers
    if level == "hard":
        return hard_quiz, hard_answers

## Behavior: creates list of placeholders Input: difficulty level and list of answers, OUTPUT: list of placeholders as found in the quiz text
def prep_palceholders(level, answers):
    placeholders_nbr= list(range(1, len(answers)+1))
    placeholders_nbr = [str(x) for x in placeholders_nbr]
    placeholders = ["___" + x + "___" for x in placeholders_nbr]
    return placeholders 


##Input quiz, word that is currently iterated, user_guess. Behavior: replaces placeholder/word with user guess. Output: quiz as a list.
def replace_userguess(quiz, word, user_guess):
    loc = quiz.index(word)
    quiz.remove(word)
    quiz.insert(loc, user_guess)
    return quiz

##Behavior: validates user input by comparing to answers, does this for a set number of times. OUTPUT: returns user_guess and the index to jump to next answer
def validate_userguess(user_guess, answers, index, nbr_games):
    if user_guess == answers[index]:
        print "You are right:__", user_guess, "__ is the correct answer!\n"
        return user_guess
    else:
        if nbr_games == 1:
            print "You didn't guessed correctly. The correct_answer was:___", answers[index],"__!\n"
            exit()    
        else:
            print '\nTry again. You still got', nbr_games-1, 'time(s) left!\n'         
            return None

## Behavior: iterates through the quiz[], compares if current word is in the placeholders[], asks for user input for question. OUTPUT
## returns the quiz as a []
def write_game(quiz, placeholders, user_nbr_games, answers):
    index = 0
    for word in quiz:
        if word in placeholders: 
            nbr_games = user_nbr_games
            while nbr_games > 0:
                user_guess = raw_input("Type in your guess for __" + word +"__!     \n")
                answer = validate_userguess(user_guess, answers, index, nbr_games)
                if answer != None: #correct answer next placeholder
                    replace_userguess(quiz, word, answer)
                    index = index +1
                    break
                elif answer == None:
                    nbr_games = nbr_games-1
                    
    return quiz 

##Behavior: runs the game. Asks for user input on difficulty level, and number of guesses. OUTPUT: if guesses are correct: quiz with answers filled in.
def play_game():
    print "\nHello! Let's play a Python quiz. "
    difficulty_level= raw_input("Which level do you want to play? Enter: easy OR medium OR hard\n")
    user_nbr_games = int(raw_input("How many times do you want to guess?   \n"))
    
    quiz, answers = get_quiz(difficulty_level)
     
    placeholders = prep_palceholders(difficulty_level, answers)
    print quiz
    print placeholders
    print "Cheat-mode on: Anwsers are:", answers ##Comment on == Cheat mode off, Comment off == Cheat mode on
    quiz = quiz.split() # quiz in a []
    write_game(quiz, placeholders, user_nbr_games, answers)
    quiz = " ".join(quiz) 
    print quiz 

play_game()