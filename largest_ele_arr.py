#optimal
arr = [4,5,6,4,2,6,5,8,9]
largest = arr[0]
for i in range(len(arr)):
    if(arr[i]>largest):
        largest = arr[i]
print(largest)