#Author: Mateja Vujsic 

from sense_hat import SenseHat
import random as rnd
import time
import sys

box = SenseHat()
box.clear()

rgb = (0,0,0)
position_x = 0
position_y = 0

try:
    while True:
        
       box.set_pixel(position_x, position_y, rgb)
       
       rgb = (rnd.randint(0,255), rnd.randint(0,255), rnd.randint(0,255))

       position_x = rnd.randint(0,7)
       position_y = rnd.randint(0,7)

       box.set_pixel(position_x, position_y, rgb)
       
       time.sleep(0.1)
       box.clear()
       
except KeyboardInterrupt:
    print("The End..")
    
    box.clear()
    pass
   
   
