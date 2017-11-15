#!/usr/bin/env python3
from pprint import pprint # to print matrix row by row
from math import pow

def main():
	n = input("") # splits the output into 2 numbers
	n = int(n) # converts to int
	matrix = initialise(n,n)
	matrix = assign(matrix)
	pprint(matrix)
	sum = det(matrix)
	printDet(matrix, sum)

# initialise a mxn matrix with 0s
def initialise(m,n):
	matrixZero = [[0 for x in range(n)] for y in range(m)]
	return matrixZero

def assign(matrix): # len(matrix) = row, len(matrix[0])= column
	for x in range(len(matrix)):
		for y in range(len(matrix[0])):
			matrix[x][y] = float(input()) # pprint prints in separate rows in float, not int
	return matrix

def det(matrix):
	sum = 0
	if len(matrix) is not 2:
		for k in range(len(matrix[0])):
			# print(k)
			subMatrix = []
			for i in range(len(matrix)):
				if i is not 0:
					row = []
					for j in range(len(matrix[0])):
						if j is not k:
							row.append(matrix[i][j])
					subMatrix.append(row)
			sum = pow(-1, k) * matrix[0][k] * det(subMatrix) + sum # (-1)^k does not work, requires pow(x,y) from math
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
	main()