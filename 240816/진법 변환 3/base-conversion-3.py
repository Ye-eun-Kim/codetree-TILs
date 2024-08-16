n = input()

len_n = len(n)

result = []
for i in range(len_n):
    num = n[len_n-i-1]
    num = int(num)
    result.append(str(num%2))
    num //= 2
    result.append(str(num%2))
    result.append(str(num//2))

len_r = len(result)
flag = False
for i in range(len_r-1, -1, -1):
    num = result[i]
    if num == '1' and not flag:
        flag = True
    if num == '0' and not flag:
        continue
    else:
        print(result[i], end='')