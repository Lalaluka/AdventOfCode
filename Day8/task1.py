lines = [line.strip() for line in open("data.txt", "r").readlines()]

def processLine(line):
  return sum(1 for word in line.split(" | ")[1].split() if len(word) in [2, 3, 4, 7])

res=sum(processLine(line) for line in lines)

print(res)
