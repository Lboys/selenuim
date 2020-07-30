# -*- coding:utf-8
import requests

#豆瓣搜索功能
param={"q":"西游记"}

#请求豆瓣首页
r = requests.get("https://www.douban.com/search",params=param)

#打印状态吗
print(r.status_code)

#打印url
print(r.url)


#打印文本
print(r.text)

print(r.headers)