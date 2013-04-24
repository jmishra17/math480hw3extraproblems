def computeDetPy():
	matrix = \
		  [[13,42,43,22],
		   [12,67,45,98],
		   [23,91,18,54],
		   [34,56,82,76]]		   
	
	return determ(matrix,len(matrix))

def determ(matrix,n):
	det = 0;p=0;h=0;k=0;i=0;j=0
	temp=[[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
	if n == 1:
		return matrix[0][0]
	elif  n == 2:
		return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
	else:
		for p in range(0, n):
			h = 0
			k = 0
			for i in range(1, n):
				for j in range(0, n):
					if j==p:
						continue 
					temp[h][k] = matrix[i][j]
					k+=1
					if k ==(n-1):
						h+=1
						k=0
			det= det + matrix[0][p] * (-1)**p * determ(temp, n-1)
		
		return det