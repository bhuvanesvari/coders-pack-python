a=float(input("Enter the first side"))
b=float(input("Enter the second side"))
c=float(input("Enter the third side"))
if(a==b and a==c):
    print("Equilateral triangle")
elif(a==b or a==c or b==c):
    print("Isosceles triangle")
else:
    print("Scalene triangle")
    
