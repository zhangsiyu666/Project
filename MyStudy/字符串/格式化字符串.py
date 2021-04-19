name='casey'
age=18
print("我的名字叫%s,今年:%i岁"%(name,age))
#format方法
print("我的名字叫{0},今年:{1}岁,我真的叫{0}".format(name,age))
#string的方式/f来格式化字符串
print(f"我的名字叫{name},今年:{age}岁,我真的叫{name}")

#%10d表示输出的内容宽度为10
print('%10d' % 99)
print('%f' % 3.1415926)
#保留三位小数
print('%.3f' % 3.1415926)
#同时表示宽度和精度 %10.3f
print('%10.3f' % 3.1415926)

print("=========================")

print('{0}'.format(3.1415926))
#3表示一共三位数
print('{:0.3}'.format(3.1415926))
#3f表示的是三位小数
print('{:0.3f}'.format(3.1415926))
#同时设置宽度和精度
print('{:10.3f}'.format(3.1415926))




