hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
#print h, r 
if h < 40:
    Pay = h*r
else:
    Pay = 40*r + (h-40)*1.5*r
print (Pay)
