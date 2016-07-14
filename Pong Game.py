##########################################################
#12:12 PM
#Thursday, July 01, 2016 (GMT+5:30) 
#@ author : VAIBHAV GUPTA(15454) 

#########################################################
# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos=[WIDTH / 2, HEIGHT/2]
ball_vel=[0,0]
paddle1_pos = 160
paddle2_pos = 160

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left




def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH / 2, HEIGHT/2]
    ball_vel[1]=-((random.randrange(60, 180))/60)
    if direction==True:
        ball_vel[0]=((random.randrange(120, 240))/60)
    else:
        ball_vel[0]=-((random.randrange(120, 240))/60)


# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(RIGHT)
    paddle1_vel=0
    paddle2_vel=0
    score1=0
    score2=0

    
    
#drawing canvas    



def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,PAD_WIDTH,PAD_HEIGHT
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], PAD_WIDTH, "olive")
    canvas.draw_line([0, 0],[0, HEIGHT], PAD_WIDTH+8, "olive")
    canvas.draw_line([WIDTH, 0],[WIDTH , HEIGHT], PAD_WIDTH+8, "olive")
        
 
    
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,1,'orange','orange')
    
    
    # update paddle's vertical position, keep paddle on the screen
    if ((4<=paddle1_pos<=316) or (paddle1_pos==1 and paddle1_vel==3)or(paddle1_pos==319 and paddle1_vel==-3)):
           paddle1_pos+=paddle1_vel
        
    if ((4<=paddle2_pos<=316) or (paddle2_pos==1 and paddle2_vel==3)or(paddle2_pos==319 and paddle2_vel==-3))==True:
           paddle2_pos+=paddle2_vel   
    
    
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos], [PAD_WIDTH-1, paddle1_pos], [PAD_WIDTH-1, paddle1_pos + PAD_HEIGHT], [0, paddle1_pos + PAD_HEIGHT]], 3, 'red', 'Red')
    canvas.draw_polygon([[WIDTH - PAD_WIDTH+1, paddle2_pos], [WIDTH - PAD_WIDTH+1, paddle2_pos + PAD_HEIGHT], [WIDTH, paddle2_pos + PAD_HEIGHT], [WIDTH, paddle2_pos]], 3, 'navy', 'navy')
  
    
    
    # determine whether paddle and ball collide    
    if ((ball_pos[0]<=(BALL_RADIUS+PAD_WIDTH))  and (ball_pos[1]>=paddle1_pos)and(ball_pos[1]<=(paddle1_pos+PAD_HEIGHT)) )==True:
        
        ball_vel[0]=-(1.1*ball_vel[0])
    
    if (ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH) and (paddle2_pos <= ball_pos[1] <= paddle2_pos + 80):
        ball_vel[0] = - 1.1 * ball_vel[0]    
    
    
    # update ball if it doesn't collide with pad
    
    
    ball_pos[0]+=ball_vel[0]        
    ball_pos[1]+=ball_vel[1]
    if ((ball_pos[0]<=(BALL_RADIUS+PAD_WIDTH)) and not (paddle1_pos <= ball_pos[1] <= paddle1_pos + 80))==True:
        score2+=1
        spawn_ball(RIGHT)
    if (ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH) and not (paddle2_pos <= ball_pos[1] <= paddle2_pos + 80)==True:
        score1+=1 
        spawn_ball(LEFT)        
    if (ball_pos[1]>=(HEIGHT-BALL_RADIUS) or ball_pos[1]<=BALL_RADIUS ):    
         ball_vel[1]=-ball_vel[1]
    
    # draw scores
    canvas.draw_text(str(score1), [250, 50], 50, 'maroon')
    canvas.draw_text(str(score2), [338, 50], 50, 'maroon') 
    canvas.draw_text(' @Vaibhav',[400,300],20,'black')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = -3
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 3
    elif key==simplegui.KEY_MAP["s"] and key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = -3
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 3
    elif key==simplegui.KEY_MAP["up"] and key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0   

        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"] or key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key==simplegui.KEY_MAP['up'] or key==simplegui.KEY_MAP['down']:
        paddle2_vel = 0 

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('NEW GAME !',new_game)
frame.set_canvas_background('white')
# start frame
new_game()
frame.start()
