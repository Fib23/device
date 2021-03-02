import re
import pexpect
import time
import sys
import os
def port_desc(ip,user_auth, user_os,tvlan):
	tvlan1000 = tvlan[0]
	tvlan3999 = tvlan[1]
	try: #desc dslam
		with pexpect.spawn("ssh -oKexAlgorithms=+diffie-hellman-group1-sha1  -c 3des-cbc {1}@{0} -i /home/{2}/.ssh/{1}.rsa -o StrictHostKeyChecking=no".format(ip,user_auth,user_os)) as ssh:
			ssh.expect('-')
			#print(str(ssh.before.decode('utf-8')))
			ssh.sendline('\r')
			ssh.expect('>')
			#print(str(ssh.before.decode('utf-8')))
			ssh.sendline('enable')
			ssh.expect('#')
			#print(str(ssh.before.decode('utf-8'))) 
			ssh.sendline('config')
			ssh.expect('#')
			#print(str(ssh.before.decode('utf-8'))) 
			ssh.sendline('scroll')
			ssh.expect('}:')
			ssh.sendline('\r')
			ssh.expect('#')
			#print(str(ssh.before.decode('utf-8')), " 1")
			ssh.sendline('undo  port  desc 0/7')
			ssh.expect('}:')
			ssh.sendline('\r')
			ssh.expect('#')

			for i in tvlan1000:
				if i in tvlan3999:
					print("Uplink-All-{0}".format(i))
					ssh.sendline('port desc {0} description Uplink-All-{0}'.format(i))
					ssh.expect('#')
					if len(tvlan3999) == 1:
						tvlan3999 = [] 
					elif len(tvlan3999) > 1:
						tvlan3999.remove(i)
				elif i not in tvlan3999:
					print("Uplink-Iptv-{0}".format(i))
					ssh.sendline('port desc {0} description Uplink-Iptv-{0}'.format(i))
					ssh.expect('#')
					#print("Uplink-Other-%s"%i)
					#ssh.sendline('port desc {0} description Uplink-Other-{0}'.format(i))
					#ssh.expect('#')
				if tvlan3999:
					for i in  tvlan3999:
						print("Uplink-Other-{0}".format(i))	
						ssh.sendline('port desc {0} description Uplink-Other-{0}'.format(i))
						ssh.expect('#')
			print(str(ssh.before.decode('utf-8')))
			ssh.sendline('quit')
			ssh.expect('#')
			ssh.sendline('quit')
			ssh.expect(']:')
			ssh.sendline('y')
			ssh.close(force=True)
	except:
		print("{ip}: error description ")