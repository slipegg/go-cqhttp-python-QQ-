import requests
from bs4 import BeautifulSoup
import json
import random
import time


def url_open(url):
# try:

    head =\
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
    }
    req = requests.get(url,headers=head).content.decode('gbk')

    return req
# except:
#     return '0'


def get_pic_url(chose):
    page_id=random.randint(1,50)
    if page_id==1:
        url = 'https://pic.netbian.com/' + chose + '/index' + '.html'
    else:
        url='https://pic.netbian.com/'+chose+'/index_'+str(page_id)+'.html'
    print(url)
    res=url_open(url)
    soup = BeautifulSoup(res, "html.parser")
    a_int=random.randint(0,20)
    a = soup.select('.clearfix>li')[a_int]
    b=a.find(name="a").get('href')
    p_url='https://pic.netbian.com'+b
    p_res=url_open(p_url)
    s=BeautifulSoup(p_res, "html.parser")
    pic=s.select('.photo-pic>a')[0].find(name='img').get('src')
    pic_url='https://pic.netbian.com/'+pic
    return pic_url