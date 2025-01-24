from enum import Enum, auto

class Person:
  sex = 'male' # 类属性
  
  def __init__(self, name, age, hobby):
    self.name = name # 实例属性
    # self.age = age
    self._protected = age
    self.__age = age
    self.__hobby = hobby

  def speak(self):
    print('Person speak called')
    return f'Person: {self.name}, {self._protected}, {self.__age}, {self.__hobby}'
  
  def get_private(self):
    return self.__age

p = Person('张三', 18, '篮球')
p1 = Person('李四', 20, '足球')

# print(p.speak())
# print(p1.speak())

# 私有属性不能直接访问
# print(p.__age)
print(p.get_private())

# 类属性可以被所有实例共享
print(p.sex)
print(p1.sex)
Person.sex = 'female'
print(p.sex)
print(p1.sex)

# 获取对象信息
print('type(p):', type(p)) 
print(isinstance(p, Person))
# print(dir(p))
print(hasattr(p, 'name'))
print(getattr(p, 'name'))


# 继承
class Student(Person):
  def __init__(self, name, age, hobby, score):
    super().__init__(name, age, hobby)
    self.score = score
  # 多态: 父类的方法可以被子类重写
  # 公有、保护都可以被继承，但是私有不能被继承，需要通过父类的方法获取，类属性可以被继承
  def speak(self):
    super().speak() # 调用父类的方法
    print('sex:', super().sex)
    return f'Student: {self.name}, {self._protected}, {self.get_private()}, {self.score}'


s = Student('王五', 20, '篮球', 90)
print('Student speak:', s.speak())
print('S:', s)


# 多继承
class Eat:
  def eat(self):
    print('Eat called')

class Sleep:
  def sleep(self):
    print('Sleep called')

class Person(Eat, Sleep):
  def speak(self):
    print('Person speak called')

p = Person()
p.eat()
p.sleep()
p.speak()

# __slots__: 限制实例的属性
class Animal:
  __slots__ = ('name', 'age')
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  


a = Animal('dog', 1)
# a.sex = 'male' # 报错，因为Animal类中__slots__限制了实例的属性
print('a.name:', a.name)
print('a.age:', a.age)



# property: 把方法变成属性
class Circle:
  def __init__(self, radius):
    self._radius = radius

  # getter
  @property
  def radius(self):
    return self._radius
  
  # setter
  @radius.setter
  def radius(self, value):
    if value < 0:
      raise ValueError('Radius must be positive')
    self._radius = value
  
  @property
  def area(self):
    print('area called')
    return self._radius ** 2 * 3.14

c = Circle(10)
print('c.radius:', c.radius)
c.radius = 20
print('c.radius:', c.radius)
print('c.area:', c.area)

# 定制类: 重写类的特殊方法，例如：__str__、__iter__

class MyList:
  def __init__(self, items):
    self.items = items

  def __iter__(self):
    print('__iter__ called')
    return iter(self.items)

  def __next__(self):
    print('__next__ called')
    return next(self.items)

  def __str__(self):
    print('__str__ called')
    return str(self.items)
  
  def __len__(self):
    print('__len__ called')
    return len(self.items)
  
list = MyList([1, 2, 3, 4, 5])
print('list:', list)
print('len(list):', len(list))  
it = iter(list)
print('next(it):', next(it))
print('next(it):', next(it))
print('next(it):', next(it))
print('next(it):', next(it))

print('str(list):', str(list))


# 枚举类: 枚举类可以用来定义一组常量
class Color(Enum):
  RED = auto()
  GREEN = auto()
  BLUE = auto()

print('Color.RED:', Color.RED, Color.RED.value, Color.RED.name)
print('Color.GREEN:', Color.GREEN, Color.GREEN.value, Color.GREEN.name)
print('Color.BLUE:', Color.BLUE, Color.BLUE.value, Color.BLUE.name)


# 元类: 元类是类的类，可以用来创建类，自定义元类可以添加属性或方法
class MetaClass(type):
  def __new__(cls, name, bases, attrs):
    print('MetaClass __new__ called')
    attrs['greet'] = lambda self: print('Hello, world!')
    return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MetaClass):
  pass

my = MyClass()
my.greet() # 输出：Hello, world!

