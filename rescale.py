import turtle

yildiz = turtle.Turtle()   
yildiz.penup()
yildiz.goto(150,0)        
yildiz.pendown()
yildiz.getscreen().bgcolor("black")
yildiz.pensize(4)       
yildiz.speed(10)

for i in range(10):
   for colours in["cyan", "orange", "white", "purple", "green", "red"]:
           yildiz.color(colours)
           yildiz.left(100)
           yildiz.left(60)
           yildiz.forward(350)