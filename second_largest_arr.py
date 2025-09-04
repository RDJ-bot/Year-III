#brute
'''
arr=[1,3,5,7,9,9,4]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if(arr[j]<arr[i]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)
num = len(arr)
largest = arr[num-1]
for k in range(num-1,-1,-1):
    if(arr[k]!=largest):
        print("Second is : ",arr[k])
        break
'''

'''
#better
arr1 = [2,4,6,8,6,5,7]
largest = arr1[0]
for i in range(len(arr1)):
    if(arr1[i]>largest):
        largest = arr1[i]

second_largest = 0
for j in range(len(arr1)):
    if(arr1[j]>second_largest and arr1[j]<largest):
        second_largest = arr1[j]
print(second_largest)
'''

#optimal
arr = [1,2,4,7,7,5]
first_largest = 0
second_largest = -1

for i in range(len(arr)):
    if(arr[i]>first_largest):
        print(arr[i])
        second_largest = first_largest 
        first_largest = arr[i]
        print("First : ",first_largest)
        print("Second",second_largest)
    elif(arr[i]<first_largest and arr[i]>second_largest):
        second_largest = arr[i]
        print("Second_largest = ",second_largest)
print("Second largest : ",second_largest)