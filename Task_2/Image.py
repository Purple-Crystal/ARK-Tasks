import tkinter as tk
import cv2 as cv
root = tk.Tk()

width = 900
height = 500

canvas = tk.Canvas(root, bg='white', width=width, height=height)
canvas.pack()

ball = canvas.create_oval(430, 10, 470, 50, fill='green')

platform_y = height - 40
img = tk.PhotoImage(file="C:/Research Group/Level1.png")
image = canvas.create_image(width//2-50, platform_y,anchor=tk.N, image=img)
xspeed = yspeed = 2

def move_ball():
  global xspeed, yspeed
  x1, y1, x2, y2 = canvas.coords(ball)
  if x1 <= 0 or x2 >= width:
    # hit wall, reverse x speed
    xspeed = -xspeed
  if y1 <= 0:
    # hit top wall
    yspeed = 2
  elif y2 >= platform_y:
    # calculate center x of the ball
    cx = (x1 + x2) // 2
    # check whether platform is hit
    px1, px2 = canvas.coords(image)
    w, h = img.width(), img.height()
    if px1 <= cx <=px1+ w:
      yspeed = -2
    else:
      canvas.create_text(width//2, height//2, text='Game Over', font=('Arial Bold', 32), fill='red')
      return
  canvas.move(ball, xspeed, yspeed)
  canvas.after(20, move_ball)

x1, y1 = canvas.coords(image)
w, h = img.width(), img.height()

flag=0

def right():
  x1, y1 = canvas.coords(image)
  print(x1)
  w, h = img.width(), img.height()
  if (x1+w)>(width+90):
    return
  dx = 6
  canvas.move(image, dx, 0)
  root.after(94, right)


def left():
  x1, y1 = canvas.coords(image)
  w, h = img.width(), img.height()
  if(x1<0):
    return
  dx = 6
  canvas.move(image, -dx, 0)
  root.after(94, left)

def movement():
  x1, y1 = canvas.coords(image)
  w, h = img.width(), img.height()
  if (x1+w>width+90):
    left()
  else:
    right()
  root.after(5000, movement)

movement()
move_ball()
root.mainloop()