dic = {}
names = []
n = int(input())
for i in range(n):
    name = input()
    party = input()
    dic[name] = [0, party]

m = int(input())
for i in range(m):
    name = input()
    if name in dic:
        dic[name][0] += 1

winner = None
tied = False
for n in dic:
    cur = dic[n]
    if winner is None:
        winner = cur
    else:
        if winner[0] < cur[0]:
            winner = cur
            tied = False
        elif winner[0] == cur[0]:
            tied = True
        else:
            tied = False
if tied:
    print("tie")
else:
    print(winner[1])


