x = int(input('enter the number :'))
y = int(input('enter the number :'))

if (x>0 and y>0):
    print("first")
elif (x<0 and y>0):
    print("second")
elif (x<0 and y<0):
    print("third")
else:
    print("fourth")