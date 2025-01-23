# print("请输入一个0-100之间的分数：")
# score = float(input("Enter Score: "))

# if score > 90:
#   grade = "A"
# elif score > 80:
#   grade = "B"
# elif score > 70:
#   grade = "C"
# elif score > 60:
#   grade = "D"
# else:
#   grade = "E"
  
# print("Grade: ", grade)

# 三元运算符
age = 20
status = "学生" if age < 18 else "成年人"
print(status)

# match-case

def get_season(month):
  match month:
    case 1 | 2 | 12:
      return "冬季"
    case 3 | 4 | 5:
      return "春季"
    case 6 | 7 | 8:
      return "夏季"
    case 9 | 10 | 11:
      return "秋季"
    case _:
      return "输入的月份不在1-12之间"

print(get_season(1))
print(get_season(13))


grade_dict = {
  "A": 90,
  "B": 80,
  "C": 70,
  "D": 60,
  "E": 50
}

print('A的分数是：', grade_dict["A"])
print('B的分数是：', grade_dict["B"])


# 嵌套的if-else

def check_login(username, password):
  if username:
    if password:
      return '登录成功'
    else:
      return '请输入密码'
  else:
    return '请输入用户名'

print(check_login("admin", "123456"))
print(check_login("admin", ""))


condition = True
condition1 = False
condition2 = False

if any([condition, condition1, condition2]):
  print("至少有一个条件为真")

if all([condition, condition1, condition2]):
  print("所有条件都为真")
else:
  print("至少有一个条件为假")


# 示例：根据用户类型执行不同操作
def handle_user(user_type):
    if user_type == "admin":
        pass  # 管理员逻辑还未实现
    elif user_type == "user":
        print("普通用户处理逻辑")
    else:
        print("未知用户类型")

handle_user("admin")
handle_user("user")
handle_user("unknown")


age = 20
match age:
  case 18:
    print('18岁')
  case 20:
    print('20岁')
  case _:
    print('其他')
