with open('day10_input') as f:
    data = f.readlines()
    data = [line.strip() for line in data]
    sorted = sorted([int(x) for x in data])



def part1():
    ones = 1
    threes = 1
    for x, y in zip(sorted, sorted[1:]):
        if y - x == 1:
            ones += 1
        if y - x == 3:
            threes += 1
    return ones * threes

print(part1())

checked = {}
def part2(pos):

    if pos == len(data)-1:
        return 1

    if pos in checked:
        return checked[pos]

    total = 0
    for i in range(pos+1, len(data)):
        if data[i] - data[pos] <= 3:
            total += get_num_ways(i)

    checked[pos] = total
    return total

print(part2(0))
