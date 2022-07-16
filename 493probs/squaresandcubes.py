import math

num_line = input()

for i in range(int(num_line)):
  s = set()
  val = int(input())
  flag1 = False
  flag2 = False
  for x in range(1, int(math.sqrt(val))+1):
    if flag1 == False:
      if isinstance(x ** 2, int) and x**2 <= val:
        s.add(x ** 2)
      elif x**2 > val:
        flag1 = True
    if flag2 == False:
      if isinstance(x ** 3, int) and x**3 <= val:
        s.add(x ** 3)
      elif x**3 > val:
        flag2 = True
  print(len(s))
