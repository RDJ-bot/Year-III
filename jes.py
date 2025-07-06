#brook
word = "Jeswin"
num = len(word)-1
for i in range(len(word)):
    print(word[num],end="")
    num = num-1

#optimal
word = "Jeswin"
print(word[::-1])