import tkinter as tk
import time
import threading
import math

CARS_LR = 0
CARS_UD = 0

GREEN_LR = 0
GREEN_UD = 0

YELLOW_LR = 0
YELLOW_UD = 0

RED_LR = 0
RED_UD = 0

HEIGHT = 1000
WIDTH = 1000

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="green")
canvas.pack()

caru_image = tk.PhotoImage(file='car2u.png')
card_image = tk.PhotoImage(file='car2d.png')
carr_image = tk.PhotoImage(file='car2r.png')
carl_image = tk.PhotoImage(file='car2l.png')

green_image = tk.PhotoImage(file='green.png')
red_image = tk.PhotoImage(file='red.png')
yellow_image = tk.PhotoImage(file='yellow.png')
redyel_image = tk.PhotoImage(file='redyel.png')

greenH_image = tk.PhotoImage(file='greenH.png')
redH_image = tk.PhotoImage(file='redH.png')
yellowH_image = tk.PhotoImage(file='yellowH.png')
redyelH_image = tk.PhotoImage(file='redyelH.png')

background_image = tk.PhotoImage(file='junction.png')
canvas.create_image(0, 0, image=background_image, anchor='nw')

car7d = canvas.create_image(440, -175, image=card_image, anchor='nw', tag="car7d", state='hidden')
car6d = canvas.create_image(440, -85, image=card_image, anchor='nw', tag="car6d", state='hidden')
car5d = canvas.create_image(440, 5, image=card_image, anchor='nw', tag="car5d", state='hidden')
car4d = canvas.create_image(440, 95, image=card_image, anchor='nw', tag="car4d", state='hidden')
car3d = canvas.create_image(440, 185, image=card_image, anchor='nw', tag="car3d", state='hidden')
car2d = canvas.create_image(440, 275, image=card_image, anchor='nw', tag="car2d", state='hidden')
car1d = canvas.create_image(440, 365, image=card_image, anchor='nw', tag="car1d", state='hidden')

car7u = canvas.create_image(480, 1085, image=caru_image, anchor='nw', tag="car7u", state='hidden')
car6u = canvas.create_image(480, 995, image=caru_image, anchor='nw', tag="car6u", state='hidden')
car5u = canvas.create_image(480, 905, image=caru_image, anchor='nw', tag="car5u", state='hidden')
car4u = canvas.create_image(480, 815, image=caru_image, anchor='nw', tag="car4u", state='hidden')
car3u = canvas.create_image(480, 725, image=caru_image, anchor='nw', tag="car3u", state='hidden')
car2u = canvas.create_image(480, 635, image=caru_image, anchor='nw', tag="car2u", state='hidden')
car1u = canvas.create_image(480, 545, image=caru_image, anchor='nw', tag="car1u", state='hidden')

car7r = canvas.create_image(-175, 480, image=carr_image, anchor='nw', tag="car7r", state='hidden')
car6r = canvas.create_image(-85, 480, image=carr_image, anchor='nw', tag="car6r", state='hidden')
car5r = canvas.create_image(5, 480, image=carr_image, anchor='nw', tag="car5r", state='hidden')
car4r = canvas.create_image(95, 480, image=carr_image, anchor='nw', tag="car4r", state='hidden')
car3r = canvas.create_image(185, 480, image=carr_image, anchor='nw', tag="car3r", state='hidden')
car2r = canvas.create_image(275, 480, image=carr_image, anchor='nw', tag="car2r", state='hidden')
car1r = canvas.create_image(365, 480, image=carr_image, anchor='nw', tag="car1r", state='hidden')

car7l = canvas.create_image(1085, 440, image=carl_image, anchor='nw', tag="car7l", state='hidden')
car6l = canvas.create_image(995, 440, image=carl_image, anchor='nw', tag="car6l", state='hidden')
car5l = canvas.create_image(905, 440, image=carl_image, anchor='nw', tag="car5l", state='hidden')
car4l = canvas.create_image(815, 440, image=carl_image, anchor='nw', tag="car4l", state='hidden')
car3l = canvas.create_image(725, 440, image=carl_image, anchor='nw', tag="car3l", state='hidden')
car2l = canvas.create_image(635, 440, image=carl_image, anchor='nw', tag="car2l", state='hidden')
car1l = canvas.create_image(545, 440, image=carl_image, anchor='nw', tag="car1l", state='hidden')

light1V = canvas.create_image(550, 600, image=green_image, anchor='nw', tag="light1V")
light2V = canvas.create_image(430, 350, image=green_image, anchor='nw', tag="light2V")
light1H = canvas.create_image(390, 550, image=greenH_image, anchor='nw', tag="light1H")
light2H = canvas.create_image(560, 430, image=greenH_image, anchor='nw', tag="light1H")


def move_up_down():
    for y in range(0, 300):
        canvas.move(car1d, 0, 3)
        canvas.move(car1u, 0, -3)
        if y > 10:
            canvas.move(car1d, 0, 3)
            canvas.move(car2d, 0, 3)
            canvas.move(car1u, 0, -3)
            canvas.move(car2u, 0, -3)
        if y > 20:
            canvas.move(car2d, 0, 3)
            canvas.move(car3d, 0, 3)
            canvas.move(car2u, 0, -3)
            canvas.move(car3u, 0, -3)
        if y > 30:
            canvas.move(car3d, 0, 3)
            canvas.move(car4d, 0, 3)
            canvas.move(car3u, 0, -3)
            canvas.move(car4u, 0, -3)
        if y > 40:
            canvas.move(car4d, 0, 3)
            canvas.move(car5d, 0, 3)
            canvas.move(car4u, 0, -3)
            canvas.move(car5u, 0, -3)
        if y > 50:
            canvas.move(car5d, 0, 3)
            canvas.move(car5u, 0, -3)
            canvas.move(car6d, 0, 3)
            canvas.move(car6u, 0, -3)
        if y > 60:
            canvas.move(car7d, 0, 3)
            canvas.move(car7u, 0, -3)
            canvas.move(car6d, 0, 3)
            canvas.move(car6u, 0, -3)
        if y > 70:
            canvas.move(car7d, 0, 3)
            canvas.move(car7u, 0, -3)
        root.update()
        time.sleep(0.01)


def move_right_left():
    for z in range(0, 300):
        canvas.move(car1r, 3, 0)
        canvas.move(car1l, -3, 0)
        if z > 10:
            canvas.move(car1r, 3, 0)
            canvas.move(car2r, 3, 0)
            canvas.move(car1l, -3, 0)
            canvas.move(car2l, -3, 0)
        if z > 20:
            canvas.move(car2r, 3, 0)
            canvas.move(car3r, 3, 0)
            canvas.move(car2l, -3, 0)
            canvas.move(car3l, -3, 0)
        if z > 30:
            canvas.move(car3r, 3, 0)
            canvas.move(car4r, 3, 0)
            canvas.move(car3l, -3, 0)
            canvas.move(car4l, -3, 0)
        if z > 40:
            canvas.move(car4r, 3, 0)
            canvas.move(car5r, 3, 0)
            canvas.move(car4l, -3, 0)
            canvas.move(car5l, -3, 0)
        if z > 50:
            canvas.move(car5r, 3, 0)
            canvas.move(car5l, -3, 0)
            canvas.move(car6r, 3, 0)
            canvas.move(car6l, -3, 0)
        if z > 60:
            canvas.move(car7r, 3, 0)
            canvas.move(car7l, -3, 0)
            canvas.move(car6r, 3, 0)
            canvas.move(car6l, -3, 0)
        if z > 70:
            canvas.move(car7r, 3, 0)
            canvas.move(car7l, -3, 0)
        root.update()
        time.sleep(0.01)



def thread1():
    global CARS_LR, CARS_UD, RED_LR, YELLOW_LR, GREEN_LR, RED_UD, YELLOW_UD, GREEN_UD



    while True:

        time.sleep(10)
        CARS_UD = 6
        CARS_LR = 4
        RED_UD=0
        RED_LR = 1
        GREEN_LR = 0
        GREEN_UD=1



        time.sleep(10)
        CARS_UD = 10
        CARS_LR = 12
        RED_UD = 1
        RED_LR = 0
        GREEN_UD = 0
        GREEN_LR = 1





def read_data():
    #socket
    #msg = read_message

    return


def prepare_rl():
    global CARS_LR, RED_LR, YELLOW_LR, GREEN_LR, RED_UD, YELLOW_UD, GREEN_UD

    # cleaning
    for z in range(1, 8):
        canvas.itemconfigure("car" + str(z) + "r", state='hidden')
        canvas.itemconfigure("car" + str(z) + "l", state='hidden')

        canvas.coords(cars_right[z - 1], 365 - (z - 1) * 90, 480)
        canvas.coords(cars_left[z - 1], 545 + (z - 1) * 90, 440)

    for i in range(min(CARS_LR+1, 15)):
        if i % 2 == 0:
            print("car" + str(math.floor((i + 2) / 2)) + "r")
            canvas.itemconfigure("car" + str(math.floor((i + 1) / 2)) + "r", state='normal')
        if i % 2 == 1:
            print("car" + str(math.floor((i + 1) / 2)) + "l")
            canvas.itemconfigure("car" + str(math.floor((i + 1) / 2)) + "l", state='normal')
    CARS_LR = 0

    root.update()


def prepare_ud():
    global CARS_UD, RED_LR, YELLOW_LR, GREEN_LR, RED_UD, YELLOW_UD, GREEN_UD
    for y in range(1, 8):
        canvas.itemconfigure("car" + str(y) + "d", state='hidden')
        canvas.itemconfigure("car" + str(y) + "u", state='hidden')

        canvas.coords(cars_down[y - 1], 440, 365 - (y - 1) * 90)
        canvas.coords(cars_up[y - 1], 480, 545 + (y - 1) * 90)

    for i in range(min(CARS_UD+1, 15)):
        if i % 2 == 0:
            print("car" + str(math.floor((i + 2) / 2)) + "u")
            canvas.itemconfigure("car" + str(math.floor((i + 1) / 2)) + "u", state='normal')
        if i % 2 == 1:
            print("car" + str(math.floor((i + 1) / 2)) + "d")
            canvas.itemconfigure("car" + str(math.floor((i + 1) / 2)) + "d", state='normal')
    CARS_UD = 0
    root.update()



def main():
    global CARS_LR, CARS_UD, GREEN_LR, GREEN_UD, YELLOW_LR, YELLOW_UD, RED_LR, RED_UD

    while True:

        if (RED_UD == 1 and YELLOW_UD==1):
            canvas.itemconfigure("light1V", image=redyel_image)
            canvas.itemconfigure("light2V", image=redyel_image)
        elif(RED_UD==1):
            canvas.itemconfigure("light1V", image=red_image)
            canvas.itemconfigure("light2V", image=red_image)
        elif (YELLOW_UD == 1):
            canvas.itemconfigure("light1V", image=yellow_image)
            canvas.itemconfigure("light2V", image=yellow_image)

        if (RED_LR == 1 and YELLOW_LR == 1):
            canvas.itemconfigure("light1H", image=redyelH_image)
            canvas.itemconfigure("light2H", image=redyelH_image)
        elif (RED_LR == 1):
            canvas.itemconfigure("light1H", image=redH_image)
            canvas.itemconfigure("light2H", image=redH_image)
        elif (YELLOW_LR == 1):
            canvas.itemconfigure("light1H", image=yellowH_image)
            canvas.itemconfigure("light2H", image=yellowH_image)

        if(GREEN_UD==1):
            canvas.itemconfigure("light1V", image=green_image)
            canvas.itemconfigure("light2V", image=green_image)
            move_up_down()
            prepare_rl()
            GREEN_UD = 0
        if(GREEN_LR==1):
            canvas.itemconfigure("light1H", image=greenH_image)
            canvas.itemconfigure("light2H", image=greenH_image)
            move_right_left()
            prepare_ud()
            GREEN_LR = 0

        root.update()





t = threading.Thread(target=thread1, args=())
t.start()



cars_down = [car1d, car2d, car3d, car4d, car5d, car6d, car7d]
cars_up = [car1u, car2u, car3u, car4u, car5u, car6u, car7u]
cars_left = [car1l, car2l, car3l, car4l, car5l, car6l, car7l]
cars_right = [car1r, car2r, car3r, car4r, car5r, car6r, car7r]


main()

root.mainloop()
