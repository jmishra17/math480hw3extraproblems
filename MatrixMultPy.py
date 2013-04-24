from random import randint
def matrixmult_Py(n):
	X=[]
	Y=[]

	Z=[[0 for j in range(n)] for i in range(n)]
	for i in range(n):
		rowx=[]
		rowy=[]
		for j in range(n):
			rowx.append(randint(1,100))
			rowy.append(randint(1,100))
		X.append(rowx)
		Y.append(rowy)
	print("X",X)
	print("Y",Y)
	
	Z =iterMult(X,Y,Z)
 
        print("Z",Z)

def iterMult(X,Y,Z):
	for i in range(len(X)):
		for j in range(len(X)):
			for k in range(len(X)):
				Z[i][j]+= X[i][k] * Y[k][j]
	return Z