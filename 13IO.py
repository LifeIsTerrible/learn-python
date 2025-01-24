# 文件读写
# r 读取文件
# w 写入文件
# a 追加文件
# rb 读取二进制文件
# wb 写入二进制文件
# ab 追加二进制文件
# t 文本模式
# b 二进制模式
# + 读写模式
# r+ 读写模式
# w+ 写读模式
# a+ 追加读写模式

with open('example.txt', 'r', encoding='utf-8') as file:
  # content = file.read()
  # print(content)
  for line in file:
    print(line.strip())
  
# 写入文件，如果文件不存在，则创建文件，如果文件存在，则覆盖文件
# with open('example.txt', 'w', encoding='utf-8') as file:
#   file.write('Hello, Python!')

# 追加文件，如果文件不存在，则创建文件，如果文件存在，则追加文件
with open('example.txt', 'a', encoding='utf-8') as file:
  file.write('\nHello, Python!')

  # 读取文件的前5行
  with open('example.txt', 'r', encoding='utf-8') as file:
    for i, line in enumerate(file):
      if i < 5:
        print(f'第{i+1}行: {line.strip()}')
      else:
        break
        
  # 读取文件的指定行
  with open('example.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(f'第2行内容: {lines[1].strip()}')
    
  # 读取文件的部分内容
  with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read(10)  # 读取前10个字符
    print(f'前10个字符: {content}')
    
  # 追加多行内容
  with open('example.txt', 'a', encoding='utf-8') as file:
    lines = ['\n新的一行1', '\n新的一行2']
    file.writelines(lines)
