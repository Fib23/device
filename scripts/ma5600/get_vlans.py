import re
import pexpect
import time
import sys
import os
def get_vlans(ip,user_auth, user_os, user_snmp, snmpv3_authpassphrase, snmpv3_privpassphrase, auth, privacy):
	# Examples re for vlan
	#re.findall(r"\d+ to \d+ \d+\/\d+ \d+", 'port vlan 1204 to 1205 0/17 0') ['1204 to 1205 0/17 0']
	#re.findall(r"\d+ \d+\/\d+ \d+", 'port vlan 1204 0/17 0') 				  ['1204 0/17 0']

	print("IP address устройства:", ip)

	vlan=[1000,3999]
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
			ssh.sendline("display current-configuration section vlan-config | include 0/")
			"""
			Пример вывод команды display current-configuration section vlan-config | include 0/
				port vlan 1000 0/7 2
				port vlan 1514 0/7 2
				port vlan 3999 to 4006 0/7 2
				port vlan 4035 0/7 2
				port vlan 4039 0/7 2
				port vlan 4043 0/7 2
 				port vlan 4035 0/7 3
			"""
			ssh.expect('#')
			ssh.expect('#')
			#print(str(ssh.before.decode('utf-8')))
			number_to_number = re.findall(r"vlan \d+ to \d+ \d+\/\d+ \d+",str(ssh.before.decode('utf-8')))
			"""
				Парсинг вывода vlan на uplink портах по кретерию  "vlan {vlaid} to {vlaid} 0/{boardid} {portid}"
			"""
			number = re.findall(r"vlan \d+ \d+\/\d+ \d+",str(ssh.before.decode('utf-8'))) #['vlan 1204 0/17 0']
			"""
				Парсинг вывода vlan на uplink портах по кретерию  "vlan {vlaid} 0/{boardid} {portid}"
			"""
			print("Одиночные vlanы:",number)
			"""
				Пример вывода переменной number: Одиночные vlanы: ['vlan 1000 0/7 2', 'vlan 1514 0/7 2', 'vlan 4035 0/7 2', 'vlan 4039 0/7 2', 'vlan 4043 0/7 2', 'vlan 4035 0/7 3']
			"""
			print("Не одиночные vlanы:",number_to_number)
			"""
				Пример вывода переменной number_to_number: Не одиночные vlanы: ['vlan 3999 to 4006 0/7 2']
			"""
			print(str(ssh.before.decode('utf-8')))
			ssh.sendline('quit')
			ssh.expect('#')
			ssh.sendline('quit')
			ssh.expect(']:')
			ssh.sendline('y')
			ssh.close(force=True) 
			return number, number_to_number
	except:
		print("error1")
			
