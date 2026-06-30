s = input()
s = list(s)

i = 0
j = len(s) - 1

while i < j:

    if s[i].isalpha() and s[j].isalpha():
        s[i],s[j] = s[j],s[i]
        i += 1
        j -= 1
    elif s[i].isnumeric() and s[j].isalpha():
        i += 1
    elif s[j].isnumeric() and s[i].isalpha():
        j -= 1
    else:
        i += 1
        j -= 1

print(s)
