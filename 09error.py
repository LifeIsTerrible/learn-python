# 错误和异常: 错误和异常是程序运行过程中出现的错误或异常情况，可以通过try、except、finally、raise等语句来处理

# try: 尝试执行代码，如果发生异常，则跳转到except语句
# except: 处理异常
# finally: 无论是否发生异常，finally语句都会执行
# raise: 抛出异常


def divide(a, b):
  try:
    result = a / b
  except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
    raise
  except ValueError as e:
    print('ValueError:', e)
    raise
  else:
    print(f'{a} / {b} = {result} called')
    return result
  finally:
    print('finally called')

print(divide(10, 2))
# print(divide(10, 0))
# print(divide(10, 'a'))


# try:
#   num = int(input('Enter a number: '))
#   result = 10 / num
# # 捕获多个异常
# except (ValueError, TypeError) as e:
#   print(f'Error: {e}')
# else:
#   print(f'10 / {num} = {result}')
# finally:
#   print('finally called')


# 自定义异常
class MyException(Exception):
  def __init__(self, message):
    self.message = message

def divide1(a, b):
  if b == 0:
    raise MyException('b can not be 0!!!')
  return a / b

print(divide1(10, 0))
