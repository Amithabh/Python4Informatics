# Exercise 5: (Advanced) Change the socket program so that it only shows data
# after the headers and a blank line have been received. Remember that recv is
# receiving characters (newlines and all), not lines.

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)
dat = " "
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    dat = dat + data.decode()
pos = dat.find("bytes")
print (dat[pos+9:])
mysock.close()

