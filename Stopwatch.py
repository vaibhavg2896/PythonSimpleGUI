##########################################################
#04:45 PM
#Thursday, June 20, 2016 (GMT+5:30) 
#@ author : VAIBHAV GUPTA(15454) 

#########################################################
# template for "Stopwatch: The Game"
import simplegui

# define global variables
start_watch=True
width=300
height=200
time=0
score=0
hit=0
deci_sec=0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def formatt():
    global times, deci_sec
    deci_sec=time%10
    ntime=time/10
    mint=int(ntime/60)
    osec=(ntime%60)%10
    tsec=(ntime%60)/10
    return str(mint)+':'+str(tsec)+str(osec)+'.'+str(deci_sec)
    
# format for scoring
def new():
    global hit, score
    
    return str(score)+'/'+str(hit)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global start_watch
    start_watch=True
    timer.start()
def stop():
    global hit,score,deci_sec,start_watch
    timer.stop()
    if start_watch==True:
        if deci_sec%10==0:
            score+=1
        hit+=1
    start_watch=False
        
def reset():
    global score, hit, time
    score=0
    hit=0
    time=0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time+=1        
    
# define draw handler
def draw(canvas):
    global width,height
    canvas.draw_text(formatt(),[100,height/2],36,'white')
    canvas.draw_text(new(),[250,25],30,'yellow')
    
    
# create frame
frame=simplegui.create_frame('Timer fun',width,height)
   
#register event handlers
frame.add_button('Start',start,100)
frame.add_button('Stop',stop,100)
frame.add_button('Reset',reset,100)
frame.set_draw_handler(draw)
timer=simplegui.create_timer(100,tick)
# start frame
frame.start()

# Please remember to review the grading rubric
