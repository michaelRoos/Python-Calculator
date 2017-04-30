from newsplit import *
from peekable import *
from linkedlist import *
from exprtree import *


conditional = ['>','<','==','!=','<=','>=']

def eval_tree_equal(iterator):
	sub =   eval_tree_conditional(iterator)
	while peek(iterator) == '=':
		operator = next(iterator)
		return Oper(sub, "=",eval_tree_equal(iterator))
	return sub

def eval_tree_conditional(iterator):
	sub = eval_tree_sum(iterator)
	if (conditional.__contains__(peek(iterator))):
		operator = next(iterator)
		comp =  Oper(sub, operator, eval_tree_sum(iterator))
		while peek(iterator) == "&" or peek(iterator)== "|":
			operator = next(iterator)
			comp2 = Oper(eval_tree_sum(iterator),next(iterator),eval_tree_sum(iterator))
			comp = Oper(comp,operator, comp2)
		next(iterator)
		one = eval_tree_sum(iterator)
		next(iterator)
		two = eval_tree_sum(iterator)
		return Conditional(one, two, comp)
	return sub


def eval_tree_sum(iterator):
	"""evaluate a sum expression (zero or more additions and subtractions)
		  expr      Python string list           complete expression to be evaluated
		  pos       integer                          subscript to current token
	   """
	sub =   eval_tree_product(iterator)
	while peek(iterator) == '+' or peek(iterator) == '-':
		operator = next(iterator)
		sub = Oper(sub,operator,eval_tree_product(iterator))

	return sub
# return result and updated subscript

def eval_tree_product(iterator):
	"""evaluate a product expression (zero or more multiplications/divisions)
	"""

	sub = eval_tree_factor(iterator)
	while peek(iterator) == '*' or peek(iterator) == '/' or peek(iterator) == '%':
		operator = next(iterator)
		sub = Oper(sub, operator, eval_tree_factor(iterator))
	return sub

def eval_tree_factor(iterator):
	"""evaluate a factor (number or parenthesized sub-expression)"""
	ans = next(iterator)
	if ans == '(':

		a =  eval_tree_sum(iterator)
		next(iterator)
		return a


	else:
		if ans.isdigit():
			if (ans == "-"):
				ans = 0 - int(next(iterator))
			return Value(str(ans))

		else:
			if(peek(iterator)=='('):
				func = ans
				next(iterator)
				parms = [eval_infix_iter(iterator)]
				x = peek(iterator)
				while peek(iterator) != ')' and peek(iterator) != ";" and peek(iterator) != ",":
					parms.append(eval_infix_iter((iterator)))





				return Func(func,parms)

			else:
				return Var(ans)

def eval_infix_iter(iterator):
	"""evaluate an expression, given an iterator to its tokens"""
	return eval_tree_equal(Peekable(iterator))


def to_expr_tree(expr):
	"""accept a character string, split it into tokens, then evaluate"""
	return eval_infix_iter(new_split_iter(expr))

