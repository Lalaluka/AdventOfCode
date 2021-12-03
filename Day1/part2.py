from numpy import inf
import numpy as np

print("Read File into Array")

fileAsArray = []
with open('data.txt') as my_file:
    for line in my_file:
        fileAsArray.append(int(line))

count = 0
increase = 0

sums_of_3=  np.array([])

for i in range(len(fileAsArray)-2):
  sums_of_3 = np.append(sums_of_3, (fileAsArray[i] + fileAsArray[i+1] + fileAsArray[i+2]))

increase = sum(np.array(sums_of_3[1:]) - sums_of_3[:-1]>0)

print(sums_of_3)

print(increase)