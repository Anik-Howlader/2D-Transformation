# Assignment : 2D Transformation in Computer Graphics (Matrix Operation)
import math
import turtle
import numpy as np

# Point input as P1(x,y)
x, y = turtle.textinput("User Input","P1(x,y) = ").split()
# Matrix of point P(x,y)
P1 = np.array([[int(x), int(y)]])

# Point input as P2(x,y)
x, y = turtle.textinput("User Input","P2(x,y) = ").split()
# Matrix of point P(x,y)
P2 = np.array([[int(x), int(y)]])

# Point input as P3(x,y)
x, y = turtle.textinput("User Input","P3(x,y) = ").split()
# Matrix of point P(x,y)
P3 = np.array([[int(x), int(y)]])


kolom=turtle.Turtle()
kolom.pensize(3)
kolom.penup()

def magic():
    global P1, P2, P3
    x = int(P1[0][0])
    y = int(P1[0][1])
    kolom.goto(x,y)
    kolom.pendown()
    kolom.write("P1 ["+str(x)+ ","+str(y)+"]")
    x = int(P2[0][0])
    y = int(P2[0][1])
    kolom.goto(x, y)
    kolom.write("P2 ["+str(x)+ ","+str(y)+"]")
    x = int(P3[0][0])
    y = int(P3[0][1])
    kolom.goto(x,y)
    kolom.write("P3 ["+str(x)+ ","+str(y)+"]")
    x = int(P1[0][0])
    y = int(P1[0][1])
    kolom.goto(x, y)
    kolom.penup()


def Translation():
    # Translation Matrix as T
    tx, ty = turtle.textinput("Translation", "T(tx,ty) = ").split()
    T = np.array([[int(tx), int(ty)]])
    kolom.clear()
    magic()
    global P1, P2, P3
    P1 = np.add(P1, T)
    P2 = np.add(P2, T)
    P3 = np.add(P3, T)
    magic()


def Rotation():
    # Rotation Matrix as R
    θ = float(turtle.textinput("Rotation", "angle(θ) = "))
    R = np.array([[math.cos(θ), math.sin(θ)], [-math.sin(θ), math.cos(θ)]])
    kolom.clear()
    magic()
    global P1, P2, P3
    P1 = np.dot(P1, R)
    P2 = np.dot(P2, R)
    P3 = np.dot(P3, R)
    magic()


def Scaling():
    # Scaling Matrix as S
    sx, sy = turtle.textinput("Scaling", "S(sx,sy) = ").split()
    S = np.array([[int(sx), 0], [0, int(sy)]])
    kolom.clear()
    magic()
    global P1, P2, P3
    P1 = np.dot(P1, S)
    P2 = np.dot(P2, S)
    P3 = np.dot(P3, S)
    magic()


# Query
while True:
    Query = turtle.textinput("Query", "[T=Translation,R=Rotation,S=Scaling]")
    if Query == "T":
        Translation()
    elif Query == "R":
        Rotation()
    elif Query == "S":
        Scaling()
    else:
        print("Invalid Query !!!")
        break

turtle.done()