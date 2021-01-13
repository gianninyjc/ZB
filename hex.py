from math import pow
from math import sqrt

def hex(r):
	assert r > 0, "The length must be greater than zero."
	return ((3 * sqrt(3))/2) * pow(r, 2)
