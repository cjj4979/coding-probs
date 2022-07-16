num_line = input()

for i in range(int(num_line)):
  s = input()
  first_str = s[:len(s)//2]
  second_str = s[len(s)//2:]
  if first_str == second_str:
    print("yes")
  else:
    print("no")
