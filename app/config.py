#!usr/bin/python2.7
# coding=utf-8

#######################################################
# Name           : Multi BF (MBF) <cookie method>     #
# File           : config.py                          #
# Author         : DulLah                             #
# Github         : https://github.com/dz-id           #
# Facebook       : https://www.facebook.com/dulahz    #
# Telegram       : https://t.me/unikers               #
# Python version : 2.7                                #
#######################################################

import requests

class Config:
	def loadCookie(self):
		try:
			file = open('log/cookies.log','r')
			cookie = file.read()
			file.close()
			return cookie.strip()
		except IOError:
			return False

	def banner(self):
		return '''\n
\033[0;96m┏━┓┏━┓╋╋╋╋╋╋╋╋┏┓╋╋┏━┓
\033[0;96m┃┃┗┛┃┃╋╋╋╋╋╋╋╋┃┃╋╋┃┏┛
\033[0;96m┃┏┓┏┓┣━━┳━┓╋╋╋┃┗━┳┛┗┓
\033[0;96m┃┃┃┃┃┃┏┓┃┏┓┳━━┫┏┓┣┓┏┛
\033[0;96m┃┃┃┃┃┃┏┓┃┃┃┣━━┫┗┛┃┃┃
\033[0;96m┗┛┗┛┗┻┛┗┻┛┗┛╋╋┗━━┛┗┛ \033[0;91mv2.0 \033[0mRecode: HilmanXD \033[0m|| FB.me/xxx.hilmanxd'''

	def httpRequest(self, url, cookies):
		try:
			return requests.get(url, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mConnection error, check your connection!!\033[0m')

	def httpRequestPost(self, url, cookies, params):
		try:
			return requests.post(url, data = params, cookies = {'cookie': cookies}).text
		except requests.exceptions.RequestException:
			exit('\n\n\033[0;91mConnection error, check your connection!!\033[0m')
