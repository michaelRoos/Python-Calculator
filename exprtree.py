from abc import ABCMeta,abstractmethod
from vartree import BinaryTree
from infixtotree import *


class ExprTree(metaclass=ABCMeta):
    """Abstract class for expression"""
    def __str__(self):
        return ' '.join( str(x) for x in iter(self) )

    #   All of the derived class mus implement these functions
    @abstractmethod
    def __iter__(self):
        """an inorder iterator for this tree node, for display"""
        pass
    @abstractmethod
    def postfix(self):
        """a post-order iterator to create a postfix expression"""
        pass
    @abstractmethod
    def evaluate(self, variables, functions):
        """evaluate using the existing variables"""
        pass

class Var(ExprTree):
    """A variable leaf"""
    def __init__(self, n):
        self._name = n
    def __iter__(self):
        yield self._name
    def postfix(self):
        yield self._name
    def evaluate(self, variables, functions):
        return str(variables.lookup(self._name))

class Value(ExprTree):
    """A variable leaf"""
    def __init__(self, n):
        self._name = n
    def __iter__(self):
        yield self._name
    def postfix(self):
        yield self._name
    def evaluate(self, variables, functions):
        return str(self._name)

class Oper(ExprTree):
	def __init__(self, left, n, right):
		self._name = str(n)
		self._left = left
		self._right = right
	def __iter__(self):
		yield "("
		yield from self._left
		yield self._name
		yield from self._right
		yield ")"
	def postfix(self):
		yield from self._left.postfix()
		yield from self._right.postfix()
		yield self._name

	def evaluate(self, variables, functions):
		if self._name == "=":
			variables.assign(self._left._name,self._right.evaluate(variables,functions))
			return self._right.evaluate(variables,functions)
		else:
			return eval(str(self._left.evaluate(variables,functions))+self._name+str(self._right.evaluate(variables,functions)))


class Conditional(ExprTree):
	def __init__(self, left, right, center):
		self._name = "?"
		self._left = left
		self._right = right
		self._center = center
	def __iter__(self):
		yield self._center
		yield "?"
		yield from self._left
		yield ":"
		yield from self._right
	def postfix(self):
		yield from self._left.postfix()
		yield from self._right.postfix()
		yield self._center
		yield "?"

	def evaluate(self, variables, functions):
		if self._center.evaluate(variables,functions):
			return self._left.evaluate(variables,functions)
		else:
			return self._right.evaluate(variables,functions)




class Func(ExprTree):
	def __init__(self, n, p):
		self._name = str(n)
		self._parm = p
	def __iter__(self):
		yield self._name
		yield "("
		yield self._parm
		yield ")"
	def postfix(self):
		yield self._name
		yield "("
		yield self._parm
		yield ")"

	def evaluate(self, variables, functions):
		parms_func, expr_tree = functions.lookup(self._name)
		parms_input = self._parm
		newTree = BinaryTree()
		for a in range(len(parms_func)):
			newTree.assign(parms_func[a],parms_input[a].evaluate(variables,functions))
		return expr_tree.evaluate(newTree,functions)




"""
V = BinaryTree()
VA = Var("A")
Sum = Oper(Value(2), '+', Value(3))
A = Oper(VA,'=',Sum)
print( "Infix iteration: ", list(A) )
print( "String version ", A )
print( "Postfix iteration: ", list(A.postfix() ))
print( "Execution: ", A.evaluate(V) )
print( "Afterwards, A = ", VA.evaluate(V) )
"""