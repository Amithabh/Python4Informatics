import string # New Code
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print ('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    line=line.strip()
#    print (line)
    translation = str.maketrans("","", string.punctuation)
    line = line.translate(translation) # New Code
#    print (line)
    line = line.lower() # New Code
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print (counts)
