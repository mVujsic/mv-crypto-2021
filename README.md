<p align="center"> <a href="http://mfkg.rs/sr/" target="_blank"> <img src="https://github.com/mVujsic/mv-crypto-2021/blob/master/img/unnamed.png" alt="arduino" width="200" height="200"/></p>
<p align="center"><a href="https://www.python.org" target="_blank"> <img src="https://github.com/mVujsic/devicon/blob/master/icons/python/python-original.svg" alt="python" width="80" height="80"/><a href="https://www.raspberrypi.org/" target="_blank"> <img src="https://github.com/mVujsic/mv-crypto-2021/blob/master/img/Raspi-PGB001.webp" alt="raspbian" width="80" height="80"/></p>
  
# Предмет: Криптографија
### **Тема** : Асиметрична криптографија и RSA алгоритам / SenseHat примери
### **Аутор** : Матеја Вујсић

<p align="center"><a href="" target="_blank"> <img src="https://trinket-app-assets.trinket.io/sense-hat.png" alt="arduino" width="500" height="300"/></p>

### flag.py
```python
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
```
### sparcles.py
```python
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
```
### station.py
```python
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

```
