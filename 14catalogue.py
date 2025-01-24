import os;
import pickle;

# 获取当前工作目录
print(os.getcwd())

print(os.listdir())

# 检查目录是否存在，如果不存在则创建
if not os.path.exists('test_dir'):
    os.mkdir('test_dir')

if os.path.exists('test_dir'):
    print('目录已存在')
else:
    print('目录不存在')

# 在test_dir目录下创建并写入文件
test_file_path = os.path.join('test_dir', 'test.txt')
with open(test_file_path, 'w', encoding='utf-8') as file:
    file.write('这是test_dir目录下的测试文件内容')

# 验证文件是否创建成功
if os.path.exists(test_file_path):
    print('文件创建成功')
    # 读取文件内容
    with open(test_file_path, 'r', encoding='utf-8') as file:
        print('文件内容:', file.read())
else:
    print('文件创建失败')

# # 删除文件
# os.remove('data.pkl')

# 删除目录
# os.removedirs('test_dir')



# 文件序列化: 将数据序列化后写入文件，然后从文件中反序列化数据
data = {'name': '张三', 'age': 20}

with open('data.txt', 'wb') as file:
  pickle.dump(data, file)

with open('data.txt', 'rb') as file:
  data = pickle.load(file)
  print('反序列化后的数据:', data)
