a=int(input("Enter the first value "))
b=int(input("Enter the second value "))
c=int(input("Enter the third value "))
if((a>=b and a<=c)or(a>=c and a<=b)):
    print(a,"is the median")
elif((b>=c and b<=a)or(b<=c and b>=a)):
    print(b," is the median")
else:
    print(c," is the median")
    
    
