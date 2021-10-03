
def get_row(passport):
    lower = 0
    upper = 127

    for i in range(6):
        half = (upper + lower) // 2
        if passport[i] == 'F':
            lower = half

        elif passport[i] == 'B':
            upper = half + 1

    if passport[6] == 'F':
        return lower

    else:
        return upper

def get_col(passport):
    upper = 7
    lower = 0

    for i in range(2):
        half = (upper + lower) // 2
        if passport[i] == 'L':
            lower = half

        elif passport[i] == 'R':
            upper = half +1

    if passport[2] == 'L':
         return lower

    else:
        return upper

largest = 0
ids = []
with open('day5_input') as file:
    data = file.readlines()
    data = [line.strip() for line in data]


    for passport in data:
        row = get_row(passport[:7])
        col = get_col(passport[7:])

        id = row * 8 + col
        ids.append(id)

print(max(ids))

for id in ids:
    if id+1 not in ids and id+2 not in ids:
        missing = id+1

print(missing)




