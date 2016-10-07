# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the
# document from a URL, (2) displaying up to 3000 characters, and (3) counting the
# overall number of characters in the document. Don’t worry about the headers for
# this exercise, simply show the first 3000 characters of the document contents.

import urllib.request, urllib.parse, urllib.error
name = input("Enter url:")
fhand = urllib.request.urlopen(name)
text = ""
for line in fhand:
    text = text + line.decode()
    if len(text) > 3000:
        break        
print (text)  
text = text.strip() 
print ("Number of characters: ", len(text))
