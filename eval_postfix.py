from vartree import *
from linkedlist import *

def eval_postfix(tree, iterator):
	vartree = tree
	stack = LinkedList()

	current = (next(iterator))
	while current is not None:
		current = str(current)
		if current.isdigit():
			stack.push((current))
			try:
				current = next(iterator)
			except StopIteration:
				break
		elif current.isalnum():
			stack.push((vartree.lookup(current)))
			try:
				current = next(iterator)
			except StopIteration:
				break
		else:
			operator = str(current)
			right = str(stack.pop()._value)
			left = str(stack.pop()._value)
			if(operator is '='):
				vartree.assign(left,right)
				stack.push(left)
			else:
				if not is_number(left):
					left = vartree.lookup(left)
				if not is_number(right):
					right = vartree.lookup(right)
				ans = eval(str(left) + operator + str(right))
				stack.push(ans)
			try:
				current = next(iterator)
			except StopIteration:
				break

	ans = str(stack.pop()._value)
	if ans.isalpha():
		return vartree.lookup(ans)
	else:
		return ans


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False