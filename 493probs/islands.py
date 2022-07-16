r, c = map(int, input().split())
img = [[c for c in input()] for _ in range(r)]
visited = [[False] * c for _ in range(r)]
count = 0


def dfs(i, j):
    visited[i][j] = True
    if i > 0:
        if img[i - 1][j] != "W" and not visited[i - 1][j]:
            dfs(i - 1, j)
    if i < r - 1:
        if img[i + 1][j] != "W" and not visited[i + 1][j]:
            dfs(i + 1, j)
    if j > 0:
        if img[i][j - 1] != "W" and not visited[i][j - 1]:
            dfs(i, j - 1)
    if j < c - 1:
        if img[i][j + 1] != "W" and not visited[i][j + 1]:
            dfs(i, j + 1)


for i in range(r):
    for j in range(c):
        if not visited[i][j] and img[i][j] == "L":
            dfs(i, j)
            count += 1

print(count)
