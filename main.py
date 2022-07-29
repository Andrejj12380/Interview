# coding=utf-8
class Stack:

	def __init__(self):
		self.stack = []

	def isEmpty(self):
		if len(self.stack) == 0:
			return True
		else:
			return False

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		if self.isEmpty():
			return None
		else:
			self.stack.pop(-1)
			if self.isEmpty():
				return None
			else:
				return self.stack[-1]

	def peek(self):
		if self.isEmpty() == False:
			return self.stack[-1]
		else:
			return None

	def size(self):
		if self.isEmpty() == False:
			return len(self.stack)
		else:
			return None