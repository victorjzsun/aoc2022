with open("4.txt") as fIn:
  total = 0
  for line in fIn:
    first, second = line.strip().split(",")
    firstStart, firstEnd, secondStart, secondEnd = map(lambda x:int(x), first.split("-") + second.split("-"))
    if ((firstStart <= secondStart and firstEnd >= secondEnd) or
        (firstStart >= secondStart and firstEnd <= secondEnd)):
      total += 1
  print(total)

sum([(lambda x:1 if ((x[0] <= x[2] and x[1] >= x[3]) or (x[0] >= x[2] and x[1] <= x[3])) else 0)(list(map(lambda x:int(x), line.replace(",", "-").split("-")))) for line in open("4.txt")])
