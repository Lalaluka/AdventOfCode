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

# for counter in range(0, len(fileAsArray)):
#   if (counter+1) % 3 == 0:
#     sumA = fileAsArray[counter-2] + fileAsArray[counter-1] + fileAsArray[counter]
#     sumB = fileAsArray[counter-1] + fileAsArray[counter] + fileAsArray[counter+1]
#     print(str(counter) + ": "+str(sumA)+" "+str(sumB))
#     if sumA < sumB:
#       increase+=1
#     if
  # Create Sets every three Steps
  # if (counter+1) % 3 == 0:
  #   sumA = fileAsArray[counter-2] + fileAsArray[counter-1] + fileAsArray[counter]
  #   sumB = fileAsArray[counter-1] + fileAsArray[counter] + fileAsArray[counter+1]
  #   if counter < len(fileAsArray):
  #     sumC = fileAsArray[counter] + fileAsArray[counter+1] + fileAsArray[counter+2]
  #     if sumB < sumC:
  #       increase += 1
  #   if sumA < sumB and counter+1 == 3:
  #     increase += 1

print(increase)