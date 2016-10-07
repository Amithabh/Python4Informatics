import re
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
reg = input("Enter a regex: \n")
for line in handle:
    if re.search(reg, line):
        print (line)