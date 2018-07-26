# 引入时间模块 提前加载好到脚本里 --->才可以使t用time模块的功能

# import time  1：提前加载好到脚本里 --->才可以使t用time模块的功能
# import time as t   2： 长的模块名 命名为别名 t

print("-----   第一种形式   import time  ----")
import time
print("此时我的时区的现在的时间：",time.localtime())


print("———————----第2种形式  from time import time, localtime ——————")
from time import time,localtime
print(localtime())
print('------------第3种形式  from time import * -----------------')
from time import *
print(gmtime())

