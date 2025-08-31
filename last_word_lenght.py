'''
word = " Hello to the moon "
count = 0
word = (word.strip())
for char in word[::-1]:
    if(char != ' '):
        count += 1
    else:
        break
print(count)
'''
word = "Jeswin Aaron"
count = 0
for char in range(len(word)-1,-1,-1):
    if(word[char] != ' '):
        count += 1
    else:
        break
print(count)