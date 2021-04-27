'''
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.

#from graphics import *


w = 101 * 5
h = 111 * 5


image = Image.open("map.png") #Открываем изображение.
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
width = image.size[0]  # Определяем ширину.
height = image.size[1]  # Определяем высоту.
pix = image.load()  # Выгружаем значения пикселей.

filew = open("map.txt","w")
filew.write(str(width)+"\n")
filew.write(str(height)+"\n")

for i in range(0, height-1):
    for j in range(0, width-1):
       # print(pix[i,j])

        if pix[j,i]==(255,255,255,255):
            celcol = 0
        elif pix[j,i]==(0,0,0,255):
            celcol = 1
        elif pix[j,i]==(0,255,0,255):
            celcol = 3
        elif pix[j,i]==(0,0,255,255):
            celcol = 4
        else:
            celcol = 1


        filew.write(str(celcol))
    filew.write('\n')



'''
'''
win = GraphWin("Окно для графики", w,h)
image = "map.png"
myImage = Image(Point(w/2,h/2),image)
myImage.draw(win)
c = Rectangle(Point(105,55),Point(150,450))
#c = Rectangle(Point(4,4),Point(297,893))
c.setFill("Green")

c.draw(win)

win.getMouse()
win.close()


'''
from graphics import *

win = GraphWin("Окно для графики", 1010,1110)
image = "src/mapNXL.png"
myImage = Image(Point(1010/2-4,1110/2-4),image)
myImage.draw(win)

for i in range(0,1010):
    for j in range(0,1110):
        if (i-4) % 10 ==0 and (j-4) % 10 ==0:
            c = Point(i,j)
            c.draw(win)



room = 1
f = open('text.txt', 'w')
f.write("0")
f.close()
def b1(event):
    f = open('text.txt', 'r')
    k = int(f.read())
    f = open('text.txt', 'w')
    f.write(str(k+1))
    f.close()


    print(k+1,":",end=" ")
    print((event.x-4)//10+1,end=" ")
    print((event.y-4)//10+1)





win.bind('<Button-1>', b1)


win.getMouse()
win.close()