n1=float(input("enter marks in english:"))
n2=float(input("enter marks in hindi:"))
n3=float(input("enter marks in maths:"))
n4=float(input("enter marks in science:"))
n5=float(input("enter marks in sst:"))
per=(n1+n2+n3+n4+n5)/5
if per >=85:
    print("A grade")
elif per>=75:
    print("B grade")
elif per>=50:
    print("C grade")
elif per>=30:
    print("D grade")
else:
    print("reappear")
print("your percentage is:",per)

