##Write another program that prompts for a list of numbers as above
##and at the end prints out both the maximum and minimum of the numbers instead
##of the average.
count = 0
total = 0
max_num = None
min_num = None
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        print (count, max_num, min_num)
        break
    try:
        inp = float(inp)
        count = count + 1
        if max_num is None or inp > max_num:
            max_num = inp
        if min_num is None or inp < min_num:
            min_num = inp
    except:
        print ('Invalid input')
        continue
