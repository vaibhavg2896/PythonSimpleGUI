##########################################################
#07:10 PM
#Thursday, June 11, 2016 (GMT+5:30) 
#@ author : VAIBHAV GUPTA(15454) 

#########################################################



# Rock-paper-scissors-lizard-Spock template



import simplegui
# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name=="rock":
        return 0
    elif name=="Spock":
         return 1
    elif name=="paper":
          return 2
    elif name=="lizard":
         return 3
    elif name=="scissors":
          return 4
    else: 
        return None
    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number==0:
        return "rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    elif number==4:
        return "scissors"
    else: return None
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    import random
    # delete the following pass statement and fill in your code below
    
    
    # print a blank line to separate consecutive games
    print ""
    # print out the message for the player's choice
    print "Player chooses",player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number=name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number=random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice=number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses",comp_choice
    # compute difference of comp_number and player_number modulo five
    diff=(comp_number-player_number)%5
    # use if/elif/else to determine winner, print winner message
    if diff<=2 and diff>0:
        print "Computer wins!"
    elif diff<=4 and diff >2:
        print "Player wins!"
    else:print "Error"    
        
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE


# always remember to check your completed program against the grading rubric
frame=simplegui.create_frame('Game',300,300)
frame.start()
frame.add_label('"rock", "Spock", "paper", "lizard", "scissors"')
frame.add_input('Enter your choice',rpsls,100)
