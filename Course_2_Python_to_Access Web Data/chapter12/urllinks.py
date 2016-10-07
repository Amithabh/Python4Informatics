# The program prompts for a web address, then opens the web page, reads the data
# and passes the data to the BeautifulSoup parser, and then retrieves all of the
# anchor tags and prints out the href attribute for each tag.


# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4
# Or download the file
# http://www.pythonlearn.com/code3/bs4.zip
# and unzip it in the same directory as this file
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
# Code: http://www.pythonlearn.com/code3/urllinks.py