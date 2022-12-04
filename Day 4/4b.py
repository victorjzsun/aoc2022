with open("4.txt") as fIn:
  total = 0
  for line in fIn:
    first, second = line.strip().split(",")
    firstStart, firstEnd, secondStart, secondEnd = map(lambda x:int(x), first.split("-") + second.split("-"))
    if not (firstEnd < secondStart or secondEnd < firstStart):
      total += 1
  print(total)

sum([(lambda x:1 if not (x[1] < x[2] or x[3] < x[0]) else 0)(list(map(lambda x:int(x), line.replace(",", "-").split("-")))) for line in open("4.txt")])

