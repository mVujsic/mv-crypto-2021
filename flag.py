#Author: Mateja
#Description : name letter by letter

from sense_hat import SenseHat
from time import sleep
import random

rgb=[(255,0,0),(0,0,255),(255,255,255)]

sh = SenseHat()
sh.clear()

counter = 0

for i in "MatejaVujsic6172017":
        counter = counter % 3

        sh.clear()
        sh.show_letter(i,text_colour=rgb[counter])
        
        sleep(1)
        counter+=1

try:
    while True:
        sh.clear(rgb[0])
        sleep(1)

        sh.clear(rgb[1])
        sleep(1)

        sh.clear(rgb[2])
        sleep(1)

except KeyboardInterrupt:
        sh.clear()
    
        


