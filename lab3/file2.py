from lab3.graph import *
import tkinter
import math as m

windowSize(1000, 450)
canvasSize(1000, 450)
# Body
penSize(0)
brushColor(0, 128, 0)
circle(250, 450, 130)
# Hands
penSize(20)
penColor(230, 200, 175)
line(125, 345, 45, 75)
line(375, 345, 455, 75)
penSize(0)
penColor(20, 75, 0)
polygon([(185, 353), (155, 400), (100, 390), (95, 335), (144, 312)])
polygon([(315, 353), (345, 400), (400, 390), (405, 335), (356, 312)])
brushColor(230, 200, 175)
penSize(1)
penColor(240, 220, 200)
circle(45, 70, 20)
circle(455, 70, 20)
# Head
circle(250, 250, 120)
# Eyes
penSize(1)
penColor(120, 120, 120)
brushColor(190, 200, 180)
circle(210, 220, 25)
circle(290, 220, 25)
brushColor(0, 0, 0)
circle(208, 225, 7)
circle(292, 225, 7)
# Mouth
brushColor(120, 70, 30)
polygon([(240, 250), (260, 250), (250, 270)])
# Nose
brushColor(255, 40, 40)
polygon([(180, 280), (315, 280), (250, 320)])
# Hair
brushColor(255, 210, 40)
for i in range(9):
    fi = (i - 4) / 4 * m.pi / 4
    polygon([(250 - 120 * m.sin(fi - .15), 250 - 120 * m.cos(fi - .15)),
             (250 - 120 * m.sin(fi + .15), 250 - 120 * m.cos(fi + .15)),
             (250 - 155 * m.sin(fi), 250 - 155 * m.cos(fi))])
# Body 2
penSize(0)
brushColor(255, 100, 0)
circle(750, 450, 130)
# Hands 2
penSize(20)
penColor(230, 200, 175)
line(625, 345, 545, 75)
line(875, 345, 955, 75)
penSize(0)
penColor(170, 75, 0)
polygon([(685, 353), (655, 400), (600, 390), (595, 335), (644, 312)])
polygon([(815, 353), (845, 400), (900, 390), (905, 335), (856, 312)])
brushColor(230, 200, 175)
penSize(1)
penColor(240, 220, 200)
circle(545, 70, 20)
circle(955, 70, 20)
# Head 2
circle(750, 250, 120)
# Eyes 2
penSize(1)
penColor(120, 120, 120)
brushColor(128, 180, 255)
circle(710, 220, 25)
circle(790, 220, 25)
brushColor(0, 0, 0)
circle(708, 225, 7)
circle(792, 225, 7)
# Mouth 2
brushColor(120, 70, 30)
polygon([(740, 250), (760, 250), (750, 270)])
# Nose 2
brushColor(255, 40, 40)
polygon([(680, 280), (815, 280), (750, 320)])
# Hair 2
brushColor(210, 40, 255)
for i in range(9):
    fi = (i - 4) / 4 * m.pi / 4
    polygon([(750 - 120 * m.sin(fi - .15), 250 - 120 * m.cos(fi - .15)),
             (750 - 120 * m.sin(fi + .15), 250 - 120 * m.cos(fi + .15)),
             (750 - 155 * m.sin(fi), 250 - 155 * m.cos(fi))])
# Text
text = tkinter.Text(width=48, height=1, bg="#60ff28", fg="black", font=('Arial', 40, 'bold'))
text.insert(tkinter.END, "     PYTHON  is  REALLY  AMAZING!")
text.config(state='disabled')
text.pack()
run()
