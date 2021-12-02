print("Read File")

file = open('data.txt', 'r')

print("Set Increase and count to 0")
increase = 0
count = 0

print("Read Line by Line")
prevLine = 0

while True:
  count += 1
  line = file.readline()
  if not line:
    break
  print("Read Line "+str(count))
  if prevLine < int(line) and count != 1:
    print("Increase!")
    increase +=1
  prevLine = int(line)
  
print("Endresult: " + str(increase))
file.close()
