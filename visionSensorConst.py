import math
h=float(input("h: "))
a=float(input("a: "))
b=float(input("a+b: "))-a
viewangle=math.atan((a+b)/h)-math.atan(a/h)
s=math.sqrt(a**2+h**2)
alpha=math.pi/2-viewangle/2
c=s*math.sin(viewangle)
beta=math.pi-alpha-math.atan(h/a)
numerator=s*c
denominator=c*math.sin(beta)/math.sin(alpha)
print(" ")
print("Numerator Constant:", numerator)
print("Denominator Constant:", denominator)
print("(bottomratio*"+str(numerator)+")/("+str(h)+"-bottomratio*"
      +str(denominator)+")+"+str(a))
print("")
print("Angle:",math.degrees(viewangle))
