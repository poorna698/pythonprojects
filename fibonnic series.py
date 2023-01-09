n=int(input("enter the number :"))
n1,n2=0,1
print("Fibonacci Series:", n1,",", n2, end=" , ")
for i in range (2,n):
    nth=n1+n2
    n1=n2
    n2=nth
    print(nth,end="  ")