#!/usr/bin/env python
# coding=utf-8
import socket
import json
import os
import random
import requests
import time
import multiprocessing
from weather import get_time_wea,get_wea
from urllib.parse import quote
from random_pic import get_pic_url
from fun import get_dianfei,xiaohua,save_dianfei,judge_df,xiaobing,fanyi,update_SUB,daidu_baike,mengniang,get_gechi
from bilibili import get_last_video

group_person_fang={934643345:'7 242',2629201744:'7 409',1378097917:'7 423',2778579446:'7 408'}

# ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ListenSocket.bind(('127.0.0.1', 5710))
# ListenSocket.listen(100)


HttpResponseHeader = '''HTTP/1.1 200 OK
Content-Type: text/html
'''
all_message=None

#定位有效信息
def request_to_json(msg):
	for i in range(len(msg)):
		if msg[i]=="{" and msg[-1]=="}":
			return json.loads(msg[i:])
	return None

#需要循环执行，返回值为json格式
def rev_msg():# json or None
	ListenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#初始化socket（）
	ListenSocket.bind(('127.0.0.1', 5710))#使用bind()绑定ip和端口号
	ListenSocket.listen(100)#用listen()监听消息
	conn, Address = ListenSocket.accept()#获取客户端的套接字地址accept()
	print('接受到消息')
	Request = conn.recv(1024).decode('utf-8','ignore')#使用recv()接收数据，send()发送数据与客户端进行交互
	# print(Request)
	rev_json=request_to_json(Request)
	print(rev_json)
	conn.sendall((HttpResponseHeader).encode(encoding='utf-8'))
	conn.close()
	return rev_json

#获取信息类型 群聊/私聊 group/private
def get_message_type():
	return all_message['message_type']

#获取群号/私聊qq号
def get_number():
	if get_message_type() == 'group':
		return all_message['group_id']
	elif get_message_type() == 'private':
		return all_message['user_id']
	else:
		print('出错啦！找不到群号/QQ号')
		exit()
# 获取信息发送者的QQ号
def get_user_id():
	return all_message['user_id']

#获取发送的信息
def get_raw_message():
	return all_message['raw_message']

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#从客户端发送给服务端
def client_to_conn():
	label = get_message_type()
	number = get_number()
	msg = get_raw_message()
	print(flag)
	if flag == 0:
		exit()
	if label == 'group':
		payload = "GET /send_group_msg?group_id=" + str(number) + "&message=" + msg + " HTTP/1.1\r\nHost: 127.0.0.1:5700\r\nConnection: close\r\n\r\n"
	elif label == 'private':
		payload = "GET /send_private_msg?user_id=" + str(number) + "&message=" + " HTTP/1.1\r\nHost: 127.0.0.1:5700\r\nConnection: close\r\n\r\n"
	# print(payload)
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#初始化socket（）
	client.connect(('127.0.0.1',5700))#使用bind()绑定ip和端口号
	client.send(payload.encode("utf-8"))#发送消息
	client.close()#关闭连接

def send_private(msg,qq_number=2778579446):
	payload = "GET /send_private_msg?user_id=" + str(qq_number) + "&message=" +msg+ " HTTP/1.1\r\nHost: 127.0.0.1:5700\r\nConnection: close\r\n\r\n"#执行语句
	print(payload)
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#初始化socket（）
	client.connect(('127.0.0.1',5700))#使用bind()绑定ip和端口号
	client.send(payload.encode("utf-8"))#发送消息
	client.close()#关闭连接

#查找txt文本数据库
# def txt_msg(msg):
# 	fp = open("/机器人/txt.txt", "r",encoding='utf-8')
# 	while 1:
# 		s = fp.readline()
# 		if not s:
# 			fp.close()
# 			if flag == 2:
# 				return
# 			return error()
# 		s = s.strip('\n')
# 		s1 = s.split(' ')[0]
# 		s2 = s.split(' ')[1]
# 		if '[CQ:at,qq=×××××] ' + s1 == msg:
# 			fp.close()
# 			return s2

def help_interface():
	number = get_number()
	tip='婳婳酱来啦！(｡>∀<｡)\n来聊天吧！\n目前学会的指令：\n1.@婳婳酱 好看的\n2.@婳婳酱 动漫\n3.@婳婳酱 天气\n4.@婳婳酱 笑话\n5.@婳婳酱 电费\n6.@婳婳酱 翻译\n7.@婳婳酱 百度\n6.@婳婳酱 萌娘\n6.@婳婳酱 歌词'
	tip=quote(tip)
	payload = "GET /send_group_msg?group_id=" + str(number) + "&message="+tip + " HTTP/1.1\r\nHost: 127.0.0.1:5700\r\nConnection: close\r\n\r\n"
	print(payload)
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(('127.0.0.1',5700))
	client.send(payload.encode("utf-8"))
	client.close()

# def send_cat_pic():
# 	global flag
# 	flag = 1
# 	cat_list = os.listdir("/data/catpic")
# 	all_message['raw_message'] = "[CQ:image,file=file:///data/catpic/"+ random.choice(cat_list)+"]"
# 	client_to_conn()

def get_raw_message():
	return all_message['raw_message']
#错误
def error():
	# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# client.connect(('127.0.0.1',5700))
	global flag
	flag = 1
	rand = random.randint(1,4)
	number = get_number()
	if rand == 1:
		msg = "我听不懂你在说什么哦[CQ:face,id=106]"
	elif rand == 2:
		msg = "我好笨，听不懂呜呜呜[CQ:face,id=106]"
	elif rand == 3:
		msg = "啊？发生了什么[CQ:face,id=179]"
	elif rand == 4:
		msg = "干啥呢干啥呢"
	all_message['raw_message'] =msg
	client_to_conn()
	# msg=quote(msg)
	# payload = "GET /send_group_msg?group_id=" + str(number) + "&message=" + msg + " HTTP/1.1\r\nHost: 127.0.0.1:5700\r\nConnection: close\r\n\r\n"
	# print(payload)
	# client.send(payload.encode("utf-8"))
	# client.close()

#发送猫猫图
# ，图片保存在本地
def send_cat_pic():
    global flag
    flag = 1
    alist = os.listdir("D:/python代码学习/练习/动漫高清壁纸")
    str=random.choice(alist)
    print(str)
    all_message['raw_message'] = "[CQ:image,file=file:///D:/python代码学习/练习/动漫高清壁纸/"+ str+"]"

    client_to_conn()


#发送setu，图片从API内获取
def send_setu_pic():
	apikey = '×××××××××××××××'
	req_url="https://api.lolicon.app/setu/"
	params = {"apikey":apikey}
	res=requests.get(req_url,params=params)
	setu_url=res.json()['data'][0]['url']
	all_message['raw_message'] ="[CQ:image,file="+setu_url+"]"
	client_to_conn()

def send_wea(name='嘉定'):
	global flag
	flag = 1
	wea_str=get_time_wea(name)
	# wea_str=get_wea(name)
	all_message['raw_message'] =wea_str
	client_to_conn()

def send_pic(chose=1):
	global flag
	flag = 1
	if(chose==1):
		url=get_pic_url('4kdongman')
	elif chose==0:
		url=get_pic_url('4kmeinv')
	meth=random.randint(0,20)
	if(meth<=3):
		id_ran=random.randint(0,5)
		id_ran=40000+id_ran
		all_message['raw_message'] = '[CQ:image,file=' + url + ',type=show,id=' +str(id_ran)+']'
	else:
		all_message['raw_message'] ='[CQ:image,file='+url+']'#+str(id_ran)+']'
	client_to_conn()

def send_dianfei(infor='7 408'):
	print(type(all_message['sender']['user_id']))
	if all_message['sender']['user_id'] in group_person_fang and infor=='7 408':
		infor=group_person_fang[all_message['sender']['user_id']]
	global flag
	flag = 1
	print(infor)
	tip=get_dianfei(infor)
	print('tip1:'+tip)
	tip=infor+':'+tip+'度'
	print('tip1:' + tip)
	tip = quote(tip)
	all_message['raw_message'] =tip
	client_to_conn()

def send_xiaohua():
	global flag
	flag = 1
	s=xiaohua()
	print(s)
	all_message['raw_message'] = s
	client_to_conn()

# def send_zimu(name,url):
# 	global flag
# 	flag = 1
# 	try:
# 		s=get_zimu(name,url)
# 		print('s',s)
# 		for pa in s:
# 			all_message['raw_message'] = "[CQ:image,file=file:///"+pa+"]"
# 			print(all_message)
# 			client_to_conn()
# 	except:
# 		all_message['raw_message']='制作失败'
# 		client_to_conn()

def setu():
	global flag
	flag = 1
	all_message['raw_message'] = '[CQ:tts,text=你是笨蛋吗！不想和你说话了！傻瓜！傻瓜！！]'
	client_to_conn()

def send_used_df(infor='7 408'):
	global flag
	flag = 1
	if all_message['sender']['user_id'] in group_person_fang and infor=='7 408':
		infor=group_person_fang[all_message['sender']['user_id']]
	tip=judge_df(infor)
	all_message['raw_message'] = tip
	client_to_conn()

def send_xiaobing(f=0):
	global flag
	flag = 1
	mes=get_raw_message()
	userid=str(all_message['sender']['user_id'])
	if userid!='1348293252':
		if f==0:
			msg=mes[22:]
		else:
			msg=mes
	print(msg)
	tip='[CQ:at,qq='+userid+']'+xiaobing(msg)
	# tip=quote(tip)
	all_message['raw_message'] =tip
	client_to_conn()

def send_fanyi(str):
	global flag
	flag = 1
	print(str)
	tip=fanyi(str)
	print(str,tip)
	all_message['raw_message'] = tip
	client_to_conn()

def send_baidu(str):
	global flag
	flag = 1
	print(str)
	tip=daidu_baike(str)
	all_message['raw_message'] = tip
	client_to_conn()

def send_mengniang(str):
	global flag
	flag = 1
	print(str)
	tip=mengniang(str)
	all_message['raw_message'] = tip
	client_to_conn()

def send_gechi(str):
	print(str)
	global flag
	flag = 1
	print(str)
	tip=get_gechi(str)
	all_message['raw_message'] = tip
	client_to_conn()

#首次判断信息内容
def first_judgement():
	# if get_message_type() == 'private':
	# 	training_message()
	mes=get_raw_message()
	if mes == '[CQ:at,qq=1348293252] help' or mes == '[CQ:at,qq=1348293252] 在' or mes=='[CQ:at,qq=1348293252] ':
		help_interface()
		return
	elif mes == '[CQ:at,qq=1348293252] 美女' or mes=='[CQ:at,qq=1348293252] 好看的'or mes == '[CQ:at,qq=1348293252] [CQ:face,id=178]':
		send_pic(0)
		return
	elif mes == '[CQ:at,qq=1348293252] 色图' or mes=='[CQ:at,qq=1348293252] 涩图':
		setu()
		return
	elif mes == '[CQ:at,qq=1348293252] 动漫' or mes == '[CQ:at,qq=1348293252] [CQ:face,id=270]':
		send_pic(1)
		return
	elif mes[:24] == '[CQ:at,qq=1348293252] 天气':
		print(999)
		if(len(mes)<=24):
			send_wea()
		else:
			send_wea(mes[25:27])
		return
	# elif mes[:24]== '[CQ:at,qq=1348293252] 字幕':
	# 	s=mes.split()
	# 	name=s[2]
	# 	url=s[3]
	# 	send_zimu(name,url)
	# 	return
	elif mes == '[CQ:at,qq=1348293252] 笑话':
		print('笑话')
		send_xiaohua()
		return
	elif mes[:24] == '[CQ:at,qq=1348293252] 用电':
		if(len(mes)==24):
			send_used_df()
		else:
			send_used_df(mes[25:])
		return
	elif mes[:24] == '[CQ:at,qq=1348293252] 更新':
		update_SUB(mes[25:])
		return
	elif mes[:24] == '[CQ:at,qq=1348293252] 百度':
		send_baidu(mes[25:])
		return
	elif mes[:24] == '[CQ:at,qq=1348293252] 萌娘':
		send_mengniang(mes[25:])
		return
	elif mes[:24] == '[CQ:at,qq=1348293252] 歌词':
		send_gechi(mes[25:])
		return
	elif mes[:24] == '[CQ:at,qq=1348293252] 电费':
		if(len(mes)==24):
			send_dianfei()
		else:
			send_dianfei(mes[25:])
		return
	elif mes[:24] == '[CQ:at,qq=1348293252] 翻译'and len(mes)>24:
		print(666)
		send_fanyi(mes[25:])
		return
	elif mes[:21]=='[CQ:at,qq=1348293252]' :
		send_xiaobing()
		return
	elif random.random()<0.07:
	# else:
		print(99)
		print(all_message)
		send_xiaobing(1)
		return
	client_to_conn()

# if __name__ == '__main__':
def jiaohu():
	# ListenSocket.bind(('127.0.0.1', 5710))
	# ListenSocket.listen(100)
	while 1:
		try:
			global flag
			flag=0		#不知道有什么用，但是不能删，删了会重复发送消息
			global all_message
			all_message= rev_msg()
			first_judgement()
			# time.sleep(5)
		except:
			continue
def jianting(uid,qq_num=2778579446):
	star_time = time.time()
	last_video=None
	b=5
	while(1):
		try:
			hour = int(time.strftime("%H"))
			if (hour >= 1 and hour <= 6):
				print('进入睡眠模式')
				time.sleep(5*60*60+90)
				print('进入监听模式')
			else:
				# print(time.time(), star_time)
				if (time.time() - star_time >= b):
					duo_tip,last_video = get_last_video(uid, last_video)
					# print('判断：', duo_tip)
					if duo_tip != None:
						send_private(duo_tip,qq_num)
					star_time = time.time()
					b=random.randint(5,30)
		except:
			time.sleep(300)
if __name__=='__main__':
	hour=int(time.strftime("%H"))
	if(hour>=1 and hour<=6):
	print(hour)
	# jiaohu()
	# duo_uid=375089647
	# warma_uid=53456
	# boshidun_uid=346563107
	# shenyi_uid=648113003
	# p0 = multiprocessing.Process(target=jianting, args=(boshidun_uid,))
	# p1 = multiprocessing.Process(target=jianting, args=(warma_uid,))
	# p2 = multiprocessing.Process(target=jianting, args=(duo_uid,))
	# p3 = multiprocessing.Process(target=jiaohu)
	# p0.start()
	# p1.start()
	# p2.start()
	# p3.start()
	# jianting(duo_uid)
	# send_private('2333')