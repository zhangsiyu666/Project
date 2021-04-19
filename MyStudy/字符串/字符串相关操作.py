'''
s='heLLo,Python'
print(s.swapcase())
print(s.capitalize())
'''

'''
s='hello ,world ,python!'
lst=s.split()
print(lst)
s1='hello*|world|python~*'
print(s1.split())
print(s1.split(sep='|'))
print(s1.split(sep='*'))
print(s1.split(sep='|',maxsplit=2))
#rsplit()从右侧开始劈分
print(s.rsplit())
'''


'''
s='hello ,world ,python!'
s1='123ABC'
print(s.isidentifier())
print(s.isspace())
print(s.isalpha())
print(s.isdecimal())
print(s.isnumeric())
print(s1.isalnum())

print(s.replace('python','Java'))
s2='hello,python,python,python'
print(s2.replace('python','Java',2))

print('============')
s3=['hello','world','python']
print(s3)
print('|'.join(s3))
print(''.join(s3))
print('*'.join('python'))
print('*'.join(s3))

print(s<s1)
print(ord('h'),ord('1'))
print(chr(104),chr(49))
#==与is区别，==比较的是value，is比较的是内存地址id（)
print('=================')

'''

s1='hello,python'
print(s1[:5]+'   切掉的部分')
print(s1[6:])
print(s1[:5]+'*'+s1[6:])
print('=====切片[start:end:step]=====')
print(s1[1:5:1]+'  切出来的部分')
print(s1[::2])
print(s1[::-1]+"  从最后一个元素开始到第一个元素")