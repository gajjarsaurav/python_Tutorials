# this is a one dimentional list
x = [2,3,4,5,6,7,8]

# this is a 2 dimentional list
y = [[5,4], [3,4], [7,9], [2,8]]
#     0 1    0 1    0 1    0 1  these are the individual positions of inner lists
#      0      1      2      3   these are the positions of outer lists
print(y)
print(y[3][1])

# this is a multidimentional list
y = [[[5,4], [3,4]], [[7,9], [2,8,3]], [4,6]]
#           0               1          2    outer lists index
#       0      1        0      1            inner lists index
#      0 1    0 1     0  1    0 1 2     0 1 inner most lists index
print(y[1][1][2])                           the output will be three here
