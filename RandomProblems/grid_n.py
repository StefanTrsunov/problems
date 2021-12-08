d = 5
n = d * d
count = 1
board = []
for i in range(d):
    for j in range(d):
        number = n - count
        if number >= 0 :
            tile = number
            board.append[tile]
        else:
            exit(1)
        count += 1
        print(board)