##Rewrite your pay computation to give the employee 1.5 times the
##hourly rate for hours worked above 40 hours.
##Enter Hours: 45
##Enter Rate: 10
##Pay: 475.0
hrs = input('Enter hours: ')
rate = input('Enter rate: ')
hrs = float(hrs)
rate = float(rate)
if hrs>40:
    Pay = 40*rate + (hrs-40)*1.5*rate
else:
    Pay = hrs*rate
print (Pay)
