with open("6.txt") as fIn:
  d = {}
  line = fIn.readline().strip()
  p0 = 0
  p1 = 0
  for i, c in enumerate(line):
    if len(d) == 14:
      print(i)
      break
    elif c in d:
      while line[p0] != c:
        del d[line[p0]]
        p0 += 1
      p0 += 1
    else:
      d[c] = True

print(__import__("functools").reduce(lambda base, x:base if len(base[1]) == 14 else ((base[0]+x, (lambda _:base[1])(base[1].__setitem__(x, True)), base[2] + 1) if x not in base[1] else (lambda _:((base[0][base[0].find(x)+1:]+x, base[1], base[2] + 1)))([base[1].__delitem__(base[0][i]) for i in range(base[0].find(x))])), open("6.txt").read().strip(), ("", {}, 0))[2])
