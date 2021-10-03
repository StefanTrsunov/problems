
# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.

with open('day7_input') as f:
    for line in f:
        dependencies = (list)
        dependencies2 = (list)


def part1():
    can = set()
    look = ["shiny gold"]
    while len(look) > 0:
        c = look.pop()
        for d in dependencies[c]:
            can.add(d)
            look.append(d)

    return len(can)


print(part1())


def part2():
    needs = defaultdict(int)
    look = [(1, "shiny gold")]
    while len(look) > 0:
        N, c = look.pop()
        for n, c1 in dependencies2[c]:
            needs[c1] += N * n
            look.append((N * n, c1))

    return sum(needs.values())


print(part2())








