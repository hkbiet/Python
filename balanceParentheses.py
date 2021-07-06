class Stack(object):
	def __init__(self):
		self.items = []

	def pop(self):
		if self.is_empty():
			return None
		else:
			return self.items.pop()

	def push(self, value):
		self.items.append(value)

	def is_empty(self):
		if self.items:
			return False
		else:
			return True

	def seek(self):
		return self.items[-1]

	def printStack(self):
		print(self.items)


def checkBalancedParantheses(input_string):
	stack = Stack()
	parentheses_balanced = False
	
	for character in input_string:
		
		if character in "({[":
			stack.push(character)
		
		elif character in ")}]":
			
			if stack.is_empty():
				parentheses_balanced = False
				return parentheses_balanced

			top_element = stack.pop()
			if top_element == '(' and character == ')':
				pass
			elif top_element == '{' and character == '}':
				pass
			elif top_element == '[' and character == ']':
				pass
			else:
				parentheses_balanced = False
				return parentheses_balanced

	if stack.is_empty():
		parentheses_balanced = True
	else:
		parentheses_balanced = False
	
	return parentheses_balanced



if __name__ == "__main__":
	user_input = input("ENTER THY STRING WITH PARENTHESES: ")
	result = checkBalancedParantheses(user_input)
	if result:
		print("PARENTHESES ARE BALANCED ")
	else:
		print("PARENTHESES ARE NOT BALANCED ")
