d = {
  "A X": 3,
  "A Y": 4,
  "A Z": 8,
  "B X": 1,
  "B Y": 5,
  "B Z": 9,
  "C X": 2,
  "C Y": 6,
  "C Z": 7,
}
with open("2a.txt") as fIn:
  total = 0
  for line in fIn:
    total += d[line.strip()]
  print(total)

print(__import__("functools").reduce(lambda base,x: base + {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}[x.strip()], open("2a.txt").readlines(), 0))
