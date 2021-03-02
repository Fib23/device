import re
import pexpect
import time
import sys
import os
from get_vlans import get_vlans
from search_vlan import search_vlan
from port_desc import port_desc
def main(ip, user_auth, user_os, user_snmp, snmpv3_authpassphrase, snmpv3_privpassphrase, auth, privacy):
	vlans = get_vlans(ip,user_auth, user_os, user_snmp, snmpv3_authpassphrase, snmpv3_privpassphrase, auth, privacy)
	tvlan = search_vlan(vlans,vlan=[1000,3999])
	portdesc = port_desc(ip,user_auth, user_os,tvlan)
if __name__ == '__main__':
	main(ip=sys.argv[1], user_auth=sys.argv[2], user_os=sys.argv[3], user_snmp=sys.argv[4], snmpv3_authpassphrase=sys.argv[5], snmpv3_privpassphrase=sys.argv[6], auth=sys.argv[7], privacy=sys.argv[8]) 
