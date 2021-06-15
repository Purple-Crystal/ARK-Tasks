import numpy as np
import random
import tkinter as tk

WIDTH = 400
HEIGHT = 400
initial_speeds = [-6, -5, -4, 4, 5, 6]
dx, dy = 0, 0
while dx == dy:
    dx, dy = random.choice(initial_speeds), random.choice(initial_speeds) 

def bounce():
    global dx, dy
    x0, y0, x1, y1 = canvas.coords(my_ball)
    if x0 <= 0 or x1 >= WIDTH:    # compare to left of ball bounding box on the left wall, and to the right on the right wall
        dx = -dx
    if y0 <= 0 or y1 >= HEIGHT:   # same for top and bottom walls
        dy = -dy
    canvas.move(my_ball, dx, dy)
    root.after(50, bounce)

if __name__ == '__main__':

    root = tk.Tk()
    root.wm_title("Bouncing Ball")
    canvas = tk.Canvas(root, width=400, height=400, bg="black")
    canvas.pack(expand=True, fill=tk.BOTH)

    size=10
    x = 50
    y = 50
    my_ball = canvas.create_oval(x-size, y-size, x+size, y+size, fill="blue")

    bounce()
    root.mainloop()