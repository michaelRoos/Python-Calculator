from newsplit import *
from peekable import *
from linkedlist import *


def eval_postfix_equal(iterator):
	yield from  eval_postfix_sum(iterator)
	while peek(iterator) == '=':
		operator = next(iterator)
		yield from eval_postfix_equal(iterator)
		yield operator


def eval_postfix_sum(iterator):
	"""evaluate a sum expression (zero or more additions and subtractions)
		  expr      Python string list           complete expression to be evaluated
		  pos       integer                          subscript to current token
	   """
	yield from  eval_postfix_product(iterator)
	while peek(iterator) == '+' or peek(iterator) == '-':
		operator = next(iterator)
		yield from eval_postfix_product(iterator)
		yield operator
# return result and updated subscript

def eval_postfix_product(iterator):
	"""evaluate a product expression (zero or more multiplications/divisions)
	"""
	yield from  eval_postfix_factor(iterator)
	while peek(iterator) == '*' or peek(iterator) == '/' or peek(iterator) == '%':
		operator = next(iterator)
		yield from eval_postfix_factor(iterator)
		yield operator

def eval_postfix_factor(iterator):
	"""evaluate a factor (number or parenthesized sub-expression)"""
	ans = next(iterator)
	if ans == '(':
		yield from eval_postfix_equal(iterator)
		next(iterator)


	else:
		yield (ans)

def eval_infix_iter(iterator):
	"""evaluate an expression, given an iterator to its tokens"""
	return eval_postfix_equal(Peekable(iterator))


def to_postfix(expr):
	"""accept a character string, split it into tokens, then evaluate"""
	return eval_infix_iter(new_split_iter(expr))

