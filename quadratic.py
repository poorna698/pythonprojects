import math
a=int(input("enter the number1 : "))
b=int(input("enter the number2 : "))
c=int(input("enter the number3 : "))
if a==0:
    print("a not equal to zero ")
else:
    d = b**2-4*a*c
    root = math.sqrt(abs(d))
    if d>0:
        print((-b+root)/2*a,"root1")
        print((-b-root)/2*a,"root2")
    elif d==0:
        print(-b/2*a,"equal root")
    else:
        print("no roots")
        print(-b/2*a,'+i',root)
        print(-b/2*a,"-i",root)