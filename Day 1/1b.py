import heapq

def addToHeap(total, heap):
  if len(heap) < 3:
    heapq.heappush(heap, total)
  else:
    heapq.heappush(heap, max(heapq.heappop(heap), total))

with open("1.txt") as fIn:
  heap = []
  total = 0
  counter = 0
  for line in fIn:
    if line.strip("\n") == "":
      addToHeap(total, heap)
      total = 0
    else:
      total += int(line.strip("\n"))
  addToHeap(total, heap)
  print(sum(heap))

print(sum(__import__("functools").reduce(lambda base, x: (0 if x.strip("\n") == "" else base[0] + int(x.strip("\n")), (heapq.heappush(base[1][1], base[0]), base[1][1]) if len(base[1][1]) < 3 else (heapq.heappush(base[1][1], max(heapq.heappop(base[1][1]), base[0])), base[1][1])), open("1.txt").readlines()+["\n"],(0,(None, [])))[1][1]))