print("Read File")

file = open('data.txt', 'r')

print("Set Increase and count to 0")
count = 0

fileAsArray = []
with open('data.txt') as my_file:
  for line in my_file:
    fileAsArray.append(str(line))

print(fileAsArray)

gammaRate = []

for a in range(12):
  cur= ""
  for i in range(len(fileAsArray)):
    cur += fileAsArray[i][a]
  gammaRate.append(cur)

print(gammaRate)

gammaRateFinal = ""
epsRateFinal = ""

for a in range(len(gammaRate)):
  print(str(gammaRate[a]).count('1'))
  if int(str(gammaRate[a]).count('1')) > len(fileAsArray) / 2:
    print(len(gammaRate))
    print("1 bigger")
    gammaRateFinal += str(1)
    epsRateFinal += str(0)
  else:
    gammaRateFinal += str(0)
    epsRateFinal += str(1)

print(eval('0b' + gammaRateFinal))
print(eval('0b' + epsRateFinal))
file.close()
