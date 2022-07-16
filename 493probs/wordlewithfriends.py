guess = []
fb = []
pattern = ["-", "-", "-", "-", "-"]
N, W = map(int, input().split())
invalid_nums = [set() for _ in range(5)]
gray = set()
green = set()
yellow = set()

for i in range(N+W):
    if i < N:
        g, f = input().split()
        guess.append(g)
        fb.append(f)
    else:
        guess.append(input())

for i in range(N):
    for j in range(5):
        if fb[i][j] == "G":
            pattern[j] = guess[i][j]
            green.add(guess[i][j])
        elif fb[i][j] == "Y":
            yellow.add(guess[i][j])
            invalid_nums[j].add(guess[i][j])
        else:
            gray.add(guess[i][j])

# get the possible words
words = []
for i in range(5):
   word = []
   if
