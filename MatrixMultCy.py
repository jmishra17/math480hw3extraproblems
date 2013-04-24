import random as rd
def matrixmult_Cy(int n):
	cdef list X=[]
	cdef list Y=[]

	cdef list Z=[[0 for j in range(n)] for i in range(n)]
	for i in range(n):
		rowx=[]
		rowy=[]
		for j in range(n):
			rowx.append(rd.randint(1,100))
			rowy.append(rd.randint(1,100))
		X.append(rowx)
		Y.append(rowy)
	print(X)
	print(Y)
	
	Z =iterMult(X,Y,Z)
	print(Z)

cdef list iterMult(list X,list Y,list Z):
	for i in range(len(X)):
		for j in range(len(X)):
			for k in range(len(X)):
				Z[i][j]+= X[i][k] * Y[k][j]
	return X
		
		
			