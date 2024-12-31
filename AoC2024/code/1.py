import collections

lines = [[int(x) for x in l.strip().split('   ')] for l in open("AoC2024/input/1.txt")]

def part1():
  list1 = [l[0] for l in lines]
  list2 = [l[1] for l in lines]

  list1.sort()

  list2.sort()

  sum = 0

  for i in range(len(list1)):
    sum += abs(list1[i] - list2[i])

  print(sum)

def part2():
  list1 = [l[0] for l in lines]
  list2 = [l[1] for l in lines]
  count = collections.Counter(list2)

  total = sum([l * (count.get(l, 0)) for l in list1])

  print(total)

  
part2()
