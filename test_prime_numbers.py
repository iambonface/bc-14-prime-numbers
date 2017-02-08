from prime_numbers import get_prime
import unittest

class TestPrimeNumbers(unittest.TestCase):

	def test_get_prime_input_7_is_prime(self):
		self.assertTrue(get_prime(7))

	def test_get_prime_input_13_returns_prime_list(self):
		result = get_prime(13)
		self.assertEqual(result, [2,3,5,7,11,13])

	def test_get_prime_input_str_raises_typeerror(self):
		self.assertRaises(TypeError, get_prime, "num")

	def test_get_prime_output_has_2_as_first_element(self):
		result = get_prime(7)
		self.assertEqual(result[0], 2)

	def test_get_prime_output_includes_input_if_input_is_prime(self):
		result = get_prime(13)
		self.assertEqual(result[-1], 13)

	def test_get_prime_output_has_no_even_number_except_2(self):
		result = get_prime(13)
		for i in result[1:]:
			self.assertTrue(i % 2)

	def test_get_prime_input_less_than_1_returns_none(self):
		result = get_prime(1)
		self.assertEqual(result, None)


if __name__ == '__main__':
	unittest.main()