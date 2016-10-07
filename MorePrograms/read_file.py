# Use words.txt as the file name
fname = input("Enter file name: ")
fhandle = open(fname)
inp = fhandle.read()
inp = inp.strip()
upper_case = inp.upper()
print (upper_case)
