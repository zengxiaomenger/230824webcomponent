#!/usr/bin/env python3
import requests
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
domain_text=''
in_type=1 #1 2
def give_value(tp):
	global domain_text
	domain_text=tp
	detect()
def detect():
	global domain_text
	if in_type==1:
		domainlist = domain_text.split(";")
	else:
		if '\r\n' in domain_text: #windows
			domainlist = domain_text.split("\r\n")
		else:
			if '\n' in domain_text: #linux
				domainlist = domain_text.split("\n")
			else: #mac/unix
				domainlist = domain_text.split("\r")
	with use_scope('res',clear=True):
		put_text('')
	for domain in domainlist:
		if domain=='':
			continue
		with use_scope('res'):
			put_text(domain,'的查询结果是:')
		dic = eval(requests.get("http://localhost:8000",params={"domain": domain}).text)
		#排序
		lis = sorted(dic.items(),key=lambda d:d[1],reverse=False)
		#分类输出
		i=0
		temp='nothing'
		for item in lis:
			i=i+1
			if item[1]=='nothing' or item[1]!=temp :
				with use_scope('res'):			
					put_text('              ',item[1],':')
					put_text('                            ',item[0])
			else:
				with use_scope('res'):
					put_text('                            ',item[0])
			temp=item[1]
def fun():
	put_image(open('test.jpg','rb').read())
	put_radio('choose',label='选择输入方式',options=['手动输入','上传文件'],inline=True,value=['手动输入'])
	#init 手动输入
	with use_scope('init',clear=True):
		put_input('input',label='输入你想查询的网址（若有多个网址，用英文";"分开）',placeholder='如：baidu.com，无需添加协议')
		put_buttons(['点击查询'],lambda _: give_value(pin.input) )
	while(True):
		changed=pin_wait_change('choose')
		with use_scope('res',clear=True):
			put_text('')
		global in_type
		if pin.choose=='手动输入':
			in_type=1
			with use_scope('init',clear=True):
				put_input('input',label='输入你想查询的网址（若有多个网址，用英文";"分开）',placeholder='如：baidu.com，无需添加协议')
				put_buttons(['点击查询'],lambda _: give_value(pin.input) )
		else:
			in_type=2
			with use_scope('init',clear=True):
				file=file_upload(label='选择文件 (文件格式为.txt，每行一个域名)')
			global domain_text
			domain_text=str(file['content'],encoding='utf-8')
			detect()

if __name__ == '__main__':
	#fun()
	start_server(fun, port=8003)
