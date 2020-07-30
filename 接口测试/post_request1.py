import requests
import json
import time
from lala import *


content=""
#url='https://api.gunqiu.com/rollball-bar/chat/sendMessage'         #正式环境
#url='http://api.test.gunqiu.com/rollball-bar/chat/sendMessage'     #测试环境
url='https://api.gunqiu.com/rollball-bar/chat/sendMessage?'


payload = url+ 'channel=2&content='+content+'&contentType=1&gqchannel=appStore&pkg=xqty&platform=1&roomId=1&sourceId=0&sourceType=1&type=chatroom_anchor_gq&userId=107622&version=2.0.0'

#XQ 篮球聊天室
#payload = {"channel":'2', "content":'a', "contentType":'1', "pkg":'xqty', "platform":'1', "roomId":'2884', "sourceId":'0', "sourceType":'3', "type":'chatroom_match_basketball', "userId":'32', "version":'1.0.0'}    #值以字典形式传入

#XQ 足球聊天室
#payload = {"channel":'2', "content":'a', "contentType":'1', "pkg":'xqty', "platform":'1', "roomId":'1828555', "sourceId":'0', "sourceType":'2', "type":'chatroom_match_football', "userId":'7', "version":'1.0.0'}

#XQ 球吧直播间
payload = {
    "channel":'2',
    "content":'a',
    "contentType":'1',
    "pkg":'xqty',
    "platform":'1',
    "roomId":'1',
    "sourceId":'0',
    "sourceType":'1',
    "type":'chatroom_anchor_gq',
    "userId":'41737',
    "version":'1.0.0'
}


#data_josn= json.dumps(payload)#转换成json格式
#response = requests.post(url=url,data=data_josn)
for i in excel():
     print(i)
    # payload['content'] = i
    # response = requests.post(url=url, data=payload)
     content=i
     response = requests.post(url=payload)
     print(response.text)
# a=0
# while a<5:
#     payload['content'] = i
# #    payload['content'] = str(a)+'IP稍微yy'
#     response = requests.post(url=url,data=payload)
#     a +=1
#  #   time.sleep(1)  # 休眠1秒
# print(response.text)