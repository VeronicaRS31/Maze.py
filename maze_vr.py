#1.2.4 Turtle Escape
import turtle as trtl 
import random as rand
walls=trtl.Turtle()
walls.speed(0)
walllenght=25
doorwidth=15
barrier_lenght=30
maze_runner= trtl.Turtle(shape= "turtle")
maze_runner.turtlesize(1)
maze_runner.color("pink")
maze_runner.hideturtle()
walls.pencolor("black")

def draw_door(x):
  walls.forward(x)
  walls.pu()
  walls.forward(doorwidth)
  walls.pd()

def runner_down():
  maze_runner.setheading(270)

def runner_up():
  maze_runner.setheading(90)

def runner_left():
  maze_runner.setheading(180)

def runner_right():
  maze_runner.setheading(0)

def runner_move():
  maze_runner.forward(5)
 


for i in range(25):
  walls.left(90)
  if i<1:
    walls.forward(walllenght)
  elif i<5:
    x= rand.randint(0,walllenght-doorwidth)
    draw_door(x)
    walls.forward(walllenght-x-doorwidth)
  else:
    if rand.randint(0,1)==1:
      x= rand.randint(0,walllenght-doorwidth)
      draw_door(x)
      y= rand.randint(0,walllenght-doorwidth-x)
      walls.forward(y)
      walls.left(90)
      walls.forward(barrier_lenght)
      walls.backward(barrier_lenght)
      walls.right(90)
      walls.forward(walllenght-x-y-doorwidth)
    else:
      y= rand.randint(0,walllenght-doorwidth)
      walls.forward(y)
      walls.left(90)
      walls.forward(barrier_lenght)
      walls.backward(barrier_lenght)
      walls.right(90)
      x= rand.randint(0,walllenght-doorwidth-y)
      draw_door(x)
      walls.forward(walllenght-x-y-doorwidth)
      walls.pd()
  walllenght+=15
  walls.hideturtle()
  maze_runner.showturtle()

wn=trtl.Screen()
wn.onkeypress(runner_down,"a")
wn.onkeypress(runner_up,"b")
wn.onkeypress(runner_left,"c")
wn.onkeypress(runner_right,"d")
wn.onkeypress(runner_move,"g")
wn.listen()

wn = trtl.Screen()
wn.mainloop()
