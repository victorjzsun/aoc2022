def charToInt(c):
  return ord(c) - ord("a") + 1 if ord(c) >= ord("a") else ord(c) - ord("A") + 27

with open("3a.txt") as fIn:
  total = 0
  elfIndex = 0
  m = [0 for _ in range(52)]
  for line in fIn:
    line = line.strip()
    if elfIndex == 0:
      for c in line:
        m[charToInt(c)-1] = 1
    elif elfIndex == 1:
      for c in line:
        if m[charToInt(c)-1] == 1:
          m[charToInt(c)-1] = 2
    else:
      for c in line:
        if m[charToInt(c)-1] == 2:
          total += charToInt(c)
          m = [0 for _ in range(52)]
          break
    elfIndex = (elfIndex + 1) % 3
  print(total)

from functools import reduce
print(sum(reduce(lambda base,line:((base[0],reduce(lambda base2,char: base2[:ord(char)-ord("a")+1 if ord(char)>=ord("a") else ord(char)-ord("A")+27-1]+[1]+base2[ord(char)-ord("a")+1 if ord(char)>=ord("a") else ord(char)-ord("A")+27:],line[1],base[1])) if (line[0] % 3) == 0 else (base[0],reduce(lambda base2,char: base2[:ord(char)-ord("a")+1 if ord(char)>=ord("a") else ord(char)-ord("A")+27-1]+[2 if base2[ord(char)-ord("a")+1 if ord(char)>=ord("a") else ord(char)-ord("A")+27-1] >= 1 else 0]+base2[ord(char)-ord("a")+1 if ord(char)>=ord("a") else ord(char)-ord("A")+27:],line[1],base[1])) if (line[0] % 3) == 1 else(base[0]+[reduce(lambda base2,char: (base2[0]+[ord(char)-ord("a")+1 if ord(char)>=ord("a") else ord(char)-ord("A")+27] if base2[1][ord(char)-ord("a")+1 if ord(char)>=ord("a") else ord(char)-ord("A")+27-1] == 2 else base2[0],base2[1]),line[1],([], base[1]))[0][0]],[0 for _ in range(52)])),enumerate(map(lambda x:x.strip(), open("3a.txt").readlines())),([], [0 for _ in range(52)]))[0]))
