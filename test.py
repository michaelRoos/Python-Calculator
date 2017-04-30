from infixtotree import *
from newsplit import new_split_iter
from vartree import *
from eval_postfix import eval_postfix

def test(expr):
    tree = to_expr_tree(expr)
    print (expr, ':', tree.evaluate(V1))
    if '?' not in expr:
        a = tree.postfix()

        print("from postfix:", eval_postfix(V1, tree.postfix()))

V1 = BinaryTree()
test("x=1")
test("x>5 or x>1 or x>2? 1:2")




