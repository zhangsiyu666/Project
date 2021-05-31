from datetime import date
from datetime import timedelta
import requests
import xlrd
import pymysql


def get_JES():
    url = "https://control.zenlayer.com/zenlayer_web/login"
    payload = {}
    session = requests.Session()
    session.get(url, data=payload)
    ts = session.cookies.get_dict()
    jes = ts['JSESSIONID']
    print(jes)
    return jes


login_url = "https://control.zenlayer.com/zenlayer_web/login/tologin"

login_user = {'user': 'xxxx',
              'pass': 'xxxx',
              'time_zone': '8',
              'op': '0'
              }
files = [
]
jess = get_JES()
jes = 'JSESSIONID={}; lang=en'.format(jess)
headers = {
    'Cookie': jes
}

response = requests.request("POST", login_url, headers=headers, data=login_user, files=files)
pre_time = ((date.today() + timedelta(1)).strftime("%Y-%m-%d"))
print(pre_time)
xls_url = "https://control.zenlayer.com/zenlayer_web/finance/report/down_excel?report_id=110&start_date=2018-01-01&end_date=%s" % pre_time
xls = requests.request("GET", xls_url, headers=headers, files=files)
file = open("mysql.xls", "wb")
for chunk in xls.iter_content(chunk_size=1024):
    if chunk:
        file.write(chunk)
file.close()

try:
    book = xlrd.open_workbook("mysql.xls")  # 文件名，把文件与py文件放在同一目录下
except:
    print("open excel file failed!")
try:
    sheet = book.sheet_by_name("rows1")  # execl里面的worksheet1
except:
    print("locate worksheet in excel failed!")

# 连接数据库
database = pymysql.connect(host = "127.0.0.1", port = 33306, user = "report",
        passwd = "**********",
        db = "report",
        charset = 'utf8')
cursor = database.cursor()


for i in range(1, sheet.nrows):
    work_order = "id"
    solution_type = "Title"
    remark = "Label"
    customer_id = "CID"
    client_name = "Client Name"
    dc_region = "DC地理位置"
    sales_region = "销售区域"
    sales = "对应销售"
    creat_user = "Create User"
    creat_time = "Create Time"
    dc_location = "Data Center"
    work_order_status = "status"
    current_step = "Current Step"
    current_group = "Current Group"
    last_update = "Last Update"
    deploy_time = "交付时间（creat_time -->返回销售 / 销售确认)"
    recycle_time = "交付时间（返回销售 -->工单结束)"
    deploy_status= "交付状态"

    work_order = sheet.cell(i, 0).value
    solution_type = sheet.cell(i, 1).value
    remark = sheet.cell(i, 2).value
    customer_id = sheet.cell(i, 3).value
    client_name = sheet.cell(i, 4).value
    dc_region = sheet.cell(i, 5).value
    sales_region = sheet.cell(i, 6).value
    sales = sheet.cell(i, 7).value
    creat_user = sheet.cell(i, 8).value
    creat_time = sheet.cell(i, 9).value
    dc_location = sheet.cell(i, 10).value
    work_order_status = sheet.cell(i, 11).value
    current_step = sheet.cell(i, 12).value
    current_group = sheet.cell(i, 13).value
    last_update = sheet.cell(i, 14).value
    deploy_time = sheet.cell(i, 15).value
    recycle_time = sheet.cell(i, 16).value
    deploy_status = sheet.cell(i, 17).value
    value = (work_order, solution_type, remark, customer_id, client_name, dc_region, sales_region, sales, creat_user, creat_time, dc_location, work_order_status, current_step, current_group, last_update, deploy_time, recycle_time, deploy_status)
    db_sql = "REPLACE INTO `test`  (`id`, `Title`, `Label`, `CID`, `Client Name`, `DC地理位置`, `销售区域`, `对应销售`, `Create User`, `Create Time`, `Data Center`, `status`, `Current Step`, `Current Group`, `Last Update`, `交付时间（creat_time-->返回销售/销售确认)`, `交付时间（返回销售-->工单结束)`, `交付状态`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
    print(db_sql)
    cursor.execute(db_sql, value)
    database.commit()
database.close()