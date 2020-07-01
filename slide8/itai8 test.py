from Slide8 import itai8
import myTestTools

if not myTestTools.print_test(itai8.validate_expr, "") == "Valid expression (empty expression)":
    raise EOFError
if not myTestTools.print_test(itai8.validate_expr, "()") == "Valid expression":
    raise EOFError
if not myTestTools.print_test(itai8.validate_expr, "{{(())}}[[]]") == "Valid expression":
    raise EOFError
if not myTestTools.print_test(itai8.validate_expr, "(") == "Not a valid expression":
    raise EOFError
if not myTestTools.print_test(itai8.validate_expr, "({}[]()") == "Not a valid expression":
    raise EOFError
if not myTestTools.print_test(itai8.validate_expr, "(1+1)") == "Valid expression":
    raise EOFError
if not myTestTools.print_test(itai8.validate_expr, "[1+1]") == "Valid expression":
    raise EOFError
if not myTestTools.print_test(itai8.validate_expr, "hello") == "Valid expression (There where no brackets in the " \
                                                             "expression)":
    raise EOFError

x = itai8.Stack()
x.push(5)
x.push('yay')
if not x.__str__() == "[5, 'yay']":
    raise EOFError
y = itai8.Stack()
y.push(5)
y.push('yay')
if not (x == y):
    raise EOFError
if not y.top() == 'yay':
    raise EOFError
z = x + y
if not z.__str__() == "[5, 'yay', 5, 'yay']":
    raise EOFError
# print(type(z))
if x == z:
    raise EOFError
if not x.top() == 'yay':
    raise EOFError
x.pop()
if not x.top() == 5:
    raise EOFError
x.pop()
try:
    x.pop()
    print("Bad")
except IndexError:
    print('Good')
x = itai8.Stack()
y = itai8.Stack()
x.push(1)
x.push(2)
y.push(3)
z = x + y
if not z.__str__() == "[1, 2, 3]":
    raise EOFError
g = y + x
if not g.__str__() == "[3, 1, 2]":
    raise EOFError
if z == g:
    raise EOFError

if not itai8.validate_expr("()"):
    print("1")
