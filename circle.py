from math import pi
def circle(r):
	assert r > 0, "The radius must be greater than zero."
	return float(pi * (r * r))
