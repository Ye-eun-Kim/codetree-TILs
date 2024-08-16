s = input()
# X와 .이 아닌 문자 삭제하는 코드 추가함
new_s = ''
for c in s:
    if c not in ['X', '.']:
        continue
    new_s += c
s = new_s
#
len_s = len(s)
dp = ['']*(len_s)
if len_s > 50:
    exit()

tmp = 0
for i in range(len_s):
    c = s[i]
    if c == '.':
        dp[i] = dp[i-1] + '.'
        continue
    if c == 'X':
        tmp+=1
    if tmp == 4:
        dp[i] = dp[i-4]+'aaaa'
        tmp = 0
    elif tmp == 2:
        if i == 1:
            dp[i] = 'bb'
            continue
        now = dp[i-2]+'bb'
        org = dp[i]
        if org == '':
            dp[i] = now
        else:
            if org == dp[i-2]+'aa':
                continue

if dp[-1] == '':
    print(-1)
else:
    print(dp[-1])