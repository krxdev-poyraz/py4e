hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Rate per hour:")
r = float(rate)
def computepay(h,r):
    if h>40:
        pay = h*r
        afterfour = (h-40.0)*(r*0.5)
        payelse = afterfour+pay
    else:
        payelse = h*r
    return payelse
print("Pay",computepay(h,r))