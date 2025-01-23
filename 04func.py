from functools import partial

# 函数定义
def my_max(a, b):
  return a if a > b else b

print(my_max(1, 2))


def my_abs(num):
  if not isinstance(num, (int, float)):
    raise TypeError('参数类型错误')
  return num if num > 0 else -num

print(my_abs(-10))


def divide(a, b):
  if b == 0:
    raise ZeroDivisionError('除数不能为0')
  if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
    raise TypeError('参数类型错误')
  return a / b

try:
  print(divide(1, 2))
except ZeroDivisionError as e:
  print('ZeroDivisionError: ', e)
except TypeError as e:
  print('TypeError: ', e)

# 默认参数
def calc_with_op(a, b, op = '+'):
  if op == '+':
    return a + b
  elif op == '-':
    return a - b
  else:
    raise ValueError('无效的运算符')

print(calc_with_op(1, 2, '+'))
print(calc_with_op(1, 2, '-'))
print(calc_with_op(1, 2), 'default')

# 可变参数
def add(a, b, *args):
  total = a + b
  for num in args:
    total += num
  return total

print(add(1, 2, 3, 4, 5))

# 关键字参数
def calc_with_kwargs(a, b, **kwargs):
  print(a, b, kwargs)

calc_with_kwargs(1, 2, c=3, d=4)

# 命名关键字参数
def calc_with_named_args(a, b, *, c, d):
  print(a, b, c, d)

calc_with_named_args(1, 2, c=3, d=4)

# 参数组合
def calc_combined(a, b, *args, c, d, **kwargs):
  print(a, b, args, c, d, kwargs)

calc_combined(1, 2, 3, 4, 5, c=6, d=7, e=8, f=9)


# 多个返回值
def calc(a, b):
  return a + b, a - b

print('calc(1, 2): ', calc(1, 2))

# print('name: ', calc.__name__, 'doc: ', calc.__doc__, 'code: ', calc.__code__)

# 匿名函数
anonymous_func = lambda x, y: x + y
print('anonymous_func(1, 2): ', anonymous_func(1, 2))

# 结合 map 使用
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)  # 输出：[1, 4, 9, 16, 25]

# 结合 filter 使用
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出：[2, 4]

# 结合 reduce 使用
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 输出：120

# 结合 sorted 使用
sorted_numbers = sorted(numbers, key=lambda x: x, reverse=True)
print('sorted_numbers', sorted_numbers)  # 输出：[1, 2, 3, 4, 5]

# 偏函数
def add(a, b):
  return a + b

add_5 = partial(add, 5)
print('add_5(10): ', add_5(10))

int2 = partial(int, base=2)
print('int2("1010"): ', int2("1010"))

