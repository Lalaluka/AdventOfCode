import numpy as np
from re import findall

fileAsArray = []

with open('data.txt') as my_file:
  for line in my_file:
    fileAsArray.append(str(line))

visitedPoints = np.zeros(shape=(1000,1000))

def processLine(lines:str):
    return [int(x) for x in findall('\d+', lines)]

def processDiagonal(xStart,yStart,xEnd,yEnd):
  hor_delta = np.sign(xEnd - xStart)
  ver_delta = np.sign(yEnd - yStart)
  length = np.abs(xEnd - xStart) + 1
    
  return [(xStart + n*hor_delta, yStart + n*ver_delta) for n in range(length)]

for i in range(len(fileAsArray)):
  
  (xStart, yStart, xEnd, yEnd) = processLine(fileAsArray[i])
  if xStart == xEnd:
    ymin = min(yStart, yEnd)
    ymax = max(yStart, yEnd)
    visitedPoints[ymin:ymax+1, xStart] += 1
  elif yStart == yEnd:
    xmin = min(xStart, xEnd)
    xmax = max(xStart, xEnd)
    visitedPoints[yStart, xmin:xmax+1] += 1
  else:
    for y,x in processDiagonal(xStart,yStart,xEnd,yEnd):
      visitedPoints[x,y] += 1

print(visitedPoints[visitedPoints > 1].shape)