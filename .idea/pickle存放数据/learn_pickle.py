# pickle读写程序
import pickle
a_dict={'da':1,2:[1,2,3],'apple':{1:'little',2:'big'}}
# 打开并创建 pickle_example.pickle

# file =open('pickle_example.pickle','wb')
# 想象pickle是挖土车，装载的是a_dict。倒到file里
# pickle.dump(a_dict,file)
# file.close()

print('--------1----------')
# day2:已读的形式rb打开
file =open('pickle_example.pickle','rb')
a_dict1=pickle.load(file)
file.close()
print(a_dict1)

print('--------2-----------')
# 第2种简单的形式打开 with
with open('pickle_example.pickle','rb')as file:
    a_dict1=pickle.load(file)
    print(a_dict1)