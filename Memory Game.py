##########################################################
#11:12 AM
#Thursday, July 06, 2016 (GMT+5:30) 
#@ author : VAIBHAV GUPTA(15454) 

#########################################################

# implementation of card game - Memory

import simplegui
import random
cards=[]
exposed=[]
card_pos=[]
state=0
pair=[]
turns=0

# helper function to initialize globals
def new_game():
    
    global cards, exposed, turns,pair,card_pos,state, turns
    turns=0
    pair=[]
    exposed=[]
    cards=[]
    card_pos=[]
    label.set_text('Turns = 0')
    for i in range(0,16) :  
        exposed.append(False)
    for l in range(0,8): 
        cards.append(l)
    for l in range(0,8): 
        cards.append(l)    
    random.shuffle(cards)
    state=0
      
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed,card_pos,cards, state, pair, turns
    
    pos_lst=list(pos)
    for i in range(len(cards)):
        if state==0:
            if card_pos[i]<pos_lst[0]<card_pos[i+1]:
                exposed[i]=True
                state=1
                pair.append(i)
                break
        if state==1 :
            if card_pos[i]<pos_lst[0]<card_pos[i+1]:
                exposed[i]=True
                state=2
                pair.append(i)
                break
        if state==2:
            if card_pos[i]<pos_lst[0]<card_pos[i+1]:
                exposed[i]=True
                pair.append(i)
                if cards[pair[0]]!=cards[pair[1]]:
                    exposed[pair[0]]=False
                    exposed[pair[1]]=False
                    state=1
                    pair.pop(0)
                    pair.pop(0)
                    turns+=1
                    label.set_text('Turns = '+str(turns))
                    break
                else:
                    turns+=1
                    pair.pop(0)
                    pair.pop(0)
                    label.set_text('Turns = '+str(turns))
                    state=1
                    break
                
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards, exposed, card_pos
    for i in range(0,17):
        card_pos.append(50*i)
        
    for card_index in range(len(cards)):
         canvas.draw_text(str(cards[card_index]), [card_pos[card_index],65],64,'white','sans-serif')     
         if exposed[card_index]==False:
                  canvas.draw_polygon([[card_pos[card_index],0],[card_pos[card_index],100],[card_pos[card_index+1],100]
                                 ,[card_pos[card_index+1],0]],1, 'black','green' )
   
         
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)

label = frame.add_label('Turns = 0')


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
