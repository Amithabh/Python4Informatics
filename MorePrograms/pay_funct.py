def computepay(h,r):
    if h < 40:
        Pay = h*r
    else:
        Pay = 40*r + (h-40)*1.5*r
    return Pay

hrsin = input("Enter Hours: ")
hrs = float(hrsin)
ratein = input("Enter rate: ")
rate = float(ratein)
p = computepay(hrs,rate)
print (p)
