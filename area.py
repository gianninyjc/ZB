from math import pi
from math import sqrt
from math import pow

square = 1
circle = pi
hex = (3 * sqrt(3))/2

def area(shape, r):
	return float(shape * pow(r, 2))

