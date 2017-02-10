
"""
This function asymptotically generates prime numbers from 0 to n
Args:
    User privides any number above 0
Results:
    If the number is less than 1,  Nothing is returned
    Else, expect list of prime numbers
    example
    get_prime(13) will print [2,3,5,7,11,13]
Exceptions:
    Raise TypeError if input n is of any other type other than int
"""
def get_prime(n):
	if not isinstance(n, int):
		raise TypeError("Invalid input {}".format(type(n)))
	elif n >= 2:
		target_prime = range(2, n+1)
		for i in range(2,8):
			target_prime = [x for x in target_prime if x == i or x % i ]
		return target_prime
	else:
		return None
		