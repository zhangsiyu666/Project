'''
urllib中包含了四个模块
urllib.request 可以用来发送request请求和获取request的结果
urllib.error包含了urllib.request产生的异常
urllib.parse用来解析和处理URL
urllib.robotparse用来解析页面的robots.txt文件

爬取网页：
先需要导入到的模块：urllib.request
在导入了模块之后，我们需要使用urllib.request.urlopen打开并爬取一个网页
读取内容常见的三种格式：
read()读取文件的全部内容，与readlines()不同的是，read()会把读取到的内容赋给一个字符串变量
readlines()读取文件的全部内容，readlines()会把读取到的内容赋值给一个列表变量
readline()读取文件的一行内容
'''
import urllib.request
html1 = urllib.request.urlopen(r'http://www.python.org')
print(html1.read(100))
print(html1.read(100).decode())
print('================================================')
print(html1.readline())
print('================================================')
print(html1.readlines())
html1.close()
123