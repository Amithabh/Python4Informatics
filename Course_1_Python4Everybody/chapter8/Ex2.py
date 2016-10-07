##Write a function called middle that takes a list and returns a new list that
##contains all but the first and last elements.
mylist = [1,2,3,4]
def middle(mylist):
    leng = len(mylist)
    mylist.pop(leng-1)
    mylist.pop(0)
    return mylist
print (middle(mylist))
