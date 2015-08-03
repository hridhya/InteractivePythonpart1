import simplegui
import random
import math

num_range = 100
secret_num = 0
guesses_left = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global num_range
    global guesses_left
    secret_number = random.randrange(0,num_range)
    
    if num_range == 100:
        guesses_left = 7
    elif num_range == 1000:
        guesses_left = 10
        
    print "New game. The range is from 0 to", num_range
    print "Number of guesses remaining == ", guesses_left
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
    
def input_guess(guess):

    
    global guesses_left
    global secret_num 
    guess_number = int(guess)
    
    won = False
    
    print "Guess was",guess_number
    guesses_left = guesses_left - 1
    print "Number of remaining guesses is ", guesses_left
    
    if guess_number == secret_num:       
        won = True
    elif guess_number > secret_num:
        result = "Lower!"
    else:
        result = "Higher!"                
        
        
    if won:
        print "Correct"
        new_game()
        return
    
    elif guesses_left == 0:
        print "Game over!"   
        new_game()
        return
    
    else:
        print result
    
# create frame
frame = simplegui.create_frame("Guess the Number", 300, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 100)
frame.add_button("Range is [0,1000)", range1000, 100)
frame.add_input("Input_guess", input_guess, 100)

frame.start()

# call new_game 
new_game()
