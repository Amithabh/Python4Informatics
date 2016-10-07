# Exercise 9.3 Write a program to read through a mail log, build a histogram using
# a dictionary to count how many messages have come from each email address,
# and print the dictionary.

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
print (counts)        
