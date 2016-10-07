##Rewrite the program that prompts the user for a list of numbers and
##prints out the maximum and minimum of the numbers at the end when the user
##enters “done”. Write the program to store the numbers the user enters in a list
##and use the max() and min() functions to compute the maximum and minimum
##numbers after the loop completes.
##Enter a number: 6
##Enter a number: 2
##Enter a number: 9
##Enter a number: 3
##Enter a number: 5
##Enter a number: done
##Maximum: 9.0
##Minimum: 2.0
max_list = list()
min_list = list()
max_num = None
min_num = None
while True: 
    inp = input('Enter a number: ')
    if inp=='done': break
    inp = float(inp)
    if max_num == None or inp > max_num:
        max_list.append(inp)
    if min_num == None or inp < min_num:
        min_list.append(inp)
#print (max_list)
maximum = max(max_list)
minimum = min(min_list)
print ('Maximum: ', maximum,'\n' 'Minimum: ',minimum)

