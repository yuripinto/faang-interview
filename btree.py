class Node:
	def __init__(self, left, right, data):
		self.data = data
		self.left = left
		self.right = right

	def insert(self, new_data):
		if new_data <= self.data:
			if self.left is None:
				self.left = Node(None, None, new_data)
			else: 
				self.left.insert(new_data)
		else:	
			if self.right is None:
				self.right = Node(None, None, new_data)
			else:
				self.right.insert(new_data)

	def search(self, searched_value):
		if searched_value == self.data:
			return True
		if searched_value <= self.data:
			return self.left.search(searched_value) if self.left is not None else False
		else:
			return self.right.search(searched_value) if self.right is not None else False

	def inorder(self):
		if self.left is not None:
			self.left.inorder()
		print(self.data)
		if self.right is not None:
			self.right.inorder()

	def preorder(self):
		print(self.data)
		if self.left is not None:
			self.left.preorder()
		if self.right is not None:
			self.right.preorder()

	def postorder(self):
		if self.left is not None:
			self.left.postorder()
		if self.right is not None:
			self.right.postorder()
		print(self.data)

head = Node(None, None, 4)
head.insert(2)
head.insert(1)
head.insert(3)
head.insert(5)
head.insert(6)
print(head.search(3))
print("inorder")
head.inorder()
print("preorder")
head.preorder()
print("postorder")
head.postorder()
