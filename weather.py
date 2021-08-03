import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import json
import random
import time
from xpinyin import Pinyin

def url_open(url):
    try:
        head =\
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/521.36',
            }
        req = requests.get(url,headers=head).content.decode()

        return req
    except:
        return '0'

def get_wea(name='嘉定'):
    wea_str=""
    id=get_city(name)
    if id==0:
        wea_str="没有找到这个地区耶"
        return wea_str
    else:
        url='http://www.weather.com.cn/weather/'+str(id)+'.shtml'
        print(url)
        res=url_open(url)
        # print(res)
        soup=BeautifulSoup(res,"html.parser")
        # print('soup:')
        # print('地区：'+str(city))
        wea_str=wea_str+'为您查询到的地区:'+name+'\n'+'----------------'+'\n'
        a=soup.select('.sky.skyid')[0]
        # print(a)
        day=a.select('h1')[0].text
        # print(str(day))
        wea_str=wea_str+"今天:"+str(day[:-5])+"号\n"
        wea=a.select('.wea')[0].text
        # print(wea)
        wea_str=wea_str+"天气:"+str(wea)+"\n"
        tem=a.select('.tem')[0].text[1:-1]
        # print(tem)
        wea_str=wea_str+"温度:"+str(tem)+"\n"+'----------------'+'\n'
        # print(dic)
        b=soup.select('.sky.skyid')[1]
        # print('b',b)
        day2=b.select('h1')[0].text
        # print(str(day2))
        wea_str=wea_str+"明天:"+str(day2[:-5])+"号\n"
        wea2=b.select('.wea')[0].text
        wea_str=wea_str+"天气:"+str(wea2)+"\n"
        # print(wea2)
        tem=b.select('.tem')[0].text[1:-1]
        # print(tem)
        wea_str=wea_str+"温度:"+str(tem)+"\n"+'----------------'+'\n'

        wea_str=wea_str+'今日天气新闻\n'
        news=soup.select('.article-box')[0]
        news_title=news.select('h2')[0].text
        wea_str=wea_str+'--'+str(news_title[2:-2])+"--\n"
        news_con=news.select('p')[0].text
        wea_str=wea_str+news_con
        wea_str=quote(wea_str,'utf-8')
        return wea_str

# 查找单个键
def find(target, dictData, notFound=0):
    queue = [dictData]
    while len(queue) > 0:
        data = queue.pop()
        for key, value in data.items():
            if key == target:
                if str(type(value))=="<class 'dict'>":
                    if 'AREAID'in value:
                        return value
                    else:
                        queue.append(value)
            elif str(type(value))=="<class 'dict'>":
                queue.append(value)
    return notFound

def get_city(name):
    url = "https://j.i8tq.com/weather2020/search/city.js"
    res = url_open(url)
    dict = eval(res[18:])
    city_id = find(name, dict)
    # print(city_id)
    if(city_id!=0):
        return city_id['AREAID']
    else:
        return 0

def get_time_wea(name='嘉定'):
    tip=''
    # id=get_city(name)
    # url='http://www.weather.com.cn/weather1d/'+str(id)+'.shtml'
    # print(url)
    p = Pinyin()
    py=p.get_pinyin(name, '')
    url='https://www.tianqishi.com/'+py+'.html'
    res=url_open(url)
    # print(res)
    soup = BeautifulSoup(res, "html.parser")
    # print(soup)
    a=soup.select('.jdjianjie')[0]
    # print(a)
    today_wea=a.select('p')[0].text
    # print(today_wea)
    tip=tip+today_wea[19:]+'\n'+'-----------------------------'+'\n'
    tom_wea=a.select('p')[1].text.replace('              ','')
    # print(tom_wea)
    tip=tip+'\n'+tom_wea+'\n'+'---------------------------'+'\n'
    for i in range(4):
        b=soup.select('.yuBaoTable>tr')[i]
        c=b.select('td')
        hour=c[0].text
        hour=hour+' 温度:'+c[1].text
        hour=hour+' '+c[2].text
        hour=hour+ ' '+c[3].text+'级'
        hour=hour+' 湿度:'+c[6].text
        hour=hour+' 降雨概率:'+c[7].text
        # print(hour)
        tip=tip+'\n'+hour
    print(tip)
    # tip=tom_wea
    tip = quote(tip)
    # print(tip)
    return tip

if __name__=='__main__':
    get_time_wea()
    # res=get_wea()
    # print(res)