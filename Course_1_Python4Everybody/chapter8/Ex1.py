##Write a function called chop that takes a list and modifies it, removing
##the first and last elements, and returns None.
mylist = [1,2,3,4]
def chop(mylist):
    leng = len(mylist)
    mylist.pop(leng-1)
    mylist.pop(0)
print (chop(mylist))
