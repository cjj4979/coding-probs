answer = []
T = int(input())
for _ in range(T):
    N = input()
    weights = list(map(int, input().split()))
    total_treat = 0
    num_treat = 1
    prev = min(weights)
    while len(weights) > 0:
        min_w = min(weights)
        # for i in range(len(weights)):
        if prev == min_w:
            total_treat += num_treat
            weights.remove(min_w)
            prev = min_w
            # break
        elif prev < min_w:
            num_treat += 1
            total_treat += num_treat
            weights.remove(min_w)
            prev = min_w
            # break
    answer.append(total_treat)
for i in range(T):
    print("Case #" + str(i+1) + ": " + str(answer[i]))