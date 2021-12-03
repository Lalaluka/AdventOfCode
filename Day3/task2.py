def oxygen(array, pos):
  if(len(array)==1):
    return array
  cur=""
  for i in range(len(array)):
    cur += array[i][pos]
  if int(cur.count('1'))==1 | int(cur.count('0'))==0:
    print("FINISH!")
    return array
  else:
    if int(cur.count('1')) >= len(array) / 2:
      return oxygen(filterlist(array,"1",pos), pos+1)
    else:
      return oxygen(filterlist(array,"0",pos), pos+1)

def co2(array, pos):
  if(len(array)==1):
    return array
  cur=""
  for i in range(len(array)):
    cur += array[i][pos]
  if int(cur.count('1')) >= len(array) / 2:
    return co2(filterlist(array,"0",pos), pos+1)
  else:
    return co2(filterlist(array,"1",pos), pos+1)

def filterlist(list, s, pos):
  retur= []
  for i in range(len(list)):
    if str(list[i])[pos]==s:
      retur.append(list[i])
  return retur
  

print("Read File")

fileAsArray = []
with open('data.txt') as my_file:
  for line in my_file:
    fileAsArray.append(str(line))

print()
ox = oxygen(fileAsArray, 0)
co2r = co2(fileAsArray, 0)
print(ox)
print(co2r)
print(eval('0b' + ox[0]) * eval('0b' + co2r[0]))