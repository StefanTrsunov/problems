def solve(n):
    grid = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        grid[i][i] = 1
        grid[i][-(i+1)] = 1
    #print(grid)
    print(*grid, sep='\n')# ova matevski mi go kaza xD

solve(5)