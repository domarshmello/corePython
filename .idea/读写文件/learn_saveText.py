# 换行  \n
print("-----\n 换行 \n-----")
text='this is a test .\nthis is a second line '

print(text)

print("----test save file: w ？ r ? -----")
# 打开文件
save_file=open('my_savePYFile.txt','w')
# 内容写进文件
save_file.write(text)
# 关闭文件
save_file.close()
