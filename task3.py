print("Enter the size of the list:")
n=int(input())
list=[]
for i in range(n):
    i=input("")
    list.append(i)
    list.sort()

a=list[0]
for x in range (n):
    if(len(list[x])>len(a)):
        a=list[x]

print("The largest element is "+a)
    
    
