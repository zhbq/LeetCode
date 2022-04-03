s = input()
result = []
for i in range(len(s)):
    l = [s[i]]
    for j in range(i+1,len(s)):
        if s[j] in l:
            # print(i,j)
            break
        l.append(s[j])
    result.append(len(l))
print(max(result))

