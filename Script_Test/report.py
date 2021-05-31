import requests
import time
from datetime import date
from datetime import timedelta


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
before_time = ((date.today() - timedelta(365)).strftime("%Y-%m-%d"))
time = (time.strftime("%Y-%m-%d", time.localtime()))
xls_url = "https://control.zenlayer.com/zenlayer_web/finance/report/down_excel?report_id=110&start_date=%s&end_date=%s" %(before_time, time)
xls = requests.request("GET", xls_url, headers=headers, files=files)
file = open("/opt/report/%s~%s.xls" % (before_time, time), "wb")
for chunk in xls.iter_content(chunk_size=1024):
    if chunk:
        file.write(chunk)