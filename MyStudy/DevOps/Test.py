'''ping测试网段内的主机'''
import os
import subprocess

def ping(host):
  result=subprocess.run(
      'ping -c2 %s &> /dev/null' % host, shell=True
  )
  if result.returncode==0:
      print('%s:UP' % host)
  else:
      pass
if __name__ == '__main__':
    ips = ['10.64.21.%s' % i for i in range(1,255)]
    for ip in ips:
        ret_val=os.fork()
        if not ret_val:
          ping(ip)
          exit()

'''使用forking脚本，在父进程重打印 in parent 然后睡眠10秒
在子进程中编写循环，循环五次，输出当前系统时间，每次循环结束后睡眠一秒
父子进程结束后，分别打印parent exit 和 child exit
'''
# import datetime
# import os
# import time
# theTime=datetime.datetime.now()
# print('starting')
# ret_val=os.fork()
# if ret_val: #非0为真、父进程
#     print('in parent')
#     time.sleep(10)
#     print('parent exit')
# else:
#     print('in child')
#     for i in range(1,6):
#         print(theTime)
#         time.sleep(1)
#     print('child exit')