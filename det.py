#!/usr/bin/env python3
# calculates the determinants of a square matrix using recursion


from pprint import pprint # to print matrix row by row
from math import pow


# initialise a mxn matrix with 0s
def initialise(m,n):
	zero_matrix = [[0 for x in range(n)] for y in range(m)]
	return zero_matrix


def assign_matrix(matrix): # len(matrix) = row, len(matrix[0])= column
	for x in range(len(matrix)):
		for y in range(len(matrix[0])):
			matrix[x][y] = float(input()) # pprint prints in separate rows in float, not int to allow for decimal places
	return matrix


def det(matrix):
	sum = 0
	if len(matrix) is not 2:
		for k in range(len(matrix[0])):
			# print(k)
			sub_matrix = [[matrix[i][j] for j in range(len(matrix[0])) if j is not k] for i in range(len(matrix)) if i is not 0]
			# list comprehension of the following:
			# sub_matrix = []
			# for i in range(len(matrix)): # append the rows
			# 	if i is not 0:
			# 		row = []
			# 		for j in range(len(matrix[0])): # append the values of the columns
			# 			if j is not k:
			# 				row.append(matrix[i][j])
			# 		sub_matrix.append(row)
			# calculates the sum of sub_matrix
			sum = pow(-1, k) * matrix[0][k] * det(sub_matrix) + sum # (-1)^k does not work, requires pow(x,y) from math
			# printDet(matrix, sum)
	else:
		sum = matrix[0][0] * matrix[1][1]-matrix[1][0] * matrix[0][1]
		# printDet(matrix, sum)
		printDet(matrix, sum)
	return sum


def printDet(matrix, sum):
	print('')
	print('The determinant of: ')
	pprint(matrix)
	print('is {}'.format(sum))


if __name__ == '__main__':
	n = input("") # splits the output into 2 numbers
	n = int(n) # converts to int
	matrix = initialise(n,n)
	matrix = assign_matrix(matrix)
	pprint(matrix)
	sum = det(matrix)
	printDet(matrix, sum)


# $ ./det.py < input.txt
# The determinant of:
# [[2.0, 3.0, 2.0, 1.0],
#  [2.0, 3.0, 4.0, 5.0],
#  [6.0, 7.0, 3.0, 2.0],
#  [43.0, 5.0, 3.0, 2.0]]
# is -706.0