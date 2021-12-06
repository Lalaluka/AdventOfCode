import numpy as np
from re import findall

fileAsArray = []

with open('data.txt') as my_file:
  for line in my_file:
    fileAsArray.append(str(line))

visitedPoints = np.zeros(shape=(1000,1000))

def processLine(lines:str):
    return [int(x) for x in findall('\d+', lines)]

for i in range(len(fileAsArray)):
  
  (xStart, yStart, xEnd, yEnd) = processLine(fileAsArray[i])
  if xStart == xEnd:
    ymin = min(yStart, yEnd)
    ymax = max(yStart, yEnd)
    visitedPoints[ymin:ymax+1, xStart] += 1

  if yStart == yEnd:
    xmin = min(xStart, xEnd)
    xmax = max(xStart, xEnd)
    visitedPoints[yStart, xmin:xmax+1] += 1

print(visitedPoints[visitedPoints > 1].shape)