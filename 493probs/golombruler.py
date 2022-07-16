nums = list(map(int, input().split()))

while len(nums) != 0:
  vals = []
  maxMark = max(nums)
  missing = list(range(1, maxMark+1))
  print(missing)
  isRuler = True
  for i in range(1, len(nums)):
    if not isRuler:
      print("not a ruler")
      break
    for j in range(len(nums)):
      if j+i < len(nums):
        val = abs(nums[j] - nums[j+i])
        vals.append(val)
        print(vals)
        if vals.count(val) > 1:
          isRuler = False
          break
        if val in missing:
          missing.remove(val)
  vals.sort()
  if vals == list(range(1, maxMark+1)):
    print("perfect")
  elif isRuler:
    print("missing", *missing)

  nums = list(map(int, input().split()))