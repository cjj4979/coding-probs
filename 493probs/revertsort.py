T = int(input())
for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))

    sum = 0
    for i in range(1, N):
        cost = 0
        minVal = min(L)
        j = L.index(minVal) + 1
        cost = j - i + 1
        sum += cost
        
