def minesweeper(mine_grid):
    for r in range(len(mine_grid)):
        for c in range(len(mine_grid[r])):
            if mine_grid[r][c] == 0:
                count = 0
                for sub_r in range(r-1, r+2):
                    if sub_r >= 0 and sub_r < len(mine_grid):
                        for sub_c in range(c-1, c+2):
                            if sub_c >= 0 and sub_c < len(mine_grid[sub_r]):
                                if mine_grid[sub_r][sub_c] == 'M':
                                    count += 1
                mine_grid[r][c] = count
    return mine_grid


if __name__ == "__main__":
    M = 'M'
    mine_grid = [[0, M, 0, M, 0],
                 [0, 0, M, 0, 0],
                 [0, 0, 0, 0, 0],
                 [M, M, 0, 0, 0],
                 [0, 0, 0, M, 0]]
    mine_grid = minesweeper(mine_grid)

    for row in mine_grid:
        for cell in row:
            print(cell, end=' ')
        print()
