matrix class with basic operations

For example: 

M = Matrix(3, 2, [1, 2, 3, 4, 5, 6]) followed by
print M will display
[[1 2]
[3 4]
[5 6]]
While if M = Matrix(3, 1, [1, 2, 3]) then M.__repr__() produces
the string '[[1]\n[2]\n[3]]'


If M = Matrix(3, 1, [1, 2, 3]) and
N = Matrix(3, 1, [4, 5, 6]) then print M + N will display
[[5]
[7]
[9]]


If M = Matrix(3, 1, [1, 2, 3]) and
N = Matrix(1, 3, [4, 5, 6]) then print N*M will display
[[32]]
and print M*N will display
[[4 5 6]
[8 10 12]
[12 15 18]]
