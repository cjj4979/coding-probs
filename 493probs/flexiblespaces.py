total_width, p = map(int, input().split())
Locations = list(map(int, input().split()))
widths = set()
Locations.insert(0, 0)
Locations.append(total_width)
for i in range(len(Locations)):
    for j in range(Locations[i], total_width + 1):
        if j in Locations:
            widths.add(j - Locations[i])

print(widths)