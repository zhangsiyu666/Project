import wget
import requests
import os
import hashlib
import tarfile

def esit_new_ver(ver_fname, ver_url):
    # 如果本地没有版本文件，那么肯定存在新版本，需要从url拉取，直接返回Ture，后面的代码就不执行了
    if not os.path.exists(ver_fname):
        return  True
    #本地有版本文件才执行下面的内容
    #将新版本文件存在r.text内
    with open(ver_fname) as fobj:
        local_ver = fobj.read()
    r = requests.get(ver_url)
    #比较本地版本文件和远程版本文件，如果不一致那么存在新版本文件
    if local_ver != r.text:
        return True
    else:
        return False

def file_ok(fname,md5url):
    #如果文件未损坏，返回ture，否则返回false
    m=hashlib.md5()
    with open(fname,'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    r = requests.get(md5url)
    if m.hexdigest() == r.text.strip():
        return True
    else:
        return False

def deploy(app_fname,deploy_dir,dest):
    #用于部署软件到WEB服务器
    #解压
    tar = tarfile.open(app_fname)   #打开压缩包
    tar.extractall(path=deploy_dir)
    tar.close()
    #拼接出解压后目录的绝对路径
    app_dir = os.path.basename(app_fname)
    app_dir = app_dir.replace('tar.gz','')
    app_dir = os.path.join(deploy_dir,app_dir)
    #创建链接
    if os.path.exists(dest):
        os.remove(dest)
    os.symlink(app_dir,dest)

if __name__ == '__main__':
    #判断服务器上是否有新版本
    ver_url = 'http://zsy.jenkins.zenlayer.online/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not esit_new_ver():
        print("未发现新版本")
        exit(1)

    #如果有新版本 DOWLOAD NEW VERSION
    r=requests.get(ver_url)
    app_url = 'http://zsy.jenkins.zenlayer.online//deploy/mysite-%s.tar.gz' % r.text
    download_dir='/var/www/download'
    app_fname = '/var/www/download/mysite-%s.tar.gz' % r.text
    wget.download(app_url,download_dir)

    #校验软件包是否损坏,如果损坏则删除;
    md5url = app_url+'.md5'
    if not file_ok(app_fname,md5url):
        print("文件已损坏")
        os.remove(app_fname)
        exit(2)

    #部署软件
    deploy_dir="/var/www/deploy"
    dest = "/var/www/html/current"
    deploy(app_fname,deploy_dir,dest)

    #更新本地版本文件
    if os.path.exists(ver_fname):
        os.remove(ver_fname)
    wget.download(ver_url,ver_fname)