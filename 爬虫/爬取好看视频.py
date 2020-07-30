import re
from bs4 import BeautifulSoup
import urllib.request
import requests
import random

def xiazai(url):
    url = str(url)
    # name = str(url)
    # name =random(1,100)
    fp = open(u'E:\\niu'+'/'+url[-20:], 'wb')
    html = requests.get(url,headers=header)
    fp.write(html.content)
    print('下载成功！')
    fp.close()

def fenlei(url):
    url = 'http://sv.baidu.com/'+url
    html = requests.get(url, headers=header)
    # print(html.txet)
    soup = BeautifulSoup(html.text, 'html.parser')
    # print(soup)
    all_a = soup.find('div', class_='video-list-inner').find_all('li')
    # print(all_a)
    # ss = soup.find('div', class_='video-tabs-wrapper').find_all('a')
    all_a = str(all_a)
    ss = re.findall('data-vsrc="(.*?mp4).*?',all_a,re.S)
    # print(ss)
    # ss = ss[0:2]+ss[-7:]
    list1 = []
    list2 = []
    list3 = []
    # for s in ss[0:3]:
    #     list1.append(s)
    for i in ss:
        cc = str(i)
    # ss = str(ss)
        cc = re.findall('data-vsrc="(.*?mp4)',cc,re.S)
        if cc !=[]:
            cc=cc
            list2.append(cc)
                # for a in ss[-6:]:
                #     a=a
                #     list3.append(a)
    list1 = ss[0:3]
    list3 = ss[-6:]
    aa =list1+list2+list3
    aa1 = aa[3]
    cc = aa[0:3]
    bb = aa[4:]
    aa = aa1 + cc +bb
    # print(aa)
    for sss in aa:
        # sss = sss
        # print(sss)
        xiazai(sss)
if __name__=='__main__':
    url = 'http://sv.baidu.com/'
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Request':'http://sv.baidu.com/'
    }
    html = requests.get(url,headers = header)
    soup = BeautifulSoup(html.text,'html.parser')
    ss = soup.find('div', class_='video-tabs-wrapper').find_all('a')
    for i in ss:
        url = i.attrs['href']
        # print(type(url))
        fenlei(url)