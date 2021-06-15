import tkinter as tk

root = tk.Tk()

width = 900
height = 500

canvas = tk.Canvas(root, bg='white', width=width, height=height)
canvas.pack()

ball = canvas.create_oval(430, 10, 470, 50, fill='green')

platform_y = height - 20
platform = canvas.create_rectangle(width//2-50, platform_y, width//2+50, platform_y+10, fill='black')

# ball moving speed
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
    px1, _, px2, _ = canvas.coords(platform)
    if px1 <= cx <= px2:
      yspeed = -2
    else:
      canvas.create_text(width//2, height//2, text='Game Over', font=('Arial Bold', 32), fill='red')
      return
  canvas.move(ball, xspeed, yspeed)
  canvas.after(20, move_ball)

def board_right(event):
  x1, y1, x2, y2 = canvas.coords(platform)
  # make sure the platform is not moved beyond right wall
  if x2 < width:
    dx = 100
    canvas.move(platform, dx, 0)

def board_left(event):
  x1, y1, x2, y2 = canvas.coords(platform)
  # make sure the platform is not moved beyond left wall
  if x1 > 0:
    dx = 100
    canvas.move(platform, -dx, 0)

canvas.bind_all('<Right>', board_right)
canvas.bind_all('<Left>', board_left)


move_ball()

root.mainloop()
