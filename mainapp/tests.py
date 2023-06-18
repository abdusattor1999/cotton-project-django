# from django.test import TestCase

def countNegatives(grid):
    n = grid.pop()
    response = countNegatives(n)
    it = 0
    if n < 0:
        it += 1
    return it

grid = [[3,2],[1,0]]

print(countNegatives(grid))