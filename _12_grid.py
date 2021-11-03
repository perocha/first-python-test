'''
Examples of using grids
'''
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10]
]

print (number_grid)
print (number_grid[0])
print (number_grid[0][1])
print (number_grid[1][2])
# print (number_grid[3][1]) ---> Out of range

print ("\nUse a FOR loop to print the grid")
for row in number_grid:
    for col in row:
        print (col)
