num1 = 2
num2 = 3.14

print(num1 + num2)  # 5.14
print(f"{num1} + {num2} = {num1 + num2}")  # 2 + 3.14 = 5.14
print(f"Addition {num1 + 5}")
print(f"Subtraction {num1 - 5}")

a = num1.__pow__(2)  # 4
print('a:', a)
b = num2.__floor__()  # 4
print('b:', b)

# 字符串
s = 'Hello Python';
print(s.upper())
print(s.maketrans('H', 'J'))
print(s.find('P'))
print(s.replace('Python', 'World'))
print(s.split(' '))

# 容器
lst = [1, 2, 3, 4, 5];

print(lst[1])
print(len(lst))
print(lst.count(1))

lst.append(6)
print(lst)
lst.remove(6)
print(lst)
lst.extend([6, 7, 8])
print(lst)
lst.insert(2, 88)
print(lst)
lst.pop()
print(lst)
lst.reverse()
print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

# 元组
t = (1, 2, 1, 4, 5)
print(t)
print(t[1])
print(len(t))
print(t.count(1))
print(t.index(2))

# 布尔
is_active = True
is_big = False
if (is_active or is_big):
    print('Active')
else:
    print('Inactive')
    
if (not is_big):
    print('Not big')    
    
# 集合
d = {1,2,3}
d.add(4)
print(d)
d.remove(4)
print(d)
d.pop()
print(d)

d1 = {2,3,4}
d2 = {4,5,6}
print(d1 | d2)
print(d1 & d2)
print(d1 - d2)


# 字典
d = {'name': 'John', 'age': 25}
print(d)
print(d['name'])
print(d.get('age'))
print(d.keys())
print(d.values())

d.update({'name': 'Tom', 'home': 'USA'})
print('d:', d)