import turtle

myTurtle = turtle.Turtle()
myTurtle.speed('fastest')
myWin = turtle.Screen()


def drawLine(myTurtle, lineLen=0):
    if lineLen < 10:
        myTurtle.forward(lineLen)
        # print(lineLen)
        drawLine(myTurtle, lineLen+1)


def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-5)

# drawSpiral(myTurtle, 100)
drawLine(myTurtle)
myWin.exitonclick()
