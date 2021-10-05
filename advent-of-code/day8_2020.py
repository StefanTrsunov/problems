with open('day8_input') as f:
    data = f.readlines()
    data = [line.strip() for line in data]


def part1():
    acc = 0
    line = 0
    instructions = []

    while line not in instructions:
        instructions.append(line)

        current = data[line]
        current = current.split()
        command = current[0]
        num = current[1]
        if '+' in num:
            num = int(num[1:])
        else:
            num = int(num)

        if command == 'acc':
            acc += num
            line += 1
        elif command == 'jmp':
            line += num
        if command == 'nop':
            line += 1

        return acc

print(part1())

def part2():
    acc = 0
    line = 0
    instructions = []

    while line not in instructions:
        instructions.append(line)

        current = data[line]
        current = current.split()
        command = current[0]
        num = current[1]

        if '+' in num:
            num = int(num[1:])

        else:
            num = int(num)

        if command == 'acc':
            acc += num
            line += 1

        elif command == 'jmp':
            line += num

        if command == 'nop':
            line += 1

        if line >= len(data):
            return acc, True

    return acc, False


for i in range(len(data)):
    if 'jmp' in data[i]:

        data[i] = data[i].replace('jmp', 'nop')
        acc, found = part2()

        if found:
            print(acc)
            break

        else:
            data[i] = data[i].replace('nop', 'jmp')


