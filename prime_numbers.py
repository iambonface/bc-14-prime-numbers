
"""
This function asymptotically generates prime numbers from 0 to n
Args:
    User privides any number above 0
Results:
    If the number is less than 1,  Nothing is returned
    Else, expect list of prime numbers
    example
    get_prime(13) will print [2,3,5,7,11]
Exceptions:
    Raise TypeError if input n is of any other type other than int
"""
def get_prime(n):

	if isinstance(n, int):
		if n < 1:
			return None
		else:
			target_list = range(2, n+1)
			for i in range(2,8):
				"""iterate on all posible divisors and exclude multiples"""
				target_list = [x for x in target_list if x == i or x % i ]
			print(target_list)

	else:
		raise TypeError("Invalid input {}".format(type(n)))