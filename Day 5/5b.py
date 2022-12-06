with open("5.txt") as fIn:
  line = fIn.readline()
  numStacks = (len(line) + 1) // 4
  stacks = [[] for _ in range(numStacks)]
  while line[0] != " ":
    for i in range(numStacks):
      if line[4*i + 1] != " ":
        stacks[i].append(line[4*i + 1])
    line = fIn.readline()
  for i in range(numStacks):
    stacks[i].reverse()
  fIn.readline()
  for line in fIn:
    a, b = line.strip().split(" from ")
    numToMove = int(a[5:])
    source, target = [int(x)-1 for x in b.split(" to ")]
    stacks[target] += stacks[source][-numToMove:]
    stacks[source] = stacks[source][:-numToMove]
  print(stacks)
  print("".join([stack.pop() for stack in stacks]))


