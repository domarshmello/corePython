
append_text="\n追加内容"

print("----test 对文件追加内容 ?----")
save_file=open('my_savePYFile.txt','a')
save_file.write(append_text)
save_file.close()