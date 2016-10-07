largest = -1
smallest = 9999
while True:
    num = input("Enter a number: ")
    try:
        val = int(num)
        if val > largest:
            largest = val
        if val < smallest:
            smallest = val
    except ValueError:
        print("Invalid input")
        if num == "done" : break
print ("Maximum is", largest)
print ("Minimum is", smallest)
