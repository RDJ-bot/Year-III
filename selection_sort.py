n = int(input("Enter the number of elements : "))
arr=[]
for i in range(0,n):
    x=int(input())
    arr.append(x)

for i in range(n-1):
    min = i
    for j in range(i,n):
        if(arr[j]<arr[min]):
            temp = arr[min]
            arr[min] = arr[j]
            arr[j] = temp
print(arr)