#Example 1 - Control individual LED

from neopixel import Neopixel
import utime
import random
import gc

numpix = 5
strip = Neopixel(numpix, 0, 28, "RGB")

# GRB
green = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
red = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)
colors_rgb = [red, orange, yellow, green, blue, indigo, violet]

delay = 0.5
strip.brightness(50)
blank = (0,0,0)

while True:
    
    strip.set_pixel(0, red)
    strip.show()

    utime.sleep(delay)
    strip.set_pixel(1, red)
    strip.show()
    
    utime.sleep(delay)
    strip.set_pixel(2, red)
    strip.show()

    utime.sleep(delay)
    strip.set_pixel(3, red)
    strip.show()

    utime.sleep(delay)
    strip.set_pixel(4, red)
    strip.show()
    utime.sleep(delay)
    strip.fill((0,0,0))
    
    
        
          



