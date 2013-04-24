def sumCy(n):
	return  compute(n)
		
cdef inline long compute(long n):
	return (n*(n+1)*((2*n)+1))/6