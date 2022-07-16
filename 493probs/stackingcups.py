num = int(input())

order = {}
for i in range(num):
    a, b = input().split()
    if not a.isalpha():
        order[int(a)//2] = b
    else:
        order[int(b)] = a


for n in sorted(order):
    print(order[n])
