
from graphics import *

win = GraphWin("Окно для графики", 1010,1110)
image = "mapc2XL.png"
myImage = Image(Point(1010/2-4,1110/2-4),image)
myImage.draw(win)

for i in range(0,1010):
    for j in range(0,1110):
        if (i-4) % 10 ==0 and (j-4) % 10 ==0:
            c = Point(i,j)
            c.draw(win)



room = 1
i = 0
def b1(event):


    print(room,":",end=" ")
    print((event.x-4)//10+1,end=" ")
    print((event.y-4)//10+1)





win.bind('<Button-1>', b1)


win.getMouse()
win.close()