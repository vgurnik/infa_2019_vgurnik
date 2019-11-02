from tkinter import *
from tkinter import messagebox as mb
from random import randrange as rnd, choice

# init
root = Tk()
width = 1200
height = 700
root.geometry(str(width)+'x'+str(height))
main_menu = Menu(root)
root.config(menu=main_menu)
menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Меню', menu=menu)
mode = Menu(menu, tearoff=0)
canv = Canvas(root, bg='black')
canv.pack(fill=BOTH, expand=1)
colors = ['red', 'orange', 'yellow', 'green', 'blue']
scoreLabel = Label(text="Текущий счет: 0", font=("Comic Sans MS", 12, "bold"))
scoreLabel.config(bd=0, bg='white')
scoreLabel.pack()
score = 0
objects = []
obj_count = 0
difficulty = IntVar()
difficulty.set(0)


# creating new one
def new_ball():
    global obj_count
    r = rnd(30, 50)
    x = rnd(100, width - 100)
    y = rnd(100, height - 100)
    f = 0
    while f == 0 & obj_count < 10:
        f = 1
        for t in objects:
            x1 = (canv.coords(t[0])[0] + canv.coords(t[0])[2]) / 2
            y1 = (canv.coords(t[0])[1] + canv.coords(t[0])[3]) / 2
            r1 = (canv.coords(t[0])[2] - canv.coords(t[0])[0]) / 2
            if (x - x1) ** 2 + (y - y1) ** 2 < (r + r1) ** 2:
                r = rnd(30, 50)
                x = rnd(100, width - 100)
                y = rnd(100, height - 100)
                f = 0
    vx = rnd(0, 7 + 2 * score // 20) - 3 - score // 20  # velocity depends on score
    vy = rnd(0, 7 + 2 * score // 20) - 3 - score // 20
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
        if target[1] > 210 - 10 * (score + 1) ** (1/3):  # this is formula for decreasing of ball's lifetime
            canv.delete(target[0])      # the ball is dead, we remove corpse
            objects.remove(target)
            obj_count -= 1
        else:
            x = (canv.coords(target[0])[0] + canv.coords(target[0])[2]) / 2     # we're getting target's coords
            y = (canv.coords(target[0])[1] + canv.coords(target[0])[3]) / 2
            r = (canv.coords(target[0])[2] - canv.coords(target[0])[0]) / 2
            if (x < r) | (x > width - r):
                target[2][0] *= -1
            if (y < r) | (y > height - r):
                target[2][1] *= -1
            for second in objects:
                if second != target:
                    x1 = (canv.coords(second[0])[0] + canv.coords(second[0])[2]) / 2    # something difficult to calc
                    y1 = (canv.coords(second[0])[1] + canv.coords(second[0])[3]) / 2    # it's bouncing
                    r1 = (canv.coords(second[0])[2] - canv.coords(second[0])[0]) / 2
                    if (x1 - x)**2 + (y1 - y)**2 < (r1 + r)**2:
                        xn = (x1 + x) / 2 - x
                        yn = (y1 + y) / 2 - y
                        xv = target[2][0]
                        yv = target[2][1]
                        x_proj = xn / (xn**2 + yn**2) * (xv * xn + yv * yn)
                        y_proj = yn / (xn**2 + yn**2) * (xv * xn + yv * yn)
                        target[2][0] -= 2 * x_proj
                        target[2][1] -= 2 * y_proj
            canv.move(target[0], target[2][0], target[2][1])

    needed_num = (score // 10) + 1      # this is formula for balls current number
    if obj_count < needed_num:
        for i in range(needed_num - obj_count):
            new_ball()
    root.after(10, update)


def new_game():     # start new game
    global obj_count, score
    obj_count = 0
    canv.delete(ALL)
    objects.clear()
    score = 0
    scoreLabel['text'] = "Текущий счет: 0"
    if difficulty.get() > 0:
        difficulty.set(0)
        mb.showerror("Ошибка", "Пока так нельзя")


new_ball()
canv.bind('<Button-1>', click)
mode.add_radiobutton(label='endless mode', var=difficulty, value=0, command=new_game)   # menu setting
mode.add_radiobutton(label='easy mode', var=difficulty, value=1, command=new_game)
mode.add_radiobutton(label='hardcore', var=difficulty, value=2, command=new_game)
menu.add_command(label='Новая игра', command=new_game)
menu.add_cascade(label='Режим', menu=mode)
root.after(10, update)
mainloop()
