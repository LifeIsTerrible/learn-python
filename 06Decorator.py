from functools import wraps

# 简单装饰器
def simple_decorator(func):
  def wrapper():
    print('before')
    func()
    print('after')
  return wrapper

@simple_decorator
def my_function():
  print('my_function')

# 带参数的装饰器
def decorator_with_args(func):
  def wrapper(*args, **kwargs):
    print(f'decorator_with_args before: {args}, {kwargs}')
    result = func(*args, **kwargs)
    print(f'decorator_with_args after: {args}, {kwargs}')
    return result
  return wrapper

@decorator_with_args
def add(a, b):
  print(f'add: {a}, {b}')
  return a + b

# 多个装饰器
def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def text():
    return "Hello World"

# 装饰器工厂
def repeat(num_times):
  def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(num_times):
        result = func(*args, **kwargs)
      return result
    return wrapper
  return decorator

@repeat(num_times=3)
def greet(name):
  """Greets the user."""
  print(f"Hello, {name}!")

if __name__ == '__main__':
  print('my_function test:')
  my_function()
  print('add test:')
  print(add(1, 2))
  print('text test:')
  print(text())
  print('greet test:')
  greet('Alice')
  print('greet:', greet.__name__, greet.__doc__)


