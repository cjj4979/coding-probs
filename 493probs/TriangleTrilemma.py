import math

num_line = input()

for i in range(int(num_line)):
  caseNum = i+1

  answer = ""
  answer += "case #"
  answer += str(caseNum)
  answer +=": "
  distances = []
  angles = []
  points  = list(map(int, input().split()))
  p1 = points[0:2]
  p2 = points[2:4]
  p3 = points[4:len(points)]

  distances.append(math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2))
  distances.append(math.sqrt((p3[0]-p1[0])**2+(p3[1]-p1[1])**2))
  distances.append(math.sqrt((p3[0]-p2[0])**2+(p3[1]-p2[1])**2))

  s = (distances[0] + distances[1] + distances[2]) / 2
  area = (s*(s-distances[0])*(s-distances[1])*(s-distances[2])) ** 0.5
  if area == 0:
    print("case #", caseNum, ": not a triangle")
    break

  tempSet = set(distances)
  if len(tempSet) != len(distances):
    answer+= "isosceles "
  else:
    answer += "scalene "

  angles.append(math.asin(distances[1]/distances[0]))
  angles.append(math.acos(distances[2]/distances[0]))
  angles.append(math.atan(distances[1]/distances[2]))

  if all(a < math.radians(90) for a in angles):
    answer += "acute "
  elif angles.count(math.radians(90)) == 1:
    answer += "right "
  answer += "triangle"
  print(answer)