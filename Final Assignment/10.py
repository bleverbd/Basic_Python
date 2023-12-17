x=int(input("Enter a integer value: "))
y=int(input("Enter a integer value: "))
z=int(input("Enter a integer value: "))
if(x>y and x>z):
    print("The Largest Number is: ",x)
elif(y>x and y>z):
    print("The Largest Number is: ",y)
else:
    print("The Largest Number is: ",z)