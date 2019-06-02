#Yew Journ Chan
#May 30, 2019
#Version 5

import turtle

#Starting with Point Alnitak
turtle.hideturtle() #this command hides arrow symbols identified as "turtle"
turtle.dot(10) #indicating the point starting at Alnitak
turtle.write("Alnitak") #label point "Alnitak"

#Point Betelgeuse
turtle.left(110) #pivoting towards direction of point Betelgeuse
turtle.forward(320) #distance between point Alnitak and point Betelgeuse
turtle.dot(10) #indicating point Betelgeuse
turtle.write("Betelgeuse") #label point "Betelgeuse"
turtle.penup() #lift pen to prevent drawing when retracing steps
turtle.backward(320) #retracing steps back to point "Alnitak"

#Point Saiph
turtle.pendown() #pen down to begin drawing again
turtle.left(135) #pivoting left towards direction of point Saiph
turtle.forward(250) #distance between point Alnitak and point Saiph
turtle.dot(10) #indicating point Saiph
turtle.write("Saiph") #label point "Saiph"

#Point Alnilam
turtle.penup() #lift pen to prevent drawing when retracing steps
turtle.backward(250) #retracing steps back to point Alnitak
turtle.pendown() #pen down to start drawing again
turtle.left(140) #pivoting left to point Alnilam
turtle.forward(70) #distance between point Alnitak and point Alnilam
turtle.dot(10) #indicating point Anilam
turtle.write("Alnilam") #label point "Alnilam"

#Point Mintaka
turtle.forward(70) #distance between point Alnilam and point Mintaka
turtle.dot(10) #indicating point Mintaka
turtle.write("Mintaka") #lavel point "Mintaka"

#Point Meissa
turtle.left(50) #pivoting left to point Meissa
turtle.forward(250) #distance between point Mintaka and point Meissa
turtle.dot(10) #indicating point Meissa
turtle.write("Meissa") #label point "Meissa"

#Point Rigel
turtle.penup() #lift pen to prevent drawing when retracing steps
turtle.backward(250) #retracing steps back to point Mintaka
turtle.pendown() #pen down to start drawing again
turtle.right(150) #pivoting right to point Rigel
turtle.forward(240) #distance between point Mintaka and point Rigel
turtle.dot(10) #indicating point Rigel
turtle.write("Rigel") #label point "Rigel"
