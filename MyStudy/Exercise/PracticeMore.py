'''求斐波那契数列的第n项数字'''
# def fib(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# print(fib(6))
#
# for i in range(1,7):#求斐波那契数列前n项数字
#    print(fib(i))

'''Q1.....在2000-3200之间找到可以被7整除，但不是5的倍数的数字。得到的数字按照逗号间隔的顺序打印在一行。'''
# for i in range(2000,3200):
#     if (i%7==0) and (i%5!=0):
#         print(i,end=',')

# list=[]
# for i in range(2000,3200):
#     if (i%7==0) and (i%5!=0):
#         list.append(str(i))
# print(','.join(list))

'''Q2.....计算给定数字的阶乘，结果按照逗号间隔的顺序打印在一行上，假设通过控制台输入8，则输出40320'''
# def jiecheng(x):
#     if x==0:
#      return 1
#     return x*jiecheng(x-1)
# print('请输入一个数字:')
# x=int(input())
# print(jiecheng(x))

'''Q3......使用给定的整数n，生成一个包含(i，i*i)的字典，该字典包含1到n之间的整数（两者都包含），然后打印该字典。
例如输入4，输出 {1:1,2:4,3:9,4:16}
'''
# def zidian(n):
#     d = {a:a*a for a in range(1,n+1)}
#     return d
# print('请输入整数n:')
# n=int(input())
# print(zidian(n))
#
# print('请输入整数n:')
# n=int(input())
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)

'''Q4.....该程序接受控制台以以逗号分隔的数字序列，生成包含每个数字的列表和元组。
假设提供输入：34岁，67岁，55岁，33岁，12日，98年
则输出为：['34','67','55','33','12','98']
        ('34','67','55','33','12','98')      //可以将列表转换为元组
'''
# import re
# print('请输入你的包含数字的序列:')
# str=input()
# print(list(re.findall(r"\d+\.?\d*",str)))
# print(tuple(re.findall(r"\d+\.?\d*",str)))
#
# import re
# print('请输入你的包含数字的序列:')
# values=input()
# l=values.split(",")
# k=re.findall(r'[0-9]+',values)
# t=tuple(k)
# print(k)
# print(t)

'''Q5.....定义一个至少有两个方法的类：getString：从控制台输入获取字符串 printString：打印大写字母的字符串。
请包含简单的测试函数来测试类的方法。
提示：使用_init_方法来构造一些参数
'''
# class InputStr():
#     def __init__(self,str):
#         self.str=str
#     def getString(self):
#         print(self.str)
#     def printString(self):
#         print(self.str.upper())
# print('请输入字符串:')
# str1=input()
# str2=InputStr(str1)
# str2.getString()
# str2.printString()

# class InputOutString(object):
#     def __init__(self):
#         self.s=""
#     def getString(self):
#         print("请输入字符串:")
#         self.s=input()
#         print(self.s)
#     def printString(self):
#         print(self.s.upper())
# str0=InputOutString()
# str0.getString()
# str0.printString()

'''Q6.....编写程序，根据给定的公式计算并打印值Q=根号下2*C*D/H，以下是C和H的固定值，C=50，H=30，D是一个变量，它的值应该以逗号分隔
的序列输入到程序中。
假设输入序列是逗号分隔的：100,150,180,
程序输出为18,22,24
如果输出是个小数。则应四舍五入到最近的整数值。要求通过控制台输入。
'''
# import math
# C=50
# H=30
# print('输入整数，请以逗号间隔:')
# lst1=list(input().split(','))
# print(lst1)
# for i in lst1:
#      D=int(i)
#      result1=float(2*C*D/H)
#      result2=round(math.sqrt(result1))
#      print(result2,end=',')

# import math
# C=50
# H=30
# print('输入整数，请以逗号间隔:')
# value=[]
# iteams=[x for x in input().split(',')]
# for D in iteams:
#     value.append(str(int(round(math.sqrt(2*C*float(D)/H)))))

'''Q7.....编写程序，以2位数字，XY作为输入，生成一个二维数组，数组的第i行和第j列中的元素应该是i*j。
注意：i=0,1...,X-1; j=0,1,...,Y-1
假设输入3,5
则输出[[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]]
通过控制台输入,以逗号间隔
'''
#
# dimensions=[int(X) for X in input('请输入两个整数以逗号间隔').split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist=[[0 for col in range(colNum)] for row in range(rowNum)]
# for row in range(rowNum):
#      for col in range(colNum):
#          multilist[row][col]=row*col
# print(multilist)

# print('请输入两个整数以逗号间隔')
# number=input().split(',')
# list1=[int(x) for x in number]   #将输入的两个整数生成一个列表
# print(list1)
# rowNum=list1[0]
# colNum=list1[1]
# print(rowNum,colNum,type(rowNum))   #将取到的两个整数一个作为行，一个作为列
# mixList=[[0 for col in range(colNum)] for row in range(rowNum)]
# print(mixList)
# for row in range(rowNum):
#     for col in range(colNum):
#         mixList[row][col]=row*col
# print(mixList)

'''Q8.....编写程序，接受以逗号分隔的单词序列作为输入，按字母排序后按逗号分隔的序列打印单词。
假设输入without,hello,world,bag
则输出bag,hello,without,world
'''
# InStr=list(input('请输入单词序列以逗号分隔').split(','))
# lst1=sorted(InStr)
# print(lst1)
# print(",".join(lst1))  #将列表转化成字符串，并以逗号间隔输出

'''Q9.....编写一个程序，接受一行序列作为输入，并在将句子中的所有字符大写后打印行。
假设输入： Hello world
Practice make perfect
则输出：HELLO WORLD
PRACTICE MAKE PERFECT
'''
# lst=[]
# while True:
#     s=input()
#     if s:
#         lst.append((s.upper()))
#     else:
#         break
# for i in lst:
#     print(i)

'''Q10.....接受一系列以空格为分隔的单词作为输入，并在删除所有重复的单词按字母数字排序后打印。
假设输入：hello world and practice makes perfect and hello world again
则输出 again and hello makes perfect practice world
我们使用set容器自动删除重复数据，然后使用sort方法对数据进行排序
'''
# set1=set(input('请输入以空格为间隔的单词:').split(' '))
# lst1=list(set1)
# lst2=sorted(lst1)
# print(lst2)
# print(' '.join(lst2))

'''Q11.....接受一系列以逗号分隔的4位二进制数作为输入，然后检查它们是否可被5整除，可被5整除的以逗号间隔打印出来。
输入：0100,0011,1010,1001
那么输出：1010
'''
# Input=input('请输入以逗号间隔的一系列二进制数:').split(',')
# list1=[x for x in Input]
# print(list1)
# for i in list1:
#     num=int(i,2)
#     if num%5==0:
#         print(i)
#         # print(f'{i}可以被5整除',end=' ')
#     # else:
#         # print(f'{i}不能被5整除',end=' ')

'''Q12.....编写程序，输入一个范围，它将找到该范围的数字(均包括)满足每个数字的个十百千万位都是偶数。
获得的数字应以逗号分隔的顺序打印在一行
'''
# values=[]
# for i in range(1000,3001):
#         s = str(i)
#         if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
#             values.append(s)
# print(",".join(values))

'''Q13.....输入一个句子，计算字母和数字的个数。
假定输入 Hello world！ 123
则输出：
字母10
数字3
'''
# letter_count=0
# num_count=0
# InputStr=input('请输入字符串:')
# for i in InputStr:
#     if i.isdigit():
#         num_count+=1
#     elif i.isalnum():
#         letter_count+=1
# print('字母个数为:',letter_count)
# print('数字个数为:',num_count)

# print('请输入：')
# s = input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print ("LETTERS", d["LETTERS"])
# print ("DIGITS", d["DIGITS"])

'''Q14......编写程序计算大写字母和小写字母的个数
假设输入：Hello world！
输出为
大写实例 1
小写实例 9
'''
# InputStr=input('请输入字符串:')
# d={"大写实例":0,"小写实例":0}
# for i in InputStr:
#     if i.isupper():
#         d["大写实例"]+=1
#     elif i.islower():
#         d["小写实例"]+=1
#     else:
#         pass
# print("大写实例",d["大写实例"])
# print("小写实例",d["小写实例"])

'''Q15.....编写程序计算a+aa+aaa+aaaa的值。
假设输入9，则输出11106
'''
# InputStr=input('请输入数字:')
# a=InputStr
# n1=int("%s" % a)
# n2=int("%s%s" % (a,a))
# n3=int("%s%s%s" % (a,a,a))
# n4=int("%s%s%s%s" % (a,a,a,a))
# print(n1+n2+n3+n4)

'''Q16......使用列表推导列表中的每个奇数，该列表由一系列逗号分隔的数字输入。
假设输入1,2,3,4,5,6,7,8,9
那么输出1,3,5,7,9
'''
# lst1=list(input("请输入逗号间隔的数字:").split(","))
# str1=''
# for i in lst1:
#      if int(i)%2==0:
#          pass
#      else:
#        str1+='{},'.format(i)
# print(str1[:-1])

# lst1=list(input("请输入逗号间隔的数字:").split(","))
# str1=[]
# for i in lst1:
#     if int(i) % 2 == 0:
#         pass
#     else:
#         str1.append(i)
# print(','.join(str1))

# print("请输入逗号间隔的数字:")
# values=input()
# num=[x for x in values.split(',') if int(x)%2 !=0]
# print(','.join(num))

'''Q17.....根据控制台输入的事务日志计算银行账户的净金额，事务日志格式：D 100 W 200
D表示存款,W表示提款
假设输入:
D 300
D 300
W 200
D 100
输出为
500
'''
# s_account=0
# while True:
#     print('请输入存/取款金额:')
#     InputStr=input()
#     if not InputStr:
#         break
#     values=InputStr.split(' ')   #values是一个列表，以空格为间隔，来取InputStr字符串内的元素
#     print(values)
#     operation=values[0]
#     account=int(values[1])
#     if operation=='D':
#       s_account+=account
#     elif operation=='W':
#       s_account-=account
#     else:
#         pass
# print(s_account)

'''Q18.....要求用户输入用户名和密码进行注册。编写程序以检查用户输入的密码合规性。
要求密码 a-z至少有一个字母，0-9至少有一个数字，A-Z至少有一个字母， $#@至少有一个字符 最短密码长度为6 最大长度为12
接受一系列密码输入，并以逗号间隔。将符合条件的密码输出：
假设输入的是 ABd1234@1,F1#,2w3E*,2We3345
输出应该是 Abd1234@1
'''
# import re
# values=[]
# print('请输入密码:')
# items=[x for x in input().split(",")]
# for i in items:
#    if len(i)>6 and len(i)<12:
#        if re.search("[a-z]",i):
#            if re.search("[A-Z]",i):
#                if re.search("[0-9]",i):
#                   if  re.search("[@#$]", i):   # if re.search(["\s"],i):
#                           values.append(i)
#    else:
#        pass
# print(",".join(values))

'''Q19.....编写程序，按照升序对(名称,年龄,高度)元组进行排序,其中name是字符串,age和height是数组。
通过控制台输入,排序标准是1.根据名称排序 2.根据年龄排序 3.按照分数排序
优先级name》age》得分
假如输入：
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
那么输出应该是：[（'John'，'20'，'90'），（'Jony'，'17'，'91'），（'Jony'，'17'，'93'），（'Json'，'21 '，'85'），（'Tom'，'19'，'80'）]
'''
# from operator import itemgetter,attrgetter
# lst1=[]
# while True:
#   InputStr=input('请输入名称/年龄/身高并以逗号间隔:').split(',')
#   if not InputStr:
#       break
#   lst1.append(tuple(InputStr))
# print(sorted(lst1, key=itemgetter(0,1,2)))


'''Q20.....使用生成器定义一个类，该生成器可以在给定范围0和n之间迭代可被7整除的数字。
考虑使用yield
'''
# def putNumbers(n):
#     i = 0
#     while i < n:
#         j = i
#         i = i + 1
#         if j % 7 == 0:
#             yield j          #yield的用法类似于return,但不同的是yield每次返回结果之后函数并不会退出,而是保留当前运行状态
# for i in putNumbers(100):
#      print(i,end=',')

'''Q21.....机器人从原点（0,0）开始在平面中移动。 机器人可以通过给定的步骤向上，向下，向左和向右移动。 机器人运动的痕迹如下所示：
UP 5
DOWN 3
LETF 3
RIGHT 2
方向之后的数字是步骤。 请编写一个程序来计算一系列运动和原点之后距当前位置的距离。如果距离是浮点数，则只打印最接近的整数。
例：如果给出以下元组作为程序的输入：
UP 5
DOWN 3
LETF 3
RIGHT 2
然后，程序的输出应该是：2
'''

'''Q22.....题：编写一个程序来计算输入中单词的频率。 按字母顺序对键进行排序后输出。
假设为程序提供了以下输入：
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
然后，输出应该是：
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''

'''Q23.....题：Python有许多内置函数，如果您不知道如何使用它，您可以在线阅读文档或查找一些书籍。 
但是Python为每个内置函数都有一个内置的文档函数。
请编写一个程序来打印一些Python内置函数文档，例如abs（），int（），raw_input（）
并为您自己的功能添加文档
提示：内置文档方法是__doc__
'''
print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)
def square(n):
    return n**2
print(square(2))
print(square.__doc__)
