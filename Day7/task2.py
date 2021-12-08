def read_sorted(file):
    with open(file) as f:
        return sorted([int(x) for x in f.readline().split(',')])

s = read_sorted("data.txt")

mean = sum(s) // len(s)
calc = lambda x: x * (x+1) // 2
part2 = sum(calc(abs(x-mean)) for x in s)

print(part2)