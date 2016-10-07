# Exercise 9.2 Write a program that categorizes each mail message by which day
# of the week the commit was done. To do this look for lines that start with “From”,
# then look for the third word and keep a running count of each of the days of the
# week. At the end of the program print out the contents of your dictionary (order
# does not matter).

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
        list_add.append(list_spl[3])
for name in list_add:    
    counts[name] = counts.get(name,0)+1
print (counts)        
