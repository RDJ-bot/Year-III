#brook
num = int(input("Enter a number : "))
count = 0
for i in range(1,num+1):
    if(num%i==0):
        count+=1
if(count>2):
    print("Not a prime")
else:
    print("Prime")


#better
num = int(input("Enter a number : "))
if (num<2):
    print("Not a prime number")
else:
    for i in range(2,num):
        if(num%i == 0):
            print("Not a prime number")
            break
    else:
        print("Prime number")


#optimal
import math
num = int(input("Enter a number : "))
if(num<2):
    print("Not a prime number")
else:
    for i in range(2,int(math.sqrt(num))+1):
        if(num%i == 0):
            print("Not a prime")
            break
    else:
        print("Prime number")