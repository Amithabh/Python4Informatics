# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of 
# the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second 
# time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
list_spl = list()
list_add = list()
for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        line_spl = line.split()
        line_spl1 = line_spl[5]
        list_add.append(line_spl1[:2])
for name in list_add:    
    counts[name] = counts.get(name,0)+1
tmp = list()   
for k,v in counts.items():
    tmp.append((k, v))
tmp.sort()
for item in tmp:
    print (item[0],item[1])
