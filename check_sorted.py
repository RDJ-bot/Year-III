arr=[1,2,3,4,4,5,6,6,7]
count = 0
for i in range(len(arr)-1):
    if(arr[i]>arr[i+1]):
        print("Not sorted")
        count=1
        break
if(count!=1):
    print("Not sorted")