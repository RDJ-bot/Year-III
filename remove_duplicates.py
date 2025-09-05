arr = [1,2,2,2,3,3,4,5,5]
arr1=[]
dupe=[]

for num in arr:
    if num not in arr1:
        arr1.append(num)
    elif num in arr1 and num not in dupe:
        dupe.append(num)

print("Unique elements = ",arr1)
print("Duplicate elements = ",dupe)