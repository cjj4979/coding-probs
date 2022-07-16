N = int(input())
p_list = list(map(int, input().split()))
p_list.sort()
votes = 0
for p in p_list[len(p_list)//2+1:]:
    votes += p
for p in p_list[:len(p_list)//2+1]:
    votes += p//2
print(votes)