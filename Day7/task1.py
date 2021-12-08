def read_sorted(file):
    with open(file) as f:
        return sorted([int(x) for x in f.readline().split(',')])

s = read_sorted("data.txt")

mid = s[len(s) // 2]

part1 = sum(abs(x-mid) for x in s)

print(part1)
