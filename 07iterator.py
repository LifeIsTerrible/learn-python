# 迭代器
list = [1, 2, 3]
it = iter(list)

print(next(it))
print(next(it))
print(next(it))
# print(next(it))

class MyIterator:
  def __init__(self, start, end):
    self.start = start
    self.end = end
  def __iter__(self):
    return self
  def __next__(self):
    if self.start < self.end:
      self.start += 1
      return self.start - 1
    else:
      raise StopIteration
  
it1 = MyIterator(1, 5)

for i in it1:
  print('it1:', i)


# 生成器
def my_generator():
  yield 1
  yield 2
  yield 3

for i in my_generator():
  print('my_generator:', i)

# 生成器表达式，格式为：(表达式 for 元素 in 可迭代对象 if 条件)
gen = (i ** 2 for i in range(5))
for i in gen:
  print('gen:', i)


# 使用了多重赋值：a, b = b, a + b，在赋值时，右边的表达式会在赋值前被求值，因此，a 和 b 的值在赋值前就已经被计算出来了。
def fibonacci(n):
  a, b = 0, 1
  while a < n:
    yield a
    a, b = b, a + b 

for i in fibonacci(10):
  print('fibonacci:', i)
