import numpy as np
import pandas as pd

s = pd.read_csv("data.txt", header=None).to_numpy()[0]

ageDistribution = np.zeros(9)
for fish in s:
  ageDistribution[fish] += 1

for i in range(256):
  today = i % len(ageDistribution)
  ageDistribution[(today + 7) % len(ageDistribution)] += ageDistribution[today]

print(sum(ageDistribution))