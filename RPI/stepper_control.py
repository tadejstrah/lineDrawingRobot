from time import sleep
from time import time
from threading import Thread
from gpiozero import LED

enable = LED(12)
enable.on()



dleft = LED(25)
dleft.on()
dright = LED(19)
dright.off()
left = LED(21)
right = LED(26)

def step_right(freq,stop):
    start = time()
    if(freq==0): return
    while (time()-start < stop):
        right.on()
        sleep(1/(2*freq))
        right.off()
        sleep(1/(2*freq))

def step_left(freq,stop):
    start = time()
    if(freq==0): return
    while (time()-start < stop):
        left.on()
        sleep(1/(2*freq))
        left.off()
        sleep(1/(2*freq))
def speed(l,r,ld,rd,time):
    if(ld): dleft.on()
    else: dleft.off()
    if(rd): dright.on()
    else: dright.off()
    t = Thread(target=step_left,args=(l,time))
    r = Thread(target=step_right,args=(r,time))
    t.start()
    r.start()
    sleep(time)
    return
for i in range(10):
	speed(i*30,i*30,0,1,0.3)


'''
    def setSpeed(left,right):
    global freqleft,freqright
    freqleft=left
    freqright = right

def test(state,time):
    if(state==1):
        setSpeed(500,500)
        start()
        
        sleep(time)
    setSpeed(0,0)'''
