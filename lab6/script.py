from tkinter import *
from random import randrange as rnd, choice
import time

# init
root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='black')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue']
scoreLabel = Label(text="Текущий счет: 0", font=("Comic Sans MS", 12, "bold"))
scoreLabel.config(bd=0, bg='white')
scoreLabel.pack()
score = 0
objects = []
obj_count = 0


# creating new one
def new_ball():
    global obj_count
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    vx = rnd(0, 7 + 2 * score // 50) - 3 - score // 50  # velocity depends on score
    vy = rnd(0, 7) - 3
    if vx**2 + vy**2 == 0:
        vx = 1
    obj_count += 1
    # first member is ball, second is its lifetime, third is its velocity
    objects.append([canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0), 0, [vx, vy]])


# click event listener
def click(event):
    global score, obj_count
    for target in objects:
        x = (canv.coords(target[0])[0] + canv.coords(target[0])[2]) / 2     # we're getting target's coords
        y = (canv.coords(target[0])[1] + canv.coords(target[0])[3]) / 2
        r = (canv.coords(target[0])[2] - canv.coords(target[0])[0]) / 2
        if (x - event.x)**2 + (y - event.y)**2 <= r*r:  # and check if we hit it
            score += 1
            scoreLabel['text'] = "Текущий счет: " + str(score)
            canv.delete(target[0])  # then delete it
            objects.remove(target)
            obj_count -= 1


# updater
def update():
    # difficulty depends on score
    global obj_count
    for target in objects:
        target[1] += 1      # counting lifetime
        if target[1] > 110 - 10 * (score + 1) ** (1/3):  # this is formula for decreasing of ball's lifetime
            canv.delete(target[0])      # the ball is dead, we remove corpse
            objects.remove(target)
            obj_count -= 1
        else:
            x = (canv.coords(target[0])[0] + canv.coords(target[0])[2]) / 2     # we're getting target's coords
            y = (canv.coords(target[0])[1] + canv.coords(target[0])[3]) / 2
            r = (canv.coords(target[0])[2] - canv.coords(target[0])[0]) / 2
            if (x < r) | (x > 800 - r):
                target[2][0] *= -1
            if (y < r) | (y > 600 - r):
                target[2][1] *= -1
            canv.move(target[0], target[2][0], target[2][1])

    needed_num = (score // 30) + 1      # this is formula for balls current number
    if obj_count < needed_num:
        for i in range(needed_num - obj_count):
            new_ball()
    root.after(10, update)


new_ball()
canv.bind('<Button-1>', click)
root.after(10, update)
mainloop()
