# Exercise 9.5 This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came from (i.e., the
# whole email address). At the end of the program, print out the contents of your
# dictionary.

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
        line_spl = line.split()
        line_spl1 = line_spl[1]
        line_spl2 = line_spl1.split("@")
        list_add.append(line_spl2[1])
for name in list_add:    
    counts[name] = counts.get(name,0)+1
print (counts)        
