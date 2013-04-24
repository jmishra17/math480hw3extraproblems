import numpy as np 
cimport numpy as np
def computeDetCy():
	r=4
	c=4
	cdef np.ndarray[long, ndim=2] matrix=np.zeros((4,4)).astype(int)
	for i in range(4):
		for j in range(4):
			matrix[i][j]=<np.int32_t> i*j
	return determ(matrix,<int>len(matrix))

cdef inline int determ(np.ndarray[long, ndim=2] matrix, int n):
	cdef int det = 0
	cdef int p=0
	cdef int h
	cdef int k
	cdef int i=0
	cdef int j=0
	cdef np.ndarray[long, ndim=2] temp=np.zeros((4,4)).astype(int)
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