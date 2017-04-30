

class LinkedList:
	class Node:
		__slots__ = "_next", "_value"

		def __init__(self, v, n):
			self._value = v
			self._next = n

	def __init__( self):
		self._head = self._tail = None
		self._size = 0

	def __len__( self ):
		return self._size

	def push(self, val):
		newNode = LinkedList.Node(val, self._head)
		self._head = newNode
		self._size += 1

	def is_empty(self):
		return len(self) == 0

	def pop(self):
		if not self.is_empty():
			val = self._head
			self._head = self._head._next
			self._size -= 1
			return val
		return None

	def append(self, val):
		"""Append val to list by making a new node at end"""
		newNode = LinkedList.Node(val, None)
		self._tail._next = newNode
		self._tail = newNode
		self._size += 1

	def __iter__(self):
		current = self._head
		while(current is not None):
			yield str(current._val)
			current = current._next
		StopIteration

	def __str__(self):
		current = self._head
		s = []
		while (current is not None):
			s.append(current._value)
			current = current._next
		return str(s)

