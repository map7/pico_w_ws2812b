#Example 1 - Control individual LED

from neopixel import Neopixel
import utime

numpix = 5
strip = Neopixel(numpix, 0, 28, "RGB")
delay = 0.5
strip.brightness(50)

while True:
    strip.set_pixel(0, (0,255,0))
    strip.show()
    utime.sleep(delay)
    strip.fill((0,0,0))
    
    
        
          



