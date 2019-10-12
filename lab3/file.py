from lab3.graph import *
import tkinter
import math as m

windowSize(500, 450)
canvasSize(500, 450)
# Body
penSize(0)
brushColor(255, 100, 0)
circle(250, 430, 130)
# Hands
penSize(20)
penColor(230, 200, 175)
line(125, 325, 45, 55)
line(375, 325, 455, 55)
penSize(0)
penColor(170, 75, 0)
polygon([(185, 333), (155, 380), (100, 370), (95, 315), (144, 292)])
polygon([(315, 333), (345, 380), (400, 370), (405, 315), (356, 292)])
brushColor(230, 200, 175)
penSize(1)
penColor(240, 220, 200)
circle(45, 50, 20)
circle(455, 50, 20)
# Head
circle(250, 230, 120)
# Eyes
penSize(1)
penColor(120, 120, 120)
brushColor(128, 180, 255)
circle(210, 200, 25)
circle(290, 200, 25)
brushColor(0, 0, 0)
circle(208, 205, 7)
circle(292, 205, 7)
# Mouth
brushColor(120, 70, 30)
polygon([(240, 230), (260, 230), (250, 250)])
# Nose
brushColor(255, 40, 40)
polygon([(180, 260), (315, 260), (250, 300)])
# Hair
brushColor(210, 40, 255)
for i in range(9):
    fi = (i - 4) / 4 * m.pi / 4
    polygon([(250 - 120 * m.sin(fi - .15), 230 - 120 * m.cos(fi - .15)),
             (250 - 120 * m.sin(fi + .15), 230 - 120 * m.cos(fi + .15)),
             (250 - 155 * m.sin(fi), 230 - 155 * m.cos(fi))])
# Text
text = tkinter.Text(width=24, height=1, bg="#60ff28", fg="black", font=('Arial', 30, 'bold'))
text.insert(tkinter.END, "   PYTHON  is  AMAZING")
text.config(state='disabled')
text.pack()
run()
