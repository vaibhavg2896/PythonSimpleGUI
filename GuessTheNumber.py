##########################################################
#01:12 PM
#Thursday, June 26, 2016 (GMT+5:30) 
#@ author : VAIBHAV GUPTA(15454) 

########################################################## template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
secret_number=0;counter=7;hrng=100
# helper function to start and restart the game
def new_game(lst):
    print ""
    global hrng
    hrng=lst
    # initialize global variables used in your code here
    print 'new game,Range is from 0 to',hrng
    global secret_number,counter
    secret_number=random.randrange(0,hrng)
    if hrng==100:
         counter=7 
    else:counter=10
    print 'Number of remaining guesses is',counter    
    


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    new_game(100)
    global counter
    counter=7
    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    new_game(1000)
    global counter
    counter=10
    
    
    
def input_guess(guess):
    # main game logic goes here
    global secret_number,counter
    print ""
    counter-=1
    num=int(guess)
    if counter>=0:
        print 'Guess was',guess
    
        print 'Number of remaining guesses is',counter
    
    
 
        if num<secret_number:
            print 'Lower!'
        elif num>secret_number:
            print 'Higher!'
        else: 
            print 'Correct!'
    if counter==0:
        print 'You ran out of guesses.',
        print 'The number was',secret_number
        print ""
        new_game(hrng)
# create frame

frame=simplegui.create_frame('Guess The Number',200,200)
frame.start()
frame.add_button('Range is [0,100)',range100,200)
frame.add_button('Range is [0,1000)',range1000,200)
frame.add_input('Enter guess',input_guess,100)
# register event handlers for control elements and start frame


# call new_game 
new_game(100)


# always remember to check your completed program against the grading rubric
