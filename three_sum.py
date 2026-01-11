arr = [-1,0,1,2,-1,-4]
n = len(arr)
ans = set()

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if(arr[i] + arr[j] + arr[k] == 0):
                temp = [arr[i],arr[j],arr[k]]
                temp.sort()
                ans.add(tuple(temp))

print(ans)



arr = [-1,0,1,2,-1,-4]
n = len(arr)
s = set()
ans = set()
arr.sort()

for i in range(n):
    s = set()
    for j in range(i+1,n):
        k = - (arr[i]+arr[j])
        if(k in s):
            temp = [arr[i],arr[j],k]
            temp.sort()
            ans.add(tuple(temp))
        s.add(arr[j])

print(ans)


arr = [-1,0,1,2,-1,-4]
n = len(arr)
s = set()

for i in range(n):
     
     left = i+1
     right = n-1

     while(right > left):
        sums = arr[i] + arr[left] + arr[right]

        if(sums == 0):
            temp = [arr[i],arr[left],arr[right]]
            temp.sort()
            s.add(tuple(temp))

            while(arr[left] == arr[left+1] and right>left):
                left += 1
            while(arr[right] == arr[right+1] and right>left):
                right -= 1
        
        elif(sums > 0):
            right -= 1
        
        elif(sums < 0):
            left += 1

print(ans)

            