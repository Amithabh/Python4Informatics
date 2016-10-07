##Rewrite your pay program using try and except so that your program
##handles non-numeric input gracefully by printing a message and exiting the
##program. The following shows two executions of the program:
##Enter Hours: 20
##Enter Rate: nine
##Error, please enter numeric input
##Enter Hours: forty
##Error, please enter numeric input    
hrs = input('Enter hours: ')
rate = input('Enter rate: ')
try:
    hrs = float(hrs)
    rate = float(rate)
    if hrs>40:
        Pay = 40*rate + (hrs-40)*1.5*rate
    else:
        Pay = hrs*rate
    print (Pay)
except:
    print('Error, please enter numeric input')

