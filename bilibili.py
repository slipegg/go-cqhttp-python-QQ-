import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import json
import random
import time
def url_open(url):
# try:
    head =\
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
    }
    req = requests.get(url,headers=head).content.decode()
    return req

def get_last_video(uid,last_video):
    t = url_open('https://api.bilibili.com/x/space/arc/search?mid='+str(uid)+'&pn=1&ps=25&index=1&jsonp=jsonp')
    f = json.loads(t)
    temp = f['data']['list']['vlist'][0]
    # print(last_video ,temp['bvid'])
    if last_video == None:
        last_video = temp['bvid']
        return [None,last_video]
    elif last_video == temp['bvid']:
        last_video=temp['bvid']
        print('有更新')
        tip=str(temp['author'])+'更新了！标题：'+str(temp['title'])+'\n点击链接前往观看~\nhttps://www.bilibili.com/video/'+str(last_video)
        return [quote(tip,'utf-8'),last_video]
    else:
        return [None,last_video]

if __name__=="__main__":
    s_time = time.time()
    print(s_time)
    if (time.time() - s_time >= 180):
        print(88)
        star_time = time.time()
    # last_video=None
    # while(1):
    #     # t=url_open('https://weibo.com/warmawarma?is_all=1')
    #     # print(t)
    #     # f=json.loads(t)
    #     # print(f["data"])
    #     # 普通说说
    #     # print(f["data"]['cards'][4])
    #     # print(f["data"]['cards'][4]['card'])
    #     # s=json.loads(f["data"]['cards'][4]['card'])
    #     # print(s['item']['content'])
    #     # 视频
    #     # print(f["data"]['cards'][3])
    #     # print(f["data"]['cards'][3]['card'])
    #     # print(f["data"]['cards'][1]['card'])
    #     # exit()
    #     t=url_open('https://api.bilibili.com/x/space/arc/search?mid=375089647&pn=1&ps=25&index=1&jsonp=jsonp')
    #     # t=url_open('https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?visitor_uid=34428314&host_uid=672328094&offset_dynamic_id=0&need_top=1&platform=web')
    #     print(t)
    #     f=json.loads(t)
    #     temp=f['data']['list']['vlist'][0]
    #     print(temp)
    #     print(temp['author'])
    #     if last_video==None:
    #         last_video=temp['bvid']
    #     elif last_video!=temp['bvid']:
    #         print('有更新')
    #     # print(last_video['bvid'])
    #     time.sleep(5)
