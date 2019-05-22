l=[]
n=int(input("Enter the size of the list"))
print("Enter the numbers")
for i in range (n):
    i=int(input())
    l.append(i)
m=1
for x in range(n):
    m=m*l[x]
print("Product",m)
