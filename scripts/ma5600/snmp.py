import re
import pexpect
import time
import sys
import os
#ma5600
def snmp_v2_ssh_gr(ip,community_2,snmp_v2_user,CONNECT):
	print("IP address устройства:", ip)
	print(CONNECT)
	try:
		#with pexpect.spawn("ssh -oKexAlgorithms=+diffie-hellman-group1-sha1  -c 3des-cbc andsh88@{0} -i /home/andrei/.ssh/andsh88.rsa -o StrictHostKeyChecking=no".format(ip)) as ssh:
		with pexpect.spawn('{0}'.format(CONNECT).format(ip)) as ssh:
			ssh.expect('-')
			ssh.sendline('\r')
			ssh.expect('>')
			ssh.sendline('enable')
			ssh.expect('#') 
			ssh.sendline('config')
			ssh.expect('#')
			print(str(ssh.before.decode('utf-8')))
			ssh.sendline('snmp-agent community read {0} mib-view {1}View'.format(community_2,snmp_v2_user.capitalize()))
			ssh.expect('#')
			ssh.sendline('snmp-agent mib-view {0}View include org'.format(snmp_v2_user.capitalize()))
			ssh.expect('#')
			ssh.sendline('quit')
			ssh.expect('#')
			ssh.sendline('quit')
			ssh.expect(']:')
			ssh.sendline('y')
			ssh.close(force=True)
	except:
		print('Error great snmp v2c')


def snmp_v3_ssh_gr(ip,snmp_v3_user,snmp_v3_auth,snmp_v3_auth_key,snmp_v3_priv,snmp_v3_priv_key,CONNECT):
	print("IP address устройства:", ip)
	try:
		with pexpect.spawn('{0}'.format(CONNECT).format(ip)) as ssh:
			ssh.expect('-')
			ssh.sendline('\r')
			ssh.expect('>')
			ssh.sendline('enable')
			ssh.expect('#') 
			ssh.sendline('config')
			ssh.expect('#') 
			ssh.sendline('snmp-agent group v3 {0}Group privacy read-view {0}View'.format(snmp_v3_user.capitalize()))
			ssh.expect('}:')
			ssh.sendline('\r')
			ssh.expect('#')
			ssh.sendline('snmp-agent mib-view {0}View include org'.format(snmp_v3_user.capitalize()))
			ssh.expect('#')
			ssh.sendline('snmp-agent usm-user v3 {0} {1}Group authentication-mode {2}'.fromat(snmp_v3_user.lower(),snmp_v3_user.capitalize(),snmp_v3_auth))
			ssh.expect('}:')
			ssh.sendline(snmp_v3_auth_key)
			ssh.expect('}:')
			ssh.sendline('privacy-mode')
			ssh.expect('}:')
			ssh.sendline(snmp_v3_priv)
			ssh.expect('}:')
			ssh.sendline(snmp_v3_priv_key)
			ssh.expect('#')
			ssh.sendline('quit')
			ssh.expect('#')
			ssh.sendline('quit')
			ssh.expect(']:')
			ssh.sendline('y')
			ssh.close(force=True)
	except:
		print('Error')
def snmp_v2_ssh_del(ip,community_2,snmp_v2_user,CONNECT):
	print("IP address устройства:", ip)
	print(CONNECT)
	try:
		with pexpect.spawn('{0}'.format(CONNECT).format(ip)) as ssh:
			ssh.expect('-')
			ssh.sendline('\r')
			ssh.expect('>')
			ssh.sendline('enable')
			ssh.expect('#') 
			ssh.sendline('config')
			ssh.expect('#') 
			ssh.sendline('undo snmp-agent community {0}'.format(community_2))
			ssh.expect('#')
			ssh.sendline('undo snmp-agent mib-view'.format(snmp_v2_user.capitalize()))
			ssh.expect('#')
			ssh.sendline('quit')
			ssh.expect('#')
			ssh.sendline('quit')
			ssh.expect(']:')
			ssh.sendline('y')
			ssh.close(force=True)
	except:
		print('No supporting delet snmp v2c')

def snmp_v3_ssh_del(ip,snmp_v3_user,snmp_v3_auth,snmp_v3_auth_key,snmp_v3_priv,snmp_v3_priv_key,CONNECT):
	print("IP address устройства:", ip)
	try:
		with pexpect.spawn('{0}'.format(CONNECT).format(ip)) as ssh:
			ssh.expect('-')
			ssh.sendline('\r')
			ssh.expect('>')
			ssh.sendline('enable')
			ssh.expect('#') 
			ssh.sendline('config')
			ssh.expect('#') 
			ssh.sendline('undo snmp-agent group v3 {0}Group privacy'.format(snmp_v3_user.capitalize()))
			ssh.expect('#')
			ssh.sendline('undo snmp-agent mib-view {0}View'.format(snmp_v3_user.capitalize()))
			ssh.expect('#')
			ssh.sendline('undo snmp-agent usm-user v3 {0}'.fromat(snmp_v3_user.lower()))
			ssh.expect('#')
			ssh.sendline('quit')
			ssh.expect('#')
			ssh.sendline('quit')
			ssh.expect(']:')
			ssh.sendline('y')
			ssh.close(force=True)
	except:
		print('No supporting delet snmp v2c')

if __name__ == '__main__':
	snmp_v2_ssh_gr(ip = sys.argv[1], community_2 = sys.argv[2], snmp_v2_user = sys.argv[3], CONNECT = sys.argv[4])
	#snmp_v3_ssh_gr()
	#snmp_v2_ssh_del()
	#snmp_v3_ssh_del()