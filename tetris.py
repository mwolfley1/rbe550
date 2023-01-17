import turtle
t = turtle.Turtle()

size = 10

def draw_rect(x0,y0,len,hgt, clr): #draw recetangle from 0 to 1
    t.fillcolor(clr)
    t.begin_fill()
    t.penup()
    t.goto(x0,y0)
    t.pendown()
    t.goto(x0+len,y0)
    t.goto(x0+len,y0+hgt)
    t.goto(x0,y0+hgt)
    t.goto(x0,y0)
    t.end_fill()

def draw_line(xval,yval):
    for jj in range(4):
        draw_rect(xval,yval,size,size,'red')
        yval += size

def draw_tee(xval,yval):
    color = 'green'
    for jj in range(3):
        draw_rect(xval,yval,size,size,color)
        xval += size
    yval += size
    xval -= size*2
    draw_rect(xval,yval,size,size,color)

def draw_l(xval,yval):
    color = 'yellow'
    for jj in range(3):
        draw_rect(xval,yval,size,size,color)
        yval += size
    yval -= size*3
    xval += size
    draw_rect(xval,yval,size,size,color)

def draw_z(xval,yval):
    color = 'pink'
    for jj in range(2):
        draw_rect(xval,yval,size,size,color)
        xval += size
    yval += size
    xval -= size
    draw_rect(xval,yval,size,size,color)
    xval += size
    draw_rect(xval,yval,size,size,color)

xval = -200
yval = 0

draw_line(xval,yval)

xval = 200
yval = 0

draw_tee(xval,yval)

xval = -100
yval = 0

draw_l(xval,yval)

xval = -200
yval = 100

draw_z(xval,yval)

xval = -200
yval = 0

draw_line(xval,yval)
draw_line(xval,yval)
draw_line(xval,yval)
draw_line(xval,yval)