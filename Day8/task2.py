lines = [line.strip() for line in open("data.txt", "r").readlines()]

def processLine(line):
  digits = line.split(" | ")[0].split()

  #Easy ones
  one = [d for d in digits if len(d) == 2].pop()
  seven = [d for d in digits if len(d) == 3].pop()
  four = [d for d in digits if len(d) == 4].pop()
  eight = [d for d in digits if len(d) == 7].pop()
  print(one)
  print(seven)
  print(four)
  print(eight)
  arr = []
  print(line)

print(sum(processLine(line) for line in lines))