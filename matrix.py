class Matrix:
    'Fields: rows, cols, entries'
    
    ## Purpose: to consume self, rows, cols, and entries and sets the attributes of the new Matrix instance.
    ## Example:
    ## M = Matrix(3,1,[1,2,3])
    ## M.rows = 3
    def __init__(self, rows, cols, entries):
        self.rows = rows
        self.cols = cols
	self.entries = entries	
    ## __repr__: matrix -> str
    ## Purpose: consumes self and produce a string that displays all of the values in entries formatted to look like a matrix.
    ## Example: M = Matrix(1,3,[1,2,3])
    ## print M will display
    ## [[1 2 3]]
    def __repr__(self):
	row = 0
	col = 0
	string = '['
	row_matrix = ''
	entry = self.entries
	while row < self.rows:
	    if col < self.cols:
		row_matrix = row_matrix + str(entry[col]) + ' '
		col += 1
	    else:
		string = string + '[' + row_matrix[:-1] + ']' + '\n'
		entry = entry[col:]
		col = 0
		row += 1
		row_matrix = ''
	return string[:-1] + ']'
    ## __add__: matrix matrix -> matrix
    ## Purpose: consumes two Matrix instance self and other and produce a new Matrix instance which 
    ## is the sum, entry-wise of self and other.
    ## Example:
    ## M = Matrix(3,1,[1,2,3]) , N = Matrix(3,1,[4,5,6])
    ## The print M + N will display
    ## [[5]
    ## [7]
    ## [9]]
    def __add__(self, other):
	n = 0
	lst = []
	while n < len(self.entries):
	    lst.append(self.entries[n] + other.entries[n])
	    n += 1
	return Matrix(self.rows, self.cols, lst)
    ## __mul__: matrix matrix -> matrix
    ## Purpose: consumes two Matrix instance self and other, and produce a new matrix which is the product of self and other.
    ## M = Matrix(3,1,[1,2,3]) , N = Matrix(1,3,[4,5,6])
    ## then print N*M will display [[32]]
    def __mul__(self, other):
	entry1 = self.entries
	new_entries = []
	row_a = 1
	col_a = 0
	row_b = 0
	col_b = 1
	sum = 0
	while row_a <= self.rows:
	    while col_b <= other.cols:
		while col_a < self.cols:
		    sum = sum + (entry1[col_a] * other.entries[row_b])
		    col_a += 1
		    row_b += other.cols
		new_entries.append(sum)
		sum = 0
		col_b += 1
		col_a = 0
		row_b = col_b - 1
	    row_a += 1
	    col_a = 0
	    row_b = 0
	    col_b = 1 
	    entry1 = entry1[self.cols:]
	return Matrix(self.rows, other.cols, new_entries)	
