from this import d
import turtle as trtl

drawing = trtl
drawing.speed(100)
#THE BLAZING SUN
drawing.begin_fill()
drawing.penup()
drawing.fillcolor('yellow')
drawing.goto(-680,195)
drawing.down()
drawing.circle(100,360,100)
drawing.end_fill()

drawing.penup()

# GRAZZ
drawing.begin_fill()
drawing.fillcolor('green')
drawing.goto(-789,-150)
drawing.pendown()
drawing.forward(1900)
drawing.right(90)
drawing.forward(300)
drawing.right(90)
drawing.forward(1900)
drawing.right(90)
drawing.forward(300)
drawing.end_fill()

#TABLE
drawing.penup()
drawing.pendown()
drawing.goto(0,-150)
drawing.forward(100)



wn = trtl.Screen()
wn.mainloop()