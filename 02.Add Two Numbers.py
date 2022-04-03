l1 = input().split()
l2 = input().split()
l1 = [int(i) for i in l1]
l2 = [int(i) for i in l2]
for i in range(abs(len(l1)-len(l2))+1):
    l1.append(0)
    l2.append(0)
x = min(len(l1),len(l2)) 
result = [0]*(x+1)
l3 = [0]*(x+1)
for i in range(x):
    if l1[i] + l2[i] + l3[i]>= 10:
        l3[i+1] = 1
        result[i] = l1[i] + l2[i] + l3[i] - 10
    else:
        result[i] = l1[i] + l2[i] + l3[i]
for i in range(x):
    if result[-1] == 0:
        result.pop(-1)
    else:
        break
print(l3,result)