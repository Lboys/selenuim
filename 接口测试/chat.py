import requests
import json
import time
from lala import *



url='https://www.heibaizhibo.com/chat/user/speak'

headers={"token":'c6YikbkQMW0hXLpxdo9FXGlCMHnanUwlIzt7n4bPCFPQbF5zDhRX5Ow2ylcnd4iWnzwIJnvDuymKh3TJxME0q2yn',"platform":'3','Content-Type': 'application/json;charset=UTF-8'}

payload = {
	"user_id": 32,
	"content": "Yyy",
	"type": 1
}
#payload = {"channel":'2', "content":'a', "contentType":'1', "pkg":'xqty', "platform":'1', "roomId":'2884', "sourceId":'0', "sourceType":'3', "type":'chatroom_match_basketball', "userId":'32', "version":'1.0.0'}    #值以字典形式传入

#XQ 足球聊天室
#payload = {"channel":'2', "content":'a', "contentType":'1', "pkg":'xqty', "platform":'1', "roomId":'1828555', "sourceId":'0', "sourceType":'2', "type":'chatroom_match_football', "userId":'7', "version":'1.0.0'}

#XQ 球吧直播间
# payload = {
#     "channel":'2',
#     "content":'a',
#     "contentType":'1',
#     "pkg":'xqty',
#     "platform":'1',
#     "roomId":'1',
#     "sourceId":'0',
#     "sourceType":'1',
#     "type":'chatroom_anchor_gq',
#     "userId":'41737',
#     "version":'1.0.0'
# }


# data_josn= json.dumps(payload)#转换成json格式
# response = requests.post(url=url, data=data_josn)
for i in excel():
	print(i)
	payload["content"] = i
	payload["content"] = i
	response = requests.post(headers=headers,url=url, data=json.dumps(payload))
#     time.sleep(1)  # 休眠1秒
	print(response.text)


