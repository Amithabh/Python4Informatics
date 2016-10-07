# If the audio or video file is large , curl1.py program may crash or at least
# run extremely slowly when your computer runs out of memory. In order to avoid
# running out of memory, we retrieve the data in blocks (or buffers) and then write
# each block to your disk before retrieving the next block. This way the program can
# read any size file without using up all of the memory you have in your computer.

import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://data.pr4e.org/cover.jpg')
fhand = open('cover.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)
    print(size, 'characters copied.')
fhand.close()
# Code: http://www.pythonlearn.com/code3/curl2.py