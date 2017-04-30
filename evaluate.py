from vartree import BinaryTree
from peekable import Peekable, peek
from newsplit import new_split_iter
from infixtotree import eval_tree_equal


def define_func(iterator):
    """ Define a new function, which should appear as
          deffn <function name> ( <parameters> ) = <function body>
          a VarTree will associate the function name with
            a list of parameters (at least one, maybe more)
            and a tree representing the function body
    """
    next(iterator)              # "deffn"
    name = next(iterator)       # function name
    next(iterator)              # (
    parms = [next(iterator)]    # first argument
    while next(iterator)==',':
        parms.append(next(iterator))
    next(iterator)              # =
    return name, parms, eval_tree_equal(iterator)

def evaluate(expr):
    """Define a new function, or evaluate an expression
       The decision is based on the first token in the input line
    """
    iterator = Peekable(new_split_iter(expr))
    if peek(iterator) == "deffn":
        name, parms, body = define_func(iterator)
        functions.assign(name, (parms, body))
    else:
        print(expr,':',eval_tree_equal(iterator).evaluate(variables, functions))


functions = BinaryTree()
variables = BinaryTree()
if __name__ == "__main__":
    evaluate("deffn sqr(x) = x*x")
    evaluate("deffn add(a,b,z) = a+b+z")
    evaluate("deffn abs(x) = x > 0 ? x : 0-x")
    evaluate("deffn fact(n) = n <= 1 ? 1 : n * fact(n-1)")
    evaluate("add(sqr(3),1,sqr(sqr(2)))")
    evaluate("1+2 + fact(sqr(2))")

