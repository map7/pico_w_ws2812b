import machine
import socket
import network
from secrets import secrets

html = """<!DOCTYPE html>
<html>
    <head> <title>Raspberry Pi Pico W Temperature Sensor</title> <meta http-equiv=Refresh content=30></head>
    <body>
    <div class="card" style="width: 18rem;">
  <img src="https://openclipart.org/image/400px/326788" alt="DHT11 Sensor Icon">
  <div class="card-body">
    <h5 class="card-title">Live Sensor Data</h5>
    <p class="card-text">{} degrees Celsius</a>
    <p class="card-text">{} % Humidity</a>
  </div>
  </div>
    </body>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
</html>
"""

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets['ssid'],secrets['password'])
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

while True:
    cl, addr = s.accept()
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    reponse = html 
    
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(reponse)
    cl.close()