import re

text = '身高：178; 体重：60kg; 学号：123456; 密码：12345678, 电话：15880088888 座机 0511-88668866'

print(re.findall(r'12',text))
print(re.findall(r'\d',text)) #数字类
print(re.findall(r'\d+',text)) #1到多个数字
print(re.findall(r'\d{3}',text)) #{n}个数字
print(re.findall(r'\d{4}-\d{8}',text)) #组合的
print(re.findall(r'\d{4}-\d{8}|1\d{10}',text)) # | 表示或

text2 = '15880088777 身高：178; 体重：60kg;座机 0511-88667777 学号：123456; 密码：12345678, 电话：15555662222 座机 0511-88668866'

print(re.findall(r'^\d{4}-\d{8}|^1\d{10}',text2)) # ^ 开头
print(re.findall(r'\d{4}-\d{8}$|1\d{10}$',text2))  # $ 结尾

text3 = 'barbar catcat haiher'

print(re.findall(r'(\w{3})(\1)',text3))  #  ()为一组   内部限制
print(re.findall(r'\d{4}-\d{8}$|1\d{10}$',text3)) 






# *
# ?
# {n,m}

