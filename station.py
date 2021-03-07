#Author: Mateja
#Description: Weather station - eface terminal

from sense_hat import SenseHat
import time
import random as rnd

box =  SenseHat()
box.set_rotation(90)


def welcomeMessage():
    box.show_message("Dobrodosli!",text_colour=(255,0,0))
    box.clear()

def getTemp():
    current = str(round(box.get_temperature(),2))
    print("Trenutna temperatura je: "+ current +" stepeni." )
    box.show_message(current + "C")
    box.clear()

def getHum():
    current = str(round(box.get_humidity(),2))
    print("Trenutna vlaznost vazduha je: "+ current +" stepeni." )
    box.show_message(current + "%")
    box.clear()
    

welcomeMessage()
box.stick.direction_up = getTemp
box.stick.direction_down = getHum
box.clear()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nKraj programa")
    box.clear()

 