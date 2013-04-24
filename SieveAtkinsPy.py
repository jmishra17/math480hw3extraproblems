'''
	This program calculates all primes upto limit
'''

import math
def sieve_atkinsPy(limit):
	result = [2,3,5]
	is_prime = [False]*(limit+1)
	factor = int(math.sqrt(limit))+1
	for x in range(1,factor):
		for y in range(1, factor):
			n = 4*(x**2)+(y**2)
			if (n <= limit) and ((n % 12 == 1) or (n % 12 == 5)):
				is_prime[n] = not is_prime[n]
			n = 3*(x**2)+(y**2)
			if (n <= limit) and ((n % 12) == 7):
				is_prime[n] = not is_prime[n]
			if x > y:
				n = 3*(x**2)-(y**2)
				if (n <= limit) and ((n % 12 == 11)):
					is_prime[n] = not is_prime[n]
	for i in range(5,factor):
		if is_prime[i]:
			jump = i**2
			for j in range(i**2, limit, jump):
				is_prime[j] = False
	for index in range(7,limit):
		if is_prime[index]:
			result.append(index)
	return result