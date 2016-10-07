# This program reads all of the data in at once across the network and stores it in the
# variable img in the main memory of your computer, then opens the file cover.jpg
# and writes the data out to your disk. This will work if the size of the file is less
# than the size of the memory of your computer.

import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('http://data.pr4e.org/cover.jpg').read()
fhand = open('cover.jpg', 'wb')
fhand.write(img)
fhand.close()
# Code: http://www.pythonlearn.com/code3/curl1.py