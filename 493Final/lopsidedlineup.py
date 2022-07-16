from itertools import combinations

def getScore(c):
    pass


n = int(input())
scores = []
for i in range(n):
    scores.append(list(map(int, input().split())))

p = []
for i in range(1, n):
    p.append(i)

comb = list(combinations(p,n//2-1))
print(comb)
max_diff = 0
for c in comb:
    print("c: " + ' '.join(str(e) for e in c))
    rest = p.copy()

    print("before rest: " + ' '.join(str(e) for e in rest))
    for i in range(len(c)):
        rest.remove(c[i])

    print("rest: " + ' '.join(str(e) for e in rest))

    score1 = 0
    score2 = 0

    if len(c) == 1:
        score1 += scores[0][c[0]]
    else:
        for i in range(len(c)):
            for j in range(i+1, len(c)+1):
                if i == 0:
                    score1 += scores[i][c[j]]
                else:
                    score1 += scores[c[i]][c[j]]
                print("i j: " + str(i) + " " + str(j))
                print("score1 " + str(score1))


    for i in range(len(rest)-1):
        for j in range(i+1, len(c)):
            score2 += scores[rest[i]][rest[j]]
            print("i j: " + str(rest[i]) + " " + str(rest[j]))
            print("score2 " + str(score2))

    print("diff " + str(abs(score1-score2)))
    if max_diff < abs(score1-score2):
        max_diff = abs(score1-score2)
        print("max_diff " + str(max_diff))

print(max_diff)



