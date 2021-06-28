class Stack(object):

	def __init__(self, length):
		self.items = []
		self.max_length = length

	def push(self, value):
		if(len(self.items) > self.max_length):
			self.items.pop(0)
		self.items.append(value)

	def pop(self):
		if(self.is_empty()):
			return None
		else:
			return self.items.pop()

	def seek(self):
		return self.items[-1]

	def is_empty(self):
		if not self.items:
			return True
		else:
			return False

	def printStack(self):
		print(self.items)