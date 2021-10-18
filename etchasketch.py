from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def screen_clear():
    #screen.clearscreen()
    tim.reset()


def clockwise():
    tim.right(5)


def anticlockwise():
    tim.left(5)


screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = anticlockwise)
screen.onkey(key = "d", fun = clockwise)
screen.onkey(key = "c", fun = screen_clear)


screen.exitonclick()