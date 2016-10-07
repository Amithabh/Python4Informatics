#9.4 Write a program to read through the mbox-short.txt and figure out who has
##the sent the greatest number of mail messages. The program looks
##for 'From ' lines and takes the second word of those lines as the person who
##sent the mail. The program creates a Python dictionary that maps the
##sender's mail address to a count of the number of times they appear in the
##file. After the dictionary is produced, the program reads through the dictionary
##using a maximum loop to find the most prolific committer.


##print ( max(counts, key=lambda k: counts[k]))
###print(max(zip(counts.values(),counts.keys())))

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
lst = list()
new_lst = list()
for line in handle:
    if line.startswith('From ') and not line.startswith('From:') :
        lst = line.split()
        new_lst.append(lst[1])
for i in new_lst:  
    counts[i] = counts.get(i,0) + 1
bigword = None
bigcount = -1
for key, value in counts.items():
    if value > bigcount:
        bigword = key
        bigcount = value
print (bigword, bigcount)
    
