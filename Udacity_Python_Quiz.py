#Defining the 3 different quizzes and corresponding answers.

easy_quiz = "The Ford __1__ was an iconic Muscle Car first introduced in __2__. The Mustang has gone through numerous iterations over it's lifetime. Most recently Ford relaunched the __3__ model which sports a 5.2L V8 producing __4__ Horsepower making it the most powerful naturally aspirated Ford production engine ever."
medium_quiz = "The Mustang has appeared in several movies which contributed to it's legacy. One such movie was Gone in 60 Seconds airing in 2000. In the movie the car is called __1__ and represented a __2__ Mustang. The Mustang also replaced the rival Camaro in a remake of the classic TV Show __3__ which re-aired in 2008. The Mustang has also had a recurring role in the __4__ movies as the Decepticon Barricade."
hard_quiz = "While the first model of the Mustang was classified as 1965 it was actually introduced in __1__. In 2014 Ford released a special edition model to celebrate the __2__ year anniversary of the Mustang. The common engine configurations of the Mustang have included 6 and 8 cylinder variations. In recent model years Ford decided to replace the 6 cylinder with a smaller turbocharged __3__ cylinder. Along with the conversion to a 4 cylinder engine Ford also improved the output of the 8 cylinder variant to __4__ horsepower."
#Add second blank #1

easy_answers = ["mustang", "1965", "shelby gt350", "526"]
medium_answers = ["eleanor", "1967 gt500", "knight rider", "transformers"]
hard_answers = ["1964.5", "50", "4", "435"]

blanks = ["__1__", "__2__", "__3__", "__4__"]

#Returns the answers and quiz for the difficulty selected by the user.
#Inputs Raw Input 1-3 to determine difficulty.
#Outputs: Answers and Quiz.

def quiz_setup(level):
    if level == "1":
        print "You selected Easy."
        return easy_quiz, easy_answers

    elif level == "2":
        print "You selected Medium."
        return medium_quiz, medium_answers

    else: # For level 3.
        print "You selected Hard."
        return hard_quiz, hard_answers

def word_in_blanks(word, blanks):
    for blank in blanks:
        if blank in word:
            return blank
    return None

#This function takes a user input after it has been validated as correct, identifies the location in the quiz and inserts the word into the quiz.
#Outputs: Quiz with the blanks replaced with the correct answers.

def replace_blanks(quiz, blanks, answers):
    replaced, user_answer, index, quiz = [], "", 0, quiz.split()
    for word in quiz:
        replacement = word_in_blanks(word, blanks)
        if replacement != None:
            user_answer = raw_input("Enter your answer for: " + replacement + " ").lower()
            while user_answer != answers[index]:
                print "Your answer was wrong. Please try again."
                user_answer = raw_input("Type it here again: ").lower()
            
            print "That's right!"

            replaced.append(user_answer)
            blank_position = quiz.index(word)
            quiz[blank_position] = user_answer
            print " ".join(quiz)
            
            index += 1
            
        else:
           replaced.append(word)

    replaced = " ".join(replaced)
    return replaced

#This function is where the other functions are triggered. It uses user input to select the level and return the appropriate quiz and answers.
#It triggers the replace_blanks function which prints the question, takes the users answer and then replaces the blank with the users correct answer.
#This function also identifies if a user selects a difficulty that is not part of the level list.

def play():
    print "Welcome to the Ultimate Mustang Quiz"
    level = raw_input(" Easy - 1 | Medium - 2 | Hard - 3 | ")
    if level == "1" or level == "2" or level == "3":
        quiz, answers = quiz_setup(level)
        print quiz

        print replace_blanks(quiz, blanks, answers)

        print "Congratulations, you passed!"
    
    else:       
        print "That's not an acceptable difficulty. Please enter 1, 2 or 3. Game will now restart."
        play()

play()