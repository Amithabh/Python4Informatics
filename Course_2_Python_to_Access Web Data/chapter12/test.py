from urllib.request import urlopen
from bs4 import *
position=int(input('Enter Position: '))
#perform the loop "count" times.
for i in range(1):
    html = urlopen("http://python-data.dr-chuck.net/known_by_Fikret.html").read()
    # print (type(html))
    soup = BeautifulSoup(html, "html.parser")
    # print (type(soup))
    tags=soup.findAll('a')
    # print (str(tags)[1])
    for tag in tags:
        url= tag.get('href')
        print (url)
        # tags=soup.findAll('a')
        # # if the link does not exist at that position, show error.
        # if not tags[position-1]:
            # print ("A link does not exist at that position.")
        # # if the link at that position exist, overwrite it so the next search will use it.
        # url = tags[position-1].get('href')
        # print (url)
    #print (url)
# print (url)