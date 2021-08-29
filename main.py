import os
import re

import requests

username = os.getenv('USERNAME') #从secret中获取身份证号
password = os.getenv('PASSWORD') #从secret中获取密码
cid = str("ygd201706050003") #此处为康教练的coachID，届时请自行修改

# 登录并获取cookie
logon_url ="http://yyyxjtdjx.ay001.net/Server/AccountServer.asmx/MobileLogin"
logon_data = {
    "LoginType": "0",
    "UserName": username,
    "Password": password}
session = requests.Session()
cookie_jar = session.post(logon_url,logon_data).cookies
cook = requests.utils.dict_from_cookiejar(cookie_jar)
c_0 = str(cook)
c_1 = re.sub("{'ASP.NET_SessionId': '","",c_0)
c_2 = re.sub("'}","",c_1)
cookie = str(c_2)

#确定预约时间
import datetime  # 导入日期时间模块

today = datetime.date.today() #获得今天的日期
date = today + datetime.timedelta(days=4) #用今天日期加上时间差，参数为4天，获得4天后的日期  ps.Github使用的是GMT标准时间，所以要加4天
date = str(date)

# 抓取stateID
ck = {
    "ASP.NET_SessionId": cookie,
    "HidIsCard": "false",
    "password": "",
    "rmbUser": "false",
    "username": ""}
hd = {
    "Host":"yyyxjtdjx.ay001.net",
    "Connection":"keep-alive",
    "Content-Length":"58",
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "DNT":"1",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",
    "Content-Type":"application/json; charset=UTF-8",
    "Origin":"http://yyyxjtdjx.ay001.net",
    "Referer":"http://yyyxjtdjx.ay001.net/Page/index.htm?version=20160927",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cookie":"ASP.NET_SessionId="+cookie+"; HidIsCard=false; password=; rmbUser=false; username="}
data ={
    "coachID": cid, 
    "date": date,
    "subid": "0"}
url = 'http://yyyxjtdjx.ay001.net/Server/OrderCoachServer.asmx/GetTimesInfoByCoachIDNew'
response = requests.post(url,cookies=ck,headers=hd,json=data)
response.encoding = "utf-8"

# 将抓取到的列表进行处理，并分别提取出每项的stateID
f_1 = re.compile("\d{7},")
t_1 = f_1.findall(response.text)
f_2 = re.compile("\d{7}")
t_2 = f_2.findall(str(t_1))
globals().update({f"s{i+1}": t_2[i] for i in range(len(t_2))})

# 设置post请求参数
url ="http://yyyxjtdjx.ay001.net/Server/OrderCoachServer.asmx/orderCoachNew"
ck = {
    "ASP.NET_SessionId": cookie,
    "HidIsCard": "false"}
hd = {
    "Host":"yyyxjtdjx.ay001.net",
    "Connection":"keep-alive",
    "Content-Length":"46",
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "DNT":"1",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48",
    "Content-Type":"application/json; charset=UTF-8",
    "Origin":"http://yyyxjtdjx.ay001.net",
    "Referer":"http://yyyxjtdjx.ay001.net/Page/index.htm?version=20160927",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cookie":"ASP.NET_SessionId="+cookie+"; HidIsCard=false"}

# 发送http请求
while True:

    # 确保设置的时间段的顺序与你想要预约的优先级一致
    # No.1 08:10-08:50   ps.修改时建议连注释一并修改，以免误导   pps.不过这一行本身只是注释，其实改不改，甚至删除也无所谓(´-ι_-｀)
    dt2 = {
        "PXResID":"",
        "SubID":"2",  #如果要预约科三，请把此处的“2”改为“3”，下同
        "stateID":s3 #这里第n个时间段就更改为“sn”,例如这里是第三个时间段，也就是8:10-8:50，请根据实际需要修改
    }
    res2 = requests.post(url, json = dt2, headers = hd, cookies = ck)
    res2.encoding = "utf-8"
    print("08:10-08:50") #这一行代码用于输出时间段信息，修改上方sn（即时间段编号）时，建议一并修改这一行，使得与之相一致，以免误导
    pr = str(res2.text)
    print(pr)

    if pr == '{"d":{"Item1":false,"Item2":["预约时间段已经约满!"]}}':
        # No.2 07:30-08:10   ps.同样，为保持一致，建议一并修改
        dt2 = {
            "PXResID":"",
            "SubID":"2",
            "stateID":s2 #同理，目前这里是第二个时间段，也就是7:30-8:10，请根据实际需要修改
        }
        res2 = requests.post(url, json = dt2, headers = hd, cookies = ck)
        res2.encoding = "utf-8"
        print("07:30-08:10") #与上面一样，建议一并修改这一行，使得与之相一致，以免误导
        pr = str(res2.text)
        print(pr)
    
    if pr == '{"d":{"Item1":false,"Item2":["预约时间段已经约满!"]}}':
        # No.3 08:50-09:30  ps.改
        dt2 = {
            "PXResID":"",
            "SubID":"2",
            "stateID":s4 #记得改
        }
        res2 = requests.post(url, json = dt2, headers = hd, cookies = ck)
        res2.encoding = "utf-8"
        print("08:50-09:30") #这里也记得改
        pr = str(res2.text)
        print(pr)

    # 后续如果需要增加更多备选时间段，请按照以下格式在后面继续复制粘贴   ps.记得复制粘贴时保持缩进，并且记得去掉注释符（井号）
    # if pr == '{"d":{"Item1":false,"Item2":["预约时间段已经约满!"]}}':
    #     # No.4 xx:xx-xx:xx
    #     dt2 = {
    #         "PXResID":"",
    #         "SubID":"2",
    #         "stateID":sn
    #     }
    #     res2 = requests.post(url, json = dt2, headers = hd, cookies = ck)
    #     res2.encoding = "utf-8"
    #     print("xx:xx-xx:xx")
    #     pr = str(res2.text)
    #     print(pr)

    if pr == '{"d":{"Item1":false,"Item2":["预约时间段已经约满!"]}}':
        exit(1)
    # 所有备选时间段都满后，将抛出异常代码1并退出程序

    if pr == '{"d":{"Item1":false,"Item2":["还没到[05:50]点，预约尚未开始，您暂时无法预约!"]}}':
        continue

    if pr == '{"d":{"Item1":true,"Item2":null}}':
        exit()

    # 上面设定了哪些时间段，这里就也同样设定哪些时间段，确保顺序一致
    if pr == '{"d":{"Item1":false,"Item2":["您已经有[08:10-08:50]的预约记录!"]}}':  # 按照上面的顺序排列这里的时间
        exit()

    if pr == '{"d":{"Item1":false,"Item2":["您已经有[07:30-08:10]的预约记录!"]}}':
        exit()

    if pr == '{"d":{"Item1":false,"Item2":["您已经有[08:50-09:30]的预约记录!"]}}':
        exit()

    # 如果有，继续增加   ps.时间必须为xx:xx格式，例如8:50必须写成08:50
    # if pr == '{"d":{"Item1":false,"Item2":["您已经有[xx:xx-xx:xx]的预约记录!"]}}':
    #     exit()

    else :
        exit(2)
    # 出现其他情况，抛出异常代码2并退出程序
