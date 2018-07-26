# 创建一个文件file存储自己刚创建的文件my_savePYFile.txt 并打开
file =open('my_savePYFile.txt','r')
# 读取文本内容输出
# content=file.read()
# print(content)

content_line=file.readlines()
print("------ readlines() ？读取文本内容存取到 list---------")
print(content_line)
file.close()

# python_list=[1,4,5,7,8,"domarshmello"]
# list_content=file.readline()
# print(list_content)