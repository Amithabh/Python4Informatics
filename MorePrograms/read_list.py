fname = input("Enter file name: ")
fh = open(fname)
lst = list()
f_lst = list()
for line in fh:
    lst = line.split()
    for element in lst:
        if element not in f_lst:
            f_lst.append(element)
f_lst.sort()
print (f_lst)
