# 类与对象
# 数据类型：
# 不同的数据类型属于不同的类
# 使用内置函数查看数据类型 type()
# 对象：
# 100/99/520都是int类之下包含的相似的不同个例，这个个例专业术语称为实例或对象
'''python中一切皆为对象  如字典、列表、字符串、元组等'''

#类的创建:
#类的组成：类属性、实例方法、静态方法、类方法
class Student():  #student为类的名称，可以由一个或者多个单词组成，要求每个单词的首字母大写，其余小写。
    native_place='吉林'  #直接写在类里面的变量称为类属性
    def __init__(self,name,age):
        self.name=name  #self.name称为实例属性，在这里进行了赋值的操作，将局部变量name的值赋给了实体属性
        self.age=age

    #在类里面定义的方法称为实例方法，在类之外定义的称为函数
    def eat(self):
        print('学生在吃饭..')

    #定义一个静态的方法
    @staticmethod
    def method():
        print('使用了staticmethod进行修饰，因此我是静态的方法')

    #定义一个类方法
    @classmethod
    def cm(cls):
        print('使用了classmethod进行修饰，因此我是类方法')

def drink():         #这是一个定义在类外的函数
    print('喝水')

#Python中一切皆为对象，Student为对象吗？有内存空间吗？
#创建Student类的对象
stu1=Student('ZSY',20)
stu1.eat()  #对象名.方法
print(stu1.name)
print(stu1.age)
Student.eat(stu1)  #和stu1.eat()  功能相同，都是调用Student类中的eat方法；类名.方法名（类的对象），实际上就是方法定义处的self
# print(id(stu1))
# print(type(stu1))
# print(stu1)  #输出和id的内存值为十六进制转换关系
# print('=======================')
# print(type(Student))
# print(id(Student))
# print(Student)

#类属性的使用方式
print(Student.native_place)
stu2=Student('ZHANGSAN',20)
stu3=Student('LISI',22)
print(stu2.native_place)
print(stu3.native_place)
Student.native_place='北京'  #更新了Student类中的类属性
print(stu2.native_place)    #变成北京  stu2的指针指向Student类中的类属性//此时已经更新
print(stu3.native_place)    #变成北京

#类属性、类方法、静态方法
'''
类属性：类中方法外的变量称为类属性，被该类的所有独享所共享
类方法：使用classmethod修饰的方法，使用类名直接访问的方法
静态方法：使用staticmethod修饰的方法，使用类名直接访问的方法
'''
print('----类方法的使用----')
Student.cm()
Student.method()

#Pyhon是动态语言，在创建对象后，可以动态绑定属性和方法
def show():
    print('我是一个函数')
stu=Student('JACK',20)
stu.gender='男'
print(stu.name,stu.age,stu.gender)
stu.show=show
stu.show()