n = int(input())
arr = []

for i in range(n):
    x = int(input())
    arr.append(x)

count30 = 0
count60 = 0


for i in arr:

    if i == 30:
        count30 += 1

    elif i == 60:
        count60 += 1
        if count30 > 0:
            count30 -= 1
        else:
            print("Transaction Failed")
            exit()

    elif i == 120:
        if count30 > 0 and count60 > 0:
            count30 -= 1
            count60 -= 1
        elif count30 >= 3:
            count30 -= 3
        else:
            print("Transaction Failed")
            exit()
        
print("Transaction Sucessful")