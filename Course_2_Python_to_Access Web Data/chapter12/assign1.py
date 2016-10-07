import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send(b'GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print (data);

mysock.close()

# Output:
# b'HTTP/1.1 200 OK\r\n
# Content-Type: text/plain\r\n
# Content-Length: 467\r\n
# Connection: close\r\n
# Date: Sun, 31 Jul 2016 10:57:06 GMT\r\n
# Server: Apache\r\n
# Last-Modified: Mon, 12 Oct 2015 14:55:29 GMT\r\n
# ETag: "20f7401b-1d3-521e9853a392b"\r\n
# Accept-Ranges: bytes\r\n
# Cache-Control: max-age=604800, public\r\n
# Access-Control-Allow-Origin: *\r\n
# Access-Control-Allow-Headers: origin, x-requested-with, content-type\r\n
# Access-Control-Allow-Methods: GET\r\n\r\n
# Why should you learn to write programs?\n\n
# Writing programs (or programming) is a very creative 'b'\n
# and rewarding activity.  You can write programs for \n
# many reasons, ranging from making your living to solving\n
# a difficult data analysis problem to having fun to helping\n
# someone else solve a problem.  This book assumes that \n
# everyone needs to know how to program, and that once \n
# you know how to program you will figure out what you want \n
# to do with your newfound skills.  \n'