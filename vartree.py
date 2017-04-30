class BinaryTree:
	class Node:
		__slots__ = "_val", "_var", "_left", "_right"

		def __init__(self, l, var,val, r):
			self._left = l;  # left branch towards smaller values
			self._val = val;  # value stored at this tree node
			self._right = r;  # right branch towards larger values
			self._var = var

		def __str__(self):
			return str(self._var)+","+str(self._val)


	def __init__(self):
		self._root = None  # initially empty tree
		self._count = 0

	def _search(self, here,var):
		if here is not None:
			if (here._var) > (var):
				here =  self._search(here._left, var)
			elif (here._var) < (var):
				here = self._search(here._right, var)
		return here


	def _insert(self,here,var,val):
		if here is not None:
			if (here._var) > (var):
				return self.Node(self._insert(here._left,var,val),here._var, here._val, here._right)
			elif (here._var) < (var):
				return self.Node( here._left,here._var, here._val,self._insert(here._right, var, val),)
			else:
				self._count -= 1
				return self.Node(here._left, here._var, val, here._right)

		return self.Node(None, var, val, None)

	def assign(self, var, val):
		self._root = self._insert(self._root, var, val)
		self._count +=1


	def lookup(self, var):
		v =  self._search(self._root, var)
		if v is None:
			self.assign(var, 0)
			return 0
		else:
			return v._val

	def is_empty(self):
		return self._root == None

	def __len__(self):
		return self._count

	def __iter__(self):
		yield from self.step(self._root)

	def step(self, here):
		yield here
		if here._left is not None:
			yield from self.step(here._left)
		if here._right is not None:
			yield from self.step(here._right)

	def __str__(self):
		return self.sub(self._root, "")

	def sub(self, root, s):
		current = list()
		current.append(root)
		while len(current) is not 0:
			for n in current:
				s+=(str(n)+" ")
			s+=("\n")
			next = list()
			for n in current:
				if n._left is not None:
					next.append(n._left)
				if n._right is not None:
					next.append(n._right)
				current = next
		return s




V = BinaryTree()
V.assign("a",2)



