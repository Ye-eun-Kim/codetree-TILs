nums = list(map(int, input().split()))

for num in nums:
    if num % 2 == 0:
        print(num//2, end = ' ')
    else:
        print(num*3-20, end=' ')