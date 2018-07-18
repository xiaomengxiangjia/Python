"""第一次打印时候读取整个文件"""
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
print("""-----------------------------""")

"""第二次打印时遍历文件对象"""
filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
print("""-----------------------------""")
        
"""第三次打印时将各行存储在一个列表中，再在with代码块外打印它们"""    
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())
