n=int(input("enter the number : "))
sum=0
for i in range (1,n+1):
    sum+=i%10
    i//=10
print(sum)