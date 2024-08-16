n, m =input().split()
m = int(m)
if m in range(2, 37):
    pass
else:
    exit()

tot = 0
len_n = len(n)
# Unicode 48~57: 0~9 숫자
#         65~90: A~Z

for i in range(0, len_n):
    num = ord(n[len_n-i-1])
    if num in range(48, 58):
        num -= 48
    else:
        num -= 55
    tot+=(m**i)*num

print(tot)