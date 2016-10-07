# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of 
# mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who 
# sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the 
# number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary 
# using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mail = ""
counts = dict()
list_spl = list()
list_add = list()
for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        list_spl = line.split()
        #print(list_spl)
        list_add.append(list_spl[1])
for name in list_add:    
    counts[name] = counts.get(name,0)+1
email = None
freq = None    
for key,val in counts.items():
    if freq is None or val > freq:
        email = key
        freq = val
print (email, freq)        
