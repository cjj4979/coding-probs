N = int(input())
prices = list(map(int, input().split()))
P = int(input())
count = 0

for i in range(N):
  val = 0
  divisor = 1
  for j in range(i,N):
    val += prices[j]
    if (val//divisor) >= P:
      count += 1
    divisor += 1
print(count)