l=[]
n=int(input("Enter the size of the list"))
print("Enter the numbers")
for i in range (n):
    i=int(input())
    l.append(i)
x=0
count_odd=0
count_even=0
for x in range (n):
    if(l[x]%2==0):
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print("Count of even numbers: ",count_even)
print("Count of odd numbers: ",count_odd)
