hrs = input("Enter Hours:")
h = float(hrs)
rate_per_hr = input ("Rate per Hour:")
rph = float(rate_per_hr)
if h>40:
    pay = h*rph
    afterfour = (h-40.0)*(rph*0.5)
    payelse = afterfour+pay
else:
    payelse = h*rph
print(payelse)