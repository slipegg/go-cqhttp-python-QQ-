import requests
from bs4 import BeautifulSoup
import json
import random
import time
import datetime
from urllib.parse import quote
import hashlib
import urllib

SUB='_2A25NoBTYDeRhGeBN6VMW8y3IwzmIHXVu1AEQrDV8PUNbmtANLXfFkW9NRIVCcm3DpvuOhbapttPw-FaAAHLZw9Vr'
def update_SUB(txt):
    global SUB
    SUB=txt
    print(SUB)
def get_gequ_id(str):
    res = url_open('https://www.9ku.com/geci/1128475.htm')
    # print('https://www.baidu.com/s?wd=' + str + '%20歌词')
    print(res)
def get_gechi(str):
    # while
    try:
        res = url_open('https://www.baidu.com/s?wd='+str+'%20歌词')
        print(res)
        soup = BeautifulSoup(res, "html.parser")
        a = soup.select('.re-box_3gPX1 ')[0].text
        a=a.replace('立即播放查看歌词','')
        print(a)
    except:
        a='似乎没找到这个或者被拒绝了，请慢点再试试><'
    a = quote(a)
    return a

def daidu_baike(txt):
    try:
        res=url_open('https://baike.baidu.com/item/'+txt)
        # print(res)
        soup = BeautifulSoup(res, "html.parser")
        a = soup.select('.lemma-summary')[0].text
        a=a+'\n详情见'+('https://baike.baidu.com/item/'+quote(txt))
        print(a)
    except:
        a='似乎没有这个词条><'
    a=quote(a)
    return a

def mengniang(txt):
    try:
        res = url_open('https://zh.moegirl.org.cn/' + txt)
        print(res)
        soup = BeautifulSoup(res, "html.parser")
        a = soup.select('.mw-parser-output')[1].text
        a=str(a)
        a=a.replace('\n\n','')
        a=a[1:2000]
        a = a + '...\n详情见' + ('https://zh.moegirl.org.cn/' + quote(txt))
        print(a)
    except:
        a='似乎没有这个词条><'
    a=quote(a)
    return a

def fanyi(word):
    # print(8888)
    # print(word)
    src = 'auto'                                                #翻译的源语言
    obj = 'zh'                                                #翻译的目标语言
    appid = '20210313000726084'                                     #这里输入你注册后得到的appid
    secretKey = 'Ycx1L5Sz_ep54METXv_x'                                  #这里输入你注册后得到的密匙

    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'                  #必须加上的头
    # word= input('请输入你要翻译的中文：')                                           #输入你要翻译的中文
    salt = random.randint(31256, 66253)                                           #产生随计数

    sign = appid + word + str(salt) + secretKey                                   #文档的step1拼接字符串
    m1 = hashlib.md5()
    m1.update(sign.encode('utf-8'))
    sign = m1.hexdigest()                                                         #文档的step2计算签名
    myur1 = myurl  + '?q=' + urllib.parse.quote(word) + '&from=' + src + '&to=' + obj + '&appid='+ appid + '&salt=' + str(salt) + '&sign=' + sign
    print (myur1)                                                                 #生成的url并打印出来
    english_data = requests.get(myur1)                                            #请求url
    js_data = json.loads(english_data.text)                                       #下载json数据
    content = js_data['trans_result'][0]['dst']                                   #提取json数据里面的dst
    tip=urllib.parse.quote(content)
    print (content)                                                               #打印出翻译的英文
    return tip

def xiaobing( msg):
    uid = ''  # !!!!!!!!!!!!这里要改的!!!!!!!!!!!!!!!!!!!!!
    source = ''  # !!!!!!!!!!!!这里要改的!!!!!!!!!!!!!!!!!!!!!
    global SUB 
    url_send = 'https://api.weibo.com/webim/2/direct_messages/new.json'
    data = {
        'text': msg,
        'uid': uid,
        'source': source
    }
    headers = {
        'cookie': 'SUB=' + SUB,
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Referer': 'https://api.weibo.com/chat/'
    }
    response = requests.post(url_send, data=data, headers=headers).json()
    sendMsg = response['text']
    time.sleep(1)

    for i in range(3):
        url_get = 'https://api.weibo.com/webim/2/direct_messages/conversation.json?uid={}&source={}'.format(uid,
                                                                                                            source)
        response = requests.get(url_get, headers=headers).json()
        getMsg = response['direct_messages'][0]['text']
        if sendMsg == getMsg:
            time.sleep(1)
        else:
            print(getMsg)
            getMsg=quote(getMsg)
            return getMsg
    getMsg='装傻(⊙_⊙)'
    return getMsg

def df_url_open(lou,fang):
    return "失败"

def xiaohua_url_open(url):
# try:
    head =\
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    req = requests.get(url,headers=head).content.decode('gbk')
    return req

def url_open(url):
# try:
    head =\
    {
        # 'Cookie': 'ASP.NET_SessionId=vo0alpvphh4lysvrj5rllpil',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    req = requests.get(url,headers=head).content.decode('utf-8')

    return req
# except:
#     return '0'

def get_dianfei(infor=' '):
        tip='找不到呜呜呜(⋟﹏⋞)'
        tip = quote(tip)
        return tip

def tips(tim='中午',tip='事件'):
    if(tim=='中午'):
        start_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '14:33:30', '%Y-%m-%d%H:%M:%S')
    # 方法一：
    # 判断当前时间是否在范围时间内
    flag=1
    while 1:
        if start_time < datetime.datetime.now() < start_time+datetime.timedelta(seconds=2):
            print(tip)
            break

def xiaohua():
    l_n=random.randint(0,7)
    lis=['lengxiaohua','youmo','aiqing','xiaoyuan','jianduan','jingdian','yijuhua','new']
    p_n=random.randint(0,8)
    url='https://xiaohua.zol.com.cn/'+lis[l_n]+'/'+str(p_n)+'.html'
    res=xiaohua_url_open(url)
    soup= BeautifulSoup(res, "html.parser")
    a_n=random.randint(0,19)
    a=soup.select('.summary-text')[a_n].text#20
    # print(a)
    a=quote(a)
    return a

def save_dianfei():
    lf = open('last_df.txt', 'r')
    last_df = eval(lf.read())
    lf.close()
    uf = open('used_df.txt', 'r')
    used_df = eval(uf.read())
    uf.close()

    lis=['7 408','7 423','7 409','7 242','9 408']
    for i in lis:
        used_df[i] = round(float(last_df[i]) - float(get_dianfei(i)), 2)
        last_df[i] = get_dianfei(i)
        print(used_df[i])

    lf = open('last_df.txt', 'w')
    lf.write(str(last_df))
    lf.close()
    uf = open('used_df.txt', 'w')
    uf.write(str(used_df))
    uf.close()

def judge_df(infor='7 408'):
    return "失败"
if __name__=='__main__':
    print(666)
    a=input(888)
    # get_gequ_id('处处傻')
    # get_gechi('处处傻')
    # mengniang('Warma')
    # daidu_baike('你好')
    # star_time=time.time()
    # while 1:
    #     if(time.time()-star_time>=5):
    #         save_dianfei()
    #         judge_df()
    #         star_time=time.time()
