s = input()
s2 = "abcdefghijklmnopqrstuvwxyz"
len_s = len(s)
len_s2 = len(s2)
table = [[0 for _ in range(len_s+1)] for _ in range(len_s2+1)]
for i in range(1, len_s2+1):
    for j in range(1, len_s+1):
        if s[j-1] == s2[i-1]:
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1])
# print(table)
num_add = len_s2 - table[len_s2][len_s]
print(num_add)