a=input("Enter the month name")
a.lower()
if (a=="february"):
    n=int(input("Enter the year: "))
    if(n%400==0 or (n%4==0 and n%100!=0)):
            print("29 days")    
    else:
        print("28 days")
elif (a=="january" or a=="march" or a=="may" or a=="july" or a=="august" or a=="october" or a=="december"):
    print("31 days")
elif(a=="april" or a=="june" or a=="september" or a=="november"):
    print("30 days")
else:
    print("Enter valid option")

    
        
        
