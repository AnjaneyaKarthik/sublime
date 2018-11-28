class Stack():
	def __init__(self):
		self.items = []

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		if not self.items:
			return("Stack is empty")
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

	def isEmpty(self):
		if not self.items:
			return True
		else:
			return False
		#return len(self.items) == []

	def display(self):
		li = ' '.join(str(item) for item in self.items)
		return li



