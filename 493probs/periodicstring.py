s = input()
length = len(s)
ks = []
for k in range(1, length+1):
    if length % k == 0:
        n = length//k
        start = 0
        end = k
        for i in range(n):
            if i < n - 1:
                cur = s[start:end]
                next = s[start+k:end+k]
                # print("before " + cur + " " + next)
                c = cur[-1]
                cur = cur[:-1]
                cur = c + cur
                # print("after " + cur + " " + next)
                if cur != next:
                    break
                start += k
                end += k
            else:
                ks.append(k)
# print(ks)
print(ks[0])