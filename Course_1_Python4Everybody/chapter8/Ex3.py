##Write a function that takes a list and returns a new list that
##contains all but the first and last elements.
mylist = [1,2,3,4]
def Using_del(mylist):
    leng = len(mylist)
    del mylist[leng-1]
    del mylist[0]
    return mylist
print (Using_del(mylist))
