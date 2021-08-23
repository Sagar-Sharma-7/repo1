n1=int(input("enter number="))
n2=int(input("enter number="))
while n1%n2!=0:
    r=n1%n2
    n1=n2
    n2=r
print("hcf=",r)
