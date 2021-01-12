def fib(n):
	fib1, fib2 = 0, 1
	i = 0
	while i < n :
		fib1, fib2 = fib2, (fib1 + fib2)
		i += 1
	return fib1

