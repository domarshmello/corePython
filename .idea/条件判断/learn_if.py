# python高级 if true: run code(tab 严谨的结构语言)
x=1
y=2
z=3
q=1
if x<y<z:
    print('x 比 y 小 , y 比 z 小')
elif x<y>z:
    print(" condition 为false 不输出")
    
if x<z:
    print(" x 比 z  小 ")

print("--- x==q ? -----")
if x==q:
    print('判断 x与q相等 则输出')

print("--- x!=z ? -----")
if x!=z:
    print('判断 x与z 不相等 ')
else:
    print("判断 x与z 相等 ")
