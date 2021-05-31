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

login_user = {'user': 'luke.xi',
              'pass': 'XiwangXW.1995',
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
xls_url = "https://control.zenlayer.com/zenlayer_web/workorder/export_wolist?1=1&updatetime=0&create_begin_time=2021-01-01%2000:00:00&fac_id=&code="
xls = requests.request("GET", xls_url, headers=headers, files=files)
file = open("/opt/oss_testwo/pmysql.xls", "wb")
for chunk in xls.iter_content(chunk_size=1024):
    if chunk:
        file.write(chunk)
file.close()


try:
    book = xlrd.open_workbook("/opt/oss_testwo/pmysql.xls")  # 文件名，把文件与py文件放在同一目录下
except:
    print("open excel file failed!")
try:
    sheet = book.sheet_by_name("total1")  # execl里面的worksheet1
except:
    print("locate worksheet in excel failed!")

# 连接数据库
database = pymysql.connect(host = "127.0.0.1", port = 33306, user = "wo_statistics",
        passwd = "j5kmAJbKhjdwAKpm",
        db = "wo_statistics",
        charset = 'utf8')
cursor = database.cursor()


for i in range(1, sheet.nrows):
    work_order = "Code"
    wo_type = "Title"
    remark = "Label"
    customer_id = "CID"
    client_name = "Client Name"
    creat_user = "Create User"
    creat_time = "Create Time"
    dc_location = "Data Center"
    wo_status = "Status"
    project_management = "PM"
    content = "Content"
    current_step = "Current Step"
    current_group = "Current Group"
    last_update = "Last Update"
    eta = "E.T.A"
    delivery_date = "Delivery Date"
    billing_start_date = "Billing Start Date"
    send_time = "Send time"
    eta_notes = "ETA notes"
    eta_finish_rate = "ETA Finish Rate"
    deal_hours = "deal hours"
    total_hours = "total hours"
    rate = "rate"


    work_order = sheet.cell(i, 0).value
    wo_type = sheet.cell(i, 1).value
    remark = sheet.cell(i, 2).value
    customer_id = sheet.cell(i, 3).value
    client_name = sheet.cell(i, 4).value
    creat_user = sheet.cell(i, 5).value
    creat_time = sheet.cell(i, 6).value
    dc_location = sheet.cell(i, 7).value
    wo_status = sheet.cell(i, 8).value
    project_management = sheet.cell(i, 9).value
    content = sheet.cell(i, 10).value
    current_step = sheet.cell(i, 11).value
    current_group = sheet.cell(i, 12).value
    last_update = sheet.cell(i, 13).value
    eta = sheet.cell(i, 14).value
    delivery_date = sheet.cell(i, 15).value
    billing_start_date = sheet.cell(i, 16).value
    send_time = sheet.cell(i, 17).value
    eta_notes = sheet.cell(i, 18).value
    eta_finish_rate = sheet.cell(i, 19).value
    deal_hours = sheet.cell(i, 20).value
    total_hours = sheet.cell(i, 21).value
    rate = sheet.cell(i, 22).value

    value = (work_order, wo_type, remark, customer_id, client_name, creat_user, creat_time, dc_location, wo_status, project_management, content, current_step, current_group, last_update, eta, delivery_date, billing_start_date, send_time, eta_notes, eta_finish_rate, deal_hours, total_hours, rate)
    db_sql = "REPLACE INTO `wo_basic_data`  (`Code`, `Title`, `Label`, `CID`, `Client Name`, `Create User`, `Create Time`, `Data Center`, `Status`, `PM`, `Content`, `Current Step`, `Current Group`, `Last Update`, `E.T.A`, `Delivery Date`, `Billing Start Date`, `Send time`, `ETA notes`, `ETA Finish Rate`, `deal hours`, `total hours`, `rate`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
    print(db_sql)
    cursor.execute(db_sql, value)
    database.commit()
database.close()