# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 18:38:44 2018

@author: toi1-
"""

#星型のコードをいじって、七芒星が描けるようにしました。


from turtle import*

reset()

#正七角形
penup()
setpos(-300, 100)
pendown()
for i in range(7):
    forward(100)
    left(360/7)
 
#2/7の七芒星
penup()
setpos(100, 100)
pendown()
pencolor("orange")
for i in range(7):
    forward (200)
    left(360*2/7)

#3/7の七芒星
penup()
setpos(-100, -200)
pendown()
pencolor("blue")
for i in range(7):
    forward (200)
    left(360*3/7)