
#"Stopwatch: The Game"
import simplegui

# define global variables
count = 0

m = 0
n = 0
p = 0
q = 0
time = "" #Empty string

successful_stops = 0
total_stops = 0
output = str(successful_stops) + '/' + str(total_stops) 
def counter() :
    global count
    count = count+1
    
    
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global m, n, p, q, time
    m = t // 600
    n = (t // 100) % 6
    p = (t // 10) % 10
    q = t % 10
    time = str(m) + ':' + str(n) + str(p) + '.' + str(q)
    return time
     
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    global q, successful_stops, total_stops, output
    
    if (timer.is_running() == True):	
        if ( q == 0 ):
            successful_stops += 1
        total_stops += 1
    output = str(successful_stops) + '/' + str(total_stops)
    
    timer.stop()
    
def reset():
    global count,successful_stops,total_stops,output
    count = 0
    format(count)
    successful_stops = 0
    total_stops = 0
    output = str(successful_stops) + '/' + str(total_stops)
    timer.stop()

# define event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(100, counter)

# define draw handler
def draw(canvas) :
    canvas.draw_text(format(count), [120, 105], 25, "red")
    canvas.draw_text(output, [0,20], 25, "white")   
    
# create frame
frame = simplegui.create_frame("StopWatch", 300, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 75)	
frame.add_button("Stop", stop, 75)
frame.add_button("Reset", reset, 75)

# start frame
frame.start()
