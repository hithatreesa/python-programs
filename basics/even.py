a=int(input("Enter a number"))
b= int(input("enter a number"))
if a % 2 == 0 and b % 2 == 0:
    print("a and b are even")
elif a % 2!= 0 and b % 2 == 0:
    print("a is odd and b is even")
else:
    print("a or b is even")