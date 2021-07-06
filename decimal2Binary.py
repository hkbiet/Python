import unittest



def decimal2Binary(user_input):
	stack = []

	if user_input == 0:
		stack.append(user_input)
	
	while user_input > 0:
		remainder = user_input % 2
		stack.append(remainder)
		user_input = user_input // 2

	result = ""

	while stack:
		result = result + str(stack.pop())

	return result




class Test_decimal2Binary(unittest.TestCase):

	def test_conversion(self):
		self.assertAlmostEqual(decimal2Binary(0),'0')
		self.assertAlmostEqual(decimal2Binary(1),'1')
		self.assertAlmostEqual(decimal2Binary(2),'10')
		self.assertAlmostEqual(decimal2Binary(5),'101')
		self.assertAlmostEqual(decimal2Binary(71),'1000111')
		self.assertAlmostEqual(decimal2Binary(82),'1010010')
		self.assertAlmostEqual(decimal2Binary(456),'111001000')
		self.assertAlmostEqual(decimal2Binary(7894),'1111011010110')
		self.assertAlmostEqual(decimal2Binary(798456),'11000010111011111000')

if __name__ == "__main__":
	
	user_input = int(input("ENTER A NUMBER: "))
	binary_result = decimal2Binary(user_input)
	print(binary_result)
