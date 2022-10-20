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
    cl, addr = s.accept()
    cl_file = cl.makefile('rwb', 0)
        
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    
    response = html 
    
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()