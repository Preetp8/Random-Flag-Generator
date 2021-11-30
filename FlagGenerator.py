from turtle import *
import random

def drawSquare (w):
    '''Draw black border around maritime flags 

    Params: 
        w: (int) width of the square
    
    '''
    seth(90)
    for i in range(4):
        fd(w)
        right(90)
        
      
def drawVerticleRect (blc, w, h):
    '''Draw verticle rectangles
    
    Params:
        blc: (2-tuple) bottom left corner
        w: (int) width
        h: (int) heigth
    '''
    up()
    goto(blc)
    down()
    seth(0)
    goto ((blc[0] + w, blc[1]))   
    goto ((blc[0] + w, blc[1] + h))         
    goto ((blc[0],     blc[1] + h))
    goto(blc)
    
def drawHorizontalRect (blc, w, h):
    '''Draw horizontal rectangles
    
    Params:
        blc:(2-tuple) bottom left corner
        w:(int) width
        h: (int) heigth  
    '''
    up()
    goto(blc)
    down()
    seth(0)
    goto ((blc[0] + h, blc[1]))   
    goto ((blc[0] + h, blc[1] + w))         
    goto ((blc[0],     blc[1] + w))
    goto(blc)
    
    
def drawTriangle(blc,w):
    ''' Draw 4 triangles for flags 4 and 5
    
    Params:
        blc:(2-tuple) bottom left corner
        w:(int) width
    '''
    up()
    goto(((blc[0]),(blc[1] + w*1/8)))
    down()
    
    begin_fill()
    goto(((blc[0] + w*3/8),(blc[1] + w/2)))         #draw triangle on the
    goto(((blc[0]),(blc[1] + w*7/8)))                   #left side of the box
    goto(((blc[0]),(blc[1] + w/8)))
    end_fill()
    up()
    goto(((blc[0] + w/8),(blc[1])))                   #move turtle to bottom
    down()
    
    begin_fill()
    goto(((blc[0] + w/2),(blc[1] + w*3/8 )))          #draw triangle on the
    goto(((blc[0] + w*7/8),(blc[1])))                     #bottom of the box
    goto(((blc[0] + w/8),(blc[1])))
    end_fill()
    up()
    goto(((blc[0] + w),(blc[1] + w*1/8)))               #move turtle to right
    down()
    
    begin_fill()
    goto(((blc[0] + w*5/8),(blc[1] + w/2)))           #draw triangle on the 
    goto(((blc[0]+w),(blc[1] + w*7/8)))                 #right side of the box
    goto(((blc[0] + w),(blc[1] + w*1/8)))
    end_fill()
    up()
    goto(((blc[0] + w/8),(blc[1] + w)))               #move turtle to top
    down()
    
    begin_fill()
    goto(((blc[0] + w/2),(blc[1] + w*5/8)))      #draw triangle on top of 
    goto(((blc[0] + w*7/8),(blc[1] + w)))             #the box
    goto(((blc[0] + w/8),(blc[1] + w)))
    end_fill()

    
    
def draw0 (blc,w):
    '''
    Draw the zero maritime flag
    
    Params:
        blc:(2-tuple) bottom left corner
        w:(int) width
    '''
    up()
    goto(blc)
    down()
    pencolor("black")
    width(1)
    drawSquare(w)
    
def draw1(blc,w):
    '''Draw the first maritime flag
    
    Params:
        blc:(2-tuple) bottom left corner
        w:(int) width
    '''
    
    color("red")
    begin_fill()
    up()
    goto(blc)
    down()
    drawSquare(w)
    end_fill()
    
    color("yellow")
    begin_fill()
    blc = ((blc[0]),(blc[1] + w*(1/3)))
    drawVerticleRect(blc,w,w/3)
    end_fill()
    
    goto((blc[0]),(blc[1] - w*1/3))
    pencolor("black")
    drawSquare(w)
    

def draw2(blc,w):
    '''Draw the second maritime flag
    
    Params:
        blc:(2-tuple) bottom left corner
        w:(int) width
    '''
    color("yellow")
    
    begin_fill()
    up()
    goto(blc)
    down()
    drawSquare(w)
    end_fill()
    
    color("red")
    
    begin_fill()
    blc = ((blc[0]),(blc[1] + w*(1/3)))
    drawVerticleRect(blc,w,w/3)
    end_fill()
    
    goto((blc[0]),(blc[1] - w*1/3))
    pencolor("black")
    drawSquare(w)

def draw3(blc,w):
    '''Draw the third maritime flag
    
    Params:
        blc:(2-tuple) bottom left corner
        w:(int) width
    '''
    color("blue")
    
    begin_fill()
    up()
    goto(blc)
    down()
    drawSquare(w)
    end_fill()
    
    color("red")
    
    begin_fill()
    blc = ((blc[0]),(blc[1] + w*(1/3)))
    drawVerticleRect(blc,w,w/3)
    end_fill()
    
    goto((blc[0]),(blc[1] - w*1/3))
    pencolor("black")
    drawSquare(w)
    
def draw4(blc,w):
    '''Draw the fourth maritime flag
    
    Params:
        blc:(2-tuple) bottom left corner
        w:(int) width
    '''
    color("red")
    drawTriangle(blc,w)
    
    up()
    goto(blc)
    down()
    pencolor("black")
    drawSquare(w)
    
def draw5(blc,w):
    '''Draw the fifth maritime flag
    
    Params:
        blc:(2-tuple) bottom left corner
        w:(int) width
    '''
    up()
    goto(blc)
    down()
    color("blue")
    begin_fill()
    drawSquare(w)
    end_fill()
    
    color("yellow")
    drawTriangle(blc,w)
    
    up()
    goto(blc)
    down()
    pencolor("black")
    drawSquare(w)
    
def draw6(blc,w):
    '''Draw the sixth maritime flag
    
    Params:
        blc:(2-tuple) bottom left corner
        w:(int) width
    '''
    up()
    goto(blc)
    down()
    color("blue")
    begin_fill()
    drawSquare(w)
    end_fill()
    
    color("white")
    begin_fill()
    up()
    goto((blc[0]),(blc[1]+ w*2/3 ))
    down()
    goto((blc[0]+w/3),(blc[1]+w))
    goto((blc[0]),(blc[1]+w))
    goto((blc[0]),(blc[1]+ w*2/3 ))
    end_fill()
    
    goto(blc)
    goto((blc[0] + w*2/3),(blc[1]))
    begin_fill()
    goto((blc[0] + w),(blc[1] + w*1/3))
    goto((blc[0] + w),(blc[1]))
    goto((blc[0] + w*2/3),(blc[1]))
    end_fill()
    
    up()
    goto(blc)
    goto((blc[0]),(blc[1] + w/3))
    down()
    begin_fill()
    goto((blc[0]+w*2/3),(blc[1]+w))
    goto((blc[0]+w*2/3),(blc[1]+w))
    goto((blc[0]+w*5/6),(blc[1]+w))
    goto((blc[0]),(blc[1]+w*1/6))
    end_fill()
    
    up()
    goto(blc)
    goto((blc[0] + w/3),(blc[1]))
    down()
    begin_fill()
    goto((blc[0]+w),(blc[1]+w*2/3))
    goto((blc[0]+w),(blc[1]+w*2/3))
    goto((blc[0]+w),(blc[1]+w*5/6))
    goto((blc[0]+w*1/6),(blc[1]))
    end_fill()
    
    up()
    goto(blc)
    down()
    pencolor("black")
    drawSquare(w)

def draw7(blc,w):
    '''Draw the seventh maritime flag
    Params:
        blc:(2-tuple) bottom left corner
        w:(int) width
    '''
    '''Draw seventh maritime flag
    
    Params:
        blc:(2-tuple) bottom left corner
        w:(int) width
    '''
    color("red")
    
    begin_fill()
    up()
    goto(blc)
    down()
    drawSquare(w)
    end_fill()
    
    color("white")

    begin_fill()
    blc = ((blc[0] + w*1/3),(blc[1]))
    drawHorizontalRect(blc,w,w/3)
    end_fill()
    goto((blc[0] - w*1/3),(blc[1]))
    pencolor("black")
    drawSquare(w)
    
    
def draw8(blc,w):
    '''Draw the eighth maritime flag
    
    Params:
        blc:(2-tuple) bottom left corner
        w:(int) width
    '''
    color("yellow")
    
    begin_fill()
    up()
    goto(blc)
    down()
    drawSquare(w)
    end_fill()
    
    color("blue")
    
    begin_fill()
    blc = ((blc[0] + w*1/3),(blc[1]))
    drawHorizontalRect(blc,w,w/3)
    end_fill()
    goto((blc[0] - w*1/3),(blc[1]))
    pencolor("black")
    drawSquare(w)
    
def draw9(blc,w):
    '''Draw the ninth maritime flag
    
    Params:
        blc:(2-tuple) bottom left corner
        w:(int) width
    '''
    color("blue")
    
    begin_fill()
    up()
    goto(blc)
    down()
    drawSquare(w)
    end_fill()
    
    color("white")
    
    begin_fill()
    blc = ((blc[0] + w*1/3),(blc[1]))
    drawHorizontalRect(blc,w,w/3)
    end_fill()
    
    goto((blc[0] - w*1/3),(blc[1]))
    pencolor("black")
    drawSquare(w)
    
def drawDigit(n, blc, w):
    '''Draw corresponding draw function for n
    
    Params:
    n (int): number from 0 to 9 (inclusive) that corresponds with flag numbers 
    blc(2-tuple): bottom left corner
    w(int): width
    '''
    assert type(n) == int
    assert n >= 0  and n <= 9
    
    
    functs = [
        draw0, draw1, draw2, draw3, draw4, 
        draw5, draw6, draw7, draw8, draw9
        ]
        
    functs[n](blc, w)
            

# 
# speed(0)
# drawDigit(9,(10,10), 100)


# draw1((100,100), 100)
# draw2((50,50), 100)
# draw3((0,0), 100)
# draw4 ((0,0),100)
# draw5 ((100,100),100)
# draw7((-50,-50), 100)
# draw8((-100,-100), 100)
# draw9((-150,-150), 100)

################################################################################

def natoRecur (sn, blc, w, g):
    
    """ Using turtle graphics, draw a positive integer in NATO signal flags.

    This is the recursive function.
    
    In this function, the location, size, and gap are already specified.
    Digits should be drawn in the same order as the associated number.
    For example, 367 would be drawn as 3-flag gap 6-flag gap 7-flag.

    Reference: https://en.wikipedia.org/wiki/International_maritime_signal_flags

    Params: 
        sn (str) the positive integer to be drawn, as a string
        blc (float 2-tuple): Cartesian coordinates of the bottom left corner 
                             of the leftmost digit flag
        w (int): width of each digit flag, in pixels
        g (int): the gap between flags, in pixels
    """

    assert type(sn) == str
    assert type(blc) == tuple and len(blc) == 2
    assert type(w) == int and w > 0
    assert type(g) == int and g > 0
    
    if len(sn)==1:
        drawDigit(int(sn), blc, w)
    else:
        drawDigit(int(sn[0]),blc,w)
        blc = ((blc[0]+w)+g),(blc[1])
        natoRecur(sn[1:],blc,w,g)
        

def nato (n):

    """ Using turtle graphics, draw a positive integer in NATO signal flags.

    This function has two purposes:
    1) to randomize the position/size/gap of the flag
    2) to cast the number to a string, for simpler recursion

    Algorithm:
    - randomize the location of the first flag:
      the Cartesian coordinates blc = (px,py) of the bottom left corner 
      of the first digit should to be chosen at random
      within the square bounded by (-400,-100) and (-350,0)

    - randomize the size of the flags:
      the width w of each digit should be chosen at random 
      so that 50 <= w <= 100 (use the same width for all digits)

    - randomize the gap between consecutive flags:
      the gap g between consecutive digits should be chosen at random
      so that 1 <= g <= 10

    - cast n to a string 
    - call natoRecur, the recursive function that does the rest of the work

    Params: 
        n (int) the positive integer to be drawn (n>0)
    """
    blc = (random.randint(-400,-350)),(random.randint(-100,0))
    
    
    w = random.randint(50,100)
    g = random.randint(1,10)
    
    
    natoRecur(str(n), blc, w ,g)




################################################################################
#                                  TESTER
################################################################################
speed(0)                             # draw at max speed, to help the TA's grade
             # while you are debugging, I suggest slowing this to, say, speed(3)
             
n = random.randint (100,99999999999) 

# n = 1023456789

print ('my random number to draw is ' + str(n))

nato (n)
hideturtle()
done()
                                                          

