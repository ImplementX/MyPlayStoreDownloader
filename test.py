#!/usr/bin/python
import download2
import time
class NameSpace(object):

	def __init__(self):
		self.credentials = None
		self.out = None	
		self.package = None

def fun():
	with open("packages.txt") as f:
		s = f.read()
		s = s.split(',')
		for i in s:
			arg = NameSpace()
			arg.credentials = "credentials.json"
			arg.out = "/data/tools/nginx/html/apk"
			arg.package = i
			print("starting download application ",arg.package)
			print("===================================================================")
			download2.main(arg)
			print("\n\n")
if __name__ == '__main__':
	fun()
