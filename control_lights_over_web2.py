# Ref: https://www.tomshardware.com/how-to/get-wi-fi-internet-on-raspberry-pi-pico
# Ref: https://core-electronics.com.au/guides/raspberry-pi-pico-w-create-a-simple-http-server/
import socket
import network
from secrets import secrets # Create secrets.py only on the PICO
from neopixel import Neopixel
import utime

# Setup neopixels
numpix = 5
strip = Neopixel(numpix, 0, 28, "RGB")
delay = 0.5
strip.brightness(50)

# html page
html ="""
<html>
    <head>
    <title>Raspberry Pi Pico W Neopixel</title>
    <meta http-equiv=Refresh content=30>
    </head>
    
    <body>
    <h1>NeoPixel Control</h1>
    
    <form>
        <button name="led0on" value="on" type=submit>Button 0 on</button>
        <button name="led1on" value="on" type=submit>Button 1 on</button>
        <button name="led2on" value="on" type=submit>Button 2 on</button>
        <button name="led3on" value="on" type=submit>Button 3 on</button>
        <button name="led4on" value="on" type=submit>Button 4 on</button>
        <br />
        <button name="led0off" value="off" type=submit>Button 0 off</button>
        <button name="led1off" value="off" type=submit>Button 1 off</button>
        <button name="led2off" value="off" type=submit>Button 2 off</button>
        <button name="led3off" value="off" type=submit>Button 3 off</button>
        <button name="led4off" value="off" type=submit>Button 4 off</button>
    </form>
    
    </body>
</html>
"""

# Connect to WIFI
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets['ssid'],secrets['password'])

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)
    
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('Connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

# Setup listening address
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)
print('listening on', addr)

while True:
    try:
        cl, addr = s.accept()
        cl_file = cl.makefile('rwb', 0)
        request = cl.recv(1024)
        print("request:")
        print(request)
        request = str(request)
        led0on= request.find('led0on')
        led0off= request.find('led0off')
        led1on= request.find('led1on')
        led1off= request.find('led1off')
        led2on= request.find('led2on')
        led2off= request.find('led2off')
        led3on= request.find('led3on')
        led3off= request.find('led3off')
        led4on= request.find('led4on')
        led4off= request.find('led4off')
        
        print('led0on = ' + str(led0on))
        print('led0off = ' + str(led0off))
        
        if led0on == 8:
            print("LED0 ON")
            strip.set_pixel(0, (0,255,0))
            strip.show()            
        elif led0off == 8:
            print("LED0 OFF")
            strip.set_pixel(0, (0,0,0))
            strip.show()
            
        elif led1on == 8:
            print("LED1 ON")
            strip.set_pixel(1, (0,255,0))
            strip.show()            
        elif led1off == 8:
            print("LED1 OFF")
            strip.set_pixel(1, (0,0,0))
            strip.show()
            
        elif led2on == 8:
            print("LED2 ON")
            strip.set_pixel(2, (0,255,0))
            strip.show()            
        elif led2off == 8:
            print("LED2 OFF")
            strip.set_pixel(2, (0,0,0))
            strip.show()
        elif led3on == 8:
            print("LED3 ON")
            strip.set_pixel(3, (0,255,0))
            strip.show()            
        elif led3off == 8:
            print("LED3 OFF")
            strip.set_pixel(3, (0,0,0))
            strip.show()
        elif led4on == 8:
            print("LED4 ON")
            strip.set_pixel(4, (0,255,0))
            strip.show()            
        elif led4off == 8:
            print("LED4 OFF")
            strip.set_pixel(4, (0,0,0))
            strip.show()
        
        response = html 
        
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
        
    except OSError as e:
        cl.close()
        print("Connection closed")