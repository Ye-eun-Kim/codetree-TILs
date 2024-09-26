n = int(input())
m = int(input())
nums = list(map(int, input().split()))

answer = 0
nums.sort()
for i in range(1, n):
    for j in range(0, i):
        a, b = nums[j], nums[i]
        if a + b == m:
            answer += 1
print(answer)