##Rewrite your pay computation with time-and-a-half for overtime
##and create a function called computepay which takes two parameters (hours and
##rate).
##Enter Hours: 45
##Enter Rate: 10
##Pay: 475.0
hrs = input('Enter hours: ')
rate = input('Enter rate: ')
def Compute_pay(hrs, rate):
    hrs = float(hrs)
    rate = float(rate)
    if hrs>40:
        Pay = 40*rate + (hrs-40)*1.5*rate
    else:
        Pay = hrs*rate
    return (Pay)
    #print (Pay)
P = Compute_pay(hrs,rate)
print(P)
