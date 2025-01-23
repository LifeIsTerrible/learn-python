
# for循环
lst = ['a', 'b', 'c', 'd', 'e']

for i in lst:
  print('当前元素是：', i)

for i in range(3):
  print('当前range元素是：', i)


# while循环

i = 5
while i < 10:
  print('当前元素是：', i)
  i = i + 1

# 嵌套循环
for i in range(3):
  for j in range(2):
    print(f'i = {i}, j = {j}')


# 循环控制
for i in range(3):
  if i == 1:
    break
  print('break test: ', i)

for i in range(3):
  if i == 1:
    continue
  print('continue test: ', i)
  
  
# while-else
i = 0
while i < 3:
  print('while-else test: ', i)
  i = i + 1
else:
  print('while-else test end: ', i)
  
# for-else
for i in range(3):
  print('for-else test: ', i)
else:
  print('for-else test end: ', i)

