#A stopwatch game...This game requires the "simplegui" Python library to run

import simplegui

millis=0
second=0
minute=0
plays=0
hits=0


def draw(canv):
    canv.draw_text(str(minute)+":"+str(second)+"."+str(millis), [46,165], 75, "White")
    if plays==0 and hits==0:
        canv.draw_text(str(plays)+"/"+str(hits), [200,50], 50, "Red")
    else:
        canv.draw_text(score, [200,50], 50, "Red")
                    

def mil_sec_min():
    global millis, second, minute
    millis+=1
    if millis==10:
        millis=0
        second+=1
    if second==60:
        second=0
        minute+=1 
    
    
def start():
    timer1.start()
 
    
def stop():
    timer1.stop()
    scoreboard()
    
    
def reset():
    global millis, second, minute
    millis=0
    second=0
    minute=0
    
def scoreboard():
    global plays, hits, score
    if not (millis==0 and second==0 and minute==0):
        plays+=1
        if (str(second)[-1]==str(0) or str(second)[-1]==str(5)) and str(millis)[-1]==str(0):
            hits+=1
        score= str(hits)+"/"+str(plays)
    
    
           
frame = simplegui.create_frame("Stopwatch: The Game", 300, 300)

frame.set_draw_handler(draw)

frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)

timer1=simplegui.create_timer(100, mil_sec_min)


frame.start()
