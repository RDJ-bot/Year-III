#brute
arr=[2,3,4,2,4,1,8,7,5,3]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if(arr[j]<arr[i]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr[len(arr)-1])

#Optimal
arr=[2,3,4,2,4,1,8,7,5,3]
largest = arr[0]
for i in range(len(arr)):
    if(arr[i]>largest):
        largest = arr[i]
print(largest)