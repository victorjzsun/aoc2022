def charToInt(c):
  return ord(c) - ord("a") + 1 if ord(c) >= ord("a") else ord(c) - ord("A") + 27

with open("3a.txt") as fIn:
  total = 0
  for line in fIn:
    m = [0 for _ in range(52)]
    line = line.strip()
    for c in line[:len(line)//2]:
      m[charToInt(c)-1] += 1
    for c in line[len(line)//2:]:
      if m[charToInt(c)-1] > 0:
        total += charToInt(c)
        break
  print(total)

print(sum(__import__("functools").reduce(lambda base,x: base+[__import__("functools").reduce(lambda base3,x3: (base3[0] if base3[1][(ord(x3)-ord("a")+1 if ord(x3)>=ord("a") else ord(x3)-ord("A")+27)-1] == 0 else base3[0]+[(ord(x3)-ord("a")+1 if ord(x3)>=ord("a") else ord(x3)-ord("A")+27)],base3[1]),x[len(x)//2:],([],__import__("functools").reduce(lambda base2,x2: base2[:(ord(x2)-ord("a")+1 if ord(x2)>=ord("a") else ord(x2)-ord("A")+27)-1]+[base2[(ord(x2)-ord("a")+1 if ord(x2)>=ord("a") else ord(x2)-ord("A")+27)-1]+1]+base2[(ord(x2)-ord("a")+1 if ord(x2)>=ord("a") else ord(x2)-ord("A")+27):],x[:len(x)//2],[0 for _ in range(52)])))[0][0]], open("3a.txt").readlines(), [])))
