# 面向对象的三大特征
# 1.封装：提高程序的安全性
#     将数据（属性）和行为（方法）包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。这样，无需关心方法内部的具体实现细节，从而
#     隔离了复杂度。
#     在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被访问，前边使用两个“_”。
#
# 2.继承：提高代码的复用性
# 3.多态：提高程序的可扩展性和可维护性

#封装的实现
class Student:
    def __init__(self,age):
       self.age=age
    def get_age(self):
       return self.age
    def set_age(self,age):
        if 0<=age<=120:
            self.__age=age
        else:
            self.__age=18
stu1=Student(130)
stu2=Student(29)
print(stu1.get_age())
print(stu2.get_age())

#继承
#    语法格式： class 子类类名(父类名1,父类2...):
#                     pass
# 如果一个类没有继承任何类，则默认继承object
# Python支持多继承
# 定义子类时，必须在其构造函数中调用父类的构造函数

#继承代码的实现：
# class Person(Object):   #person继承object类 不写默认是object
#        def __int__(self,name,age):
#            self.name=name
#            self.age=age
#        def info(self):
#            print(self.name,self.age)
#
# class Students(Person):
#        def __init__(self,name,age,score):
#            super().__init__(name,age)
#            self.score=score
#
# class Teachers(Person):
#        def __int__(self,name,age,teachyears):
#            super().__init__(name,age)
#            self.teachyears=teachyears
#
# stu=Students("张三",20,100)
# stu.info()
# teacher3=Teachers("李四",30,8)
# teacher3.info()

#方法重写
'''
 1.如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其(方法体)进行重新编写
 2.子类重写后的方法中可以通过supoer().XXX()调用父类中被重写的方法
'''
#super().方法名字()


#object类
'''
1.object类是所有类的父类，因此所有类都有object类的属性和方法。
2.内置函数dir()可以查看指定对象的所有属性
3.object有个_str_()方法，用于返回一个对于“对象的描述”，对应于内置函数str()经常用于print()方法，帮我们查看对象的信息，所以我们经常会对
_str_()进行重写
'''

#多态
'''
多态就是具有多种形态，指的是即便不知道一个遍变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法，在运行过程中根据变量所引用对象
的类型，动态决定调用哪个对象中的方法
'''
class Animal():
    def eat(self):
        print('动物要吃东西')

class Cat(Animal):
    def eat(self):
        print('猫爱吃鱼')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Person:
    def eat(self):
        print('人吃五谷杂粮')
def fun(obj):
    obj.eat()
fun(Cat())
fun(Dog())
fun(Animal())
print('============')
fun(Person())

#静态语言和动态语言
'''
静态语言和动态语言的区别
静态语言实现多态的三个必要条件
1.继承
2.方法重写
3.父类引用指向子类对象
动态语言的多态崇尚“鸭子类型”，当看到一直鸟走起来像鸭子、游泳起来像鸭子、收起来像鸭子，那么这只鸟就可以被称为鸭子。在鸭子类型中，不需要关心
对象是什么类型，到底是不是鸭子，只关心对象的行为。
'''

#特殊方法和特殊属性
'''
特殊属性 __dict__ 获得类对象或实例对象所绑定的所有属性和方法的字典
特殊方法
__len__ 通过重写__len__方法，让内置函数len()的参数可以是自定义类型
__add__ 通过重写__add__方法，可使用自定义对象具有“+”功能
__new__ 用于创建对象
__init__ 对创建的对象进行初始化
'''

# class A:
#     def __init__(self,sex):
#         self.sex=sex
# class B:
#     pass
# class C(A,B):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# x=C('CASEY',18)        #是C类的一个对象
# print(x.__dict__)     #实例对象的属性字典
# print(x.__class__)    #输出了对象所属的类
# print(C.__dict__)
# print(C.__bases__)    #C类的所有父类放在了一个元组里
# print(C.__base__)     #哪个父类在前 输出哪个
# print(C.__mro__)      #查看C类继承了哪些父类
# print(A.__subclasses__())   #查看A类的子类


#类的浅拷贝和深拷贝
'''
变量的复制操作
只是形成两个变量，实际上还是指向同一个对象
浅拷贝
python的拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此，源对象与拷贝对象会引用同一个子对象
深拷贝
使用copy模块的deepcopy函数，递归拷贝赌侠凝重包含的子对象，源对象和拷贝对象所有的子对象也不同
'''
