a = str(input())
res = 0
for i in range(len(a)):
    if res > int(a[i]):
        res = i

print(res)
