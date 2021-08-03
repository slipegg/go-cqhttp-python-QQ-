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
    uid = '5175429989'  # !!!!!!!!!!!!这里要改的!!!!!!!!!!!!!!!!!!!!!
    source = '209678993'  # !!!!!!!!!!!!这里要改的!!!!!!!!!!!!!!!!!!!!!
    global SUB
    # SUB = '_2A25NmjMBDeRhGeBN6VMW8y3IwzmIHXVu7iPJrDV8PUNbmtANLWmlkW9NRIVCcljPkIwZ3jRbPWVFUGZRq_Xx5lGl'  # !!!!!!!!!!!!这里要改的!!!!!!!!!!!!!!!!!!!!!
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
# try:
    cooks=\
        [
            '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',
            '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',
            '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'
        ]
    if fang[:1]=='4' and lou=='9':
        cook=cooks[2]
    elif fang[:1]=='2':
        cook=cooks[0]
    elif fang[:1]=='4':
        cook=cooks[1]
    # print(fang[:1])
    payload = {
        #'__VIEWSTATE': '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',
        '__VIEWSTATE': cook,
        '__VIEWSTATEGENERATOR': 'CA0B0334',
        'drlouming': '9',
        'drceng': '0'+lou,
        'dr_ceng': '0'+lou+'0'+fang[:1],
        'drfangjian': '0'+lou+'0'+fang,
        'radio': 'buyR',
        'ImageButton1.x': '5',
        'ImageButton1.y': '2'
    }
    # print(payload)
    head =\
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    rs=requests.session()
    reqq = rs.post('http://202.120.163.129:88/Default.aspx',headers=head,data=payload,verify=False)
    # print(reqq)
    req=rs.get('http://202.120.163.129:88/buyRecord1.aspx',verify=False).content.decode('utf-8')

    return req

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

def get_dianfei(infor='7 408'):
    try:
        res=df_url_open(infor[:1],infor[2:5])
        print(res)
        soup= BeautifulSoup(res, "html.parser")
        a=soup.select('h6>span')[0].text
        # print(infor+':'+a)
        tip=a
        return tip
    except:
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
    uf = open('used_df.txt', 'r')
    used_df = eval(uf.read())
    uf.close()

    if(used_df[infor]>0.07):
        print(used_df)
        print('过去3分钟用电:'+str(used_df[infor])+'，婳婳酱猜测'+infor+'的热水器在开着哦')
        tip=quote('过去3分钟用电:'+str(used_df[infor])+'，婳婳酱猜测'+infor+'的热水器在开着哦')
        return tip
    else:
        print(used_df)
        print('过去3分钟用电:'+str(used_df[infor])+'，婳婳酱猜测'+infor+'的热水器没在运行哦')
        tip=quote('过去3分钟用电:'+str(used_df[infor])+'，婳婳酱猜测'+infor+'的热水器没在运行哦')
        return tip
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
