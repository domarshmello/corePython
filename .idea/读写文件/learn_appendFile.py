# 测试append 新的内容到 文件里

append_text="\n追加内容append"

print("----test 对文件追加内容 ?----")
save_file=open('my_savePYFile.txt','a')
save_file.write(append_text)
save_file.close()