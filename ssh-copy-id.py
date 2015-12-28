#!/usr/bin/env python
# coding: utf8

import os,sys,pexpect

class SshCopy:
	
	def __init__(self, user, host, passwd, port):
		self.pub_key = os.getenv('HOME') + '/.ssh/id_rsa.pub'
		self.user = user
		self.host = host
		self.passwd = passwd
		self.port = port
	
        def displayArgs(self):
               print "key : ", self.pub_key, ", user :", self.user, ", host :", self.host, ", passwd :", self.passwd, ", port :", self.port
               
	def send(self):
		str_ssh = '/usr/bin/ssh-copy-id -i %s %s@%s -p %s' %(self.pub_key,self.user,self.host, self.port)
		child = pexpect.spawn( str_ssh )
		try:
			index = child.expect(['continue connecting \(yes/no\)','\'s password:',pexpect.EOF],timeout=20)
			print index
			if index == 0:
				child.sendline('yes')
				print child.after,child.before
			if index == 1:
				child.sendline(self.passwd)
				child.expect('password:')
				child.sendline(self.passwd)
				print child.after,child.before
			if index == 2:
				print '[ failed ]'
				print child.after,child.before
				child.close()
		except pexpect.TIMEOUT:
			print child.after,child.before
			child.close()
		else:
			print 'nada feito'
			
result=SshCopy('test','1.1.1.1','test','22')
result.displayArgs()
result.send()
