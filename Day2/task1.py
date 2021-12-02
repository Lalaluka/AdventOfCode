import numpy as np

position = np.array([0, 0]) #oben unten, nach vorne

print("Read File")

file = open('data.txt', 'r')

count = 0

while True:
  count += 1
  line = file.readline()
  if not line:
    break
  print("Read Line "+str(count))
  print(line)
  lineind = line.split(" ")
  print(lineind)
  if "forward" in line:
    position[1]= position[1] + int(lineind[1])
  if "down" in line:
    position[0]= position[0] + int(lineind[1])
  if "up" in line:
    position[0]= position[0] - int(lineind[1])
  print(position)
