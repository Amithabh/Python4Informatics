# Exercise 10.1 Revise a previous program as follows: Read and parse the “From”
# lines and pull out the addresses from the line. Count the number of messages from
# each person using a dictionary.
# After all the data has been read, print the person with the most commits by creating
# a list of (count, email) tuples from the dictionary. Then sort the list in reverse order
# and print out the person who has the most commits.

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
        list_add.append(line_spl[1])
for name in list_add:    
    counts[name] = counts.get(name,0)+1
tmp = list()   
for k,v in counts.items():
    tmp.append((v, k))
tmp.sort(reverse = True)
tup = tmp[0]
print (tup[1],tup[0])
