num_line = input()

for i in range(int(num_line)):
  sList = list(map(int, input().split()))
  flag = False
  for i in range(len(sList)):
    sList2 = sList.copy()
    s = sList2.pop(i)
    if s == sum(sList2):
      flag = True
      break
    elif s % 2 == 0 and sList2.count(sList2[0]) == len(sList2):
      flag = True
      break
  if flag:
    print('Yes')
  else:
    print('No')