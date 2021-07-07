# Number of actual operations to make a number 0 using XOR .

def zeroday(user_input):
	p = 0
	count = 0
	p_values = []

	while (2**p) <= user_input:
		computation_result = user_input ^ (2**p)
		count = count + 1
		if computation_result == 0:
			p_values.append(p)
			break
		elif (computation_result < user_input):
			user_input = computation_result
			p_values.append(p)
			p = 0
		else:
			p = p + 1
	print("NUMBER OF ACTUAL XOR OPERATIONS: ", len(p_values))




user_input = int(input())
zeroday(user_input)

