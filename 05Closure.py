# 计算器闭包案例
def create_counter():
  count = 0
  def counter():
    nonlocal count
    count += 1
    return count
  return counter

counter = create_counter()
print(counter())  # 输出：1
print(counter())  # 输出：2
print(counter())  # 输出：3

# 不受第一个 counter 的影响，因为闭包是独立的
counter2 = create_counter()
print(counter2())  # 输出：1
print(counter2())  # 输出：2
print(counter2())  # 输出：3


# 计算平均值
def make_averager():
  nums = []
  def add_num(new_num):
    nums.append(new_num)
    return sum(nums) / len(nums)
  return add_num

avg = make_averager()
print(avg(10))  # 输出：10
print(avg(11))  # 输出：10.5
print(avg(12))  # 输出：11
