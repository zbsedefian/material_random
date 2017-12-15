import turtle
import math
from random import *

def main():
    """Draws a random amount of randomly-sized and sided polygons 
    and circles in so-called material design colors.
    """

    turtle.bgcolor("#263238")      #material-design blue-gray background

    bob = turtle.Turtle()
    print(bob)

    iterations = randint(20, 100)  #how many shapes to draw

    for i in range(iterations):
        # lift pen and move
        bob.penup()
        bob.fd(randint(10, 200))
        bob.rt(randint(1, 364))
        bob.pendown()
        # new pen color and width
        random_pen_color = get_color_choice()
        bob.pencolor(random_pen_color)
        bob.width(randint(1, 4))
        # draw
        random_drawing(bob)

    turtle.mainloop()


def polygon(t, n, size, reverse):
    """Draws polygon with n sides and size size
    """
    if(reverse == False):
        for i in range(n):
            t.fd(size)
            t.rt(360/n)
    else:
    	for i in range(n):
            t.bk(size)
            t.lt(360/n)


def circle(t, r):
    """ Draws circle (c = circumference)
    """
    c = 2 * math.pi * r
    n = 50
    length = c / n
    polygon(t, n, length, False)


def random_drawing(t):
    """Chooses to draw circle or polygon 
    (1/7 chance to choose circle)
    """
    choice = randint(1, 7)
    if choice == 1:
        r_rand = randint(1, 50)
        circle(t, r_rand)
    else:
        sides_rand = randint(1, 15)
        size_rand = randint(1, 80)
        polygon(t, sides_rand, size_rand, True)


def get_color_choice():
    """Chooses material-design-inspired pen color
    """
    color_choice = randint(1, 10)
    if color_choice == 1:
        random_pen_color = ("#ffd600")
    elif color_choice == 2:
        random_pen_color = ("#00e676")
    elif color_choice == 3:
        random_pen_color = ("#009688")
    elif color_choice == 4:
        random_pen_color = ("#0288d1")
    elif color_choice == 5:
        random_pen_color = ("#00acc1")
    elif color_choice == 6:
        random_pen_color = ("#d500f9")
    elif color_choice == 7:
        random_pen_color = ("#f06292")
    elif color_choice == 8:
        random_pen_color = ("#e64a19")
    elif color_choice == 9:
        random_pen_color = ("#ff1744")
    else:
        random_pen_color = ("#c6ff00")

    return random_pen_color

if __name__ == "__main__":
	main()