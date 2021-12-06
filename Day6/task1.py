import numpy as np
import pandas as pd

s = pd.read_csv("data.txt", header=None).to_numpy()[0]

for i in range(0,80):
  for a in range(0,len(s)):
    if s[a]==0:
      s = np.append(s,8)
      s[a] = 6
    else:
      s[a] = s[a]-1

print(len(s))