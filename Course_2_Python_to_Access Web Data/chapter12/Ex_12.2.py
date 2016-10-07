# Exercise 2: Change your socket program so that it counts the number of characters
# it has received and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of
# characters and display the count of the number of characters at the end of the
# document.

import socket
name = input("Enter url:")
mysock_con = name.split("/")
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((mysock_con[2], 80))
cmd_name = "GET " + name + " HTTP/1.0\n\n"
cmd = cmd_name.encode()
mysock.send(cmd)
data_add = ""
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    data_add = data_add + data.decode()
    if len(data_add) > 3000:
        break        
print (data_add)   
print ("Number of characters: ", len(data_add))
mysock.close()