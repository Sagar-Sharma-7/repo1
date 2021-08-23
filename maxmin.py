n1=int(input("enter 1st number="))
n2=int(input("enter 2nd number="))
n3=int(input("enter 3rd number="))
min=n1
m=n1
if n2<min:
    min=n2
if n3<min:
    min=n3
if n2>m:
    m=n2
if n3>m:
    n3=m
print("max=",m,"min=",min)
