arr = [1,2,0,2,0,1,3,0,4]
start = 0

for i in range(len(arr)):
    if arr[i] == 0:
        start = i
        break
    
j = start + 1
while j < len(arr):
    if arr[j] != 0:
        arr[j],arr[start] = arr[start],arr[j]
        start += 1
        j += 1
    else:
        j += 1

print(arr)

