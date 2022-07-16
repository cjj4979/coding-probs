n = int(input())
num_types = [0, 0, 0, 0]
isValid = True
i = 0
while i < n:
    seq = input()
    if seq[0] == '0':
        num_types[0] += 1
        i += 1
        continue
    if seq[:3] == "110":
        if not i < n-1:
            print("invalid")
            isValid = False
            break
        next = input()
        if not next[:2] == "10":
            print("invalid")
            isValid = False
            break
        num_types[1] += 1
        i += 2
        continue
    if seq[:4] == "1110":
        if not i < n-2:
            print("invalid")
            isValid = False
            break
        for _ in range(2):
            next = input()
            if not next[:2] == "10":
                print("invalid")
                isValid = False
                break
        if not isValid:
            break
        num_types[2] += 1
        i += 3
        continue
    if seq[:5] == "11110":
        if not i < n-3:
            print("invalid")
            isValid = False
            break
        for _ in range(3):
            next = input()
            if not next[:2] == "10":
                print("invalid")
                isValid = False
                break
        if not isValid:
            break
        num_types[3] += 1
        i += 4
        continue
    else:
        print("invalid")
        isValid = False
        break
if isValid:
    for i in range(4):
        print(num_types[i])