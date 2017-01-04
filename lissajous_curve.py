#!/usr/bin/env python3

import math, turtle


def main():
    welcome()
    a = input("Podaj a: ")
    try:
        x = int(a)
    except ValueError as err:
        print(err)
    b = input("Podaj b: ")    
    try:
        y = int(b)
    except ValueError as err:
        print(err)

    screen_and_turtle(x, y)


def screen_and_turtle(a, b):
    win = turtle.Screen()
    win.setup(800, 600)
    win.title("Lissajous curve")
    win.bgcolor("black")

    z = turtle.Turtle()
    z.color("white")
    z.shape("circle")
    z.pensize(0)
    z.speed(0)
    z.hideturtle()
    
    lissajous(z, a, b)

    win.mainloop()


def lissajous(it, a, b):
 
    for i in range(720):
        it.penup()
        it.goto((math.sin(a*i)*250), (math.sin(b*i) * 250))
        it.stamp()


def welcome():
    print('''
      Welcome to program drawing Lissajous curve!
    The best result you can reach is when "a" is 
    even and "b" is odd, but have fun with this!
                                            Ejdrian
    ''')


main()
