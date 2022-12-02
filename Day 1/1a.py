with open("1a.txt") as fIn:
  maxSoFar = -1
  total = 0
  for line in fIn:
    if line.strip("\n") == "":
      maxSoFar = max(maxSoFar, total)
      total = 0
    else:
      total += int(line.strip("\n"))
  print(max(maxSoFar, total))

print(__import__("functools").reduce(lambda base, x: (0 if x.strip("\n") == "" else base[0] + int(x.strip("\n")), max(base[1], base[0])), open("1a.txt").readlines()+["\n"],(0,-1))[1])
