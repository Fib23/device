import re
def search_vlan(vlans,vlan=[1000,3999]):
	number = vlans[0]
	number_to_number = vlans[1]
	tvlan1000 = []
	tvlan3999 = []
	if number:
		for i in number:
			i_ = re.findall(r"n \d+ \d",i)[0][1:-1].strip() #['n 1204 0']  ' 1024 ' '1024'
			#print(i) # '1024'
			for vlan_ in vlan:
				if vlan_ == int(i_):
					if vlan_ == 1000:
						print("Одиночный vlan:",vlan_)																	#Одиночный vlan: 1000
						print("Номер vlan:",vlan_, "Номер port:",re.findall(r"\d+\/\d+ \d+",i)[0].replace(" ","/"))		#Номер vlan: 1000 Номер port: 0/7/2
						tvlan1000.append(re.findall(r"\d+\/\d+ \d+",i)[0].replace(" ","/"))
						#print(tvlan1000)
					if vlan_ == 3999:
						print("Одиночный vlan:",vlan_)																	
						print("Номер vlan:",vlan_,"Номер port:",re.findall(r"\d+\/\d+ \d+",i)[0].replace(" ","/"))		
						tvlan3999.append(re.findall(r"\d+\/\d+ \d+",i)[0].replace(" ","/"))
						#print(tvlan3999)
	if number_to_number:
		for i in number_to_number:
			#print(i)
			i_ = re.findall(r"n \d+ to \d+ \d", i)[0][1:-1].strip().split(' to ') #['n 1204 to 1205 0']	[1024,1205]
			for vlan_ in vlan:
				if vlan_ in range(int(i_[0]), int(i_[1])+1):
					if vlan_ == 1000:
						print("Не одиночный vlan:",vlan_)																
						print("Номер vlan:", vlan_,"Номер port:",re.findall(r"\d+\/\d+ \d+",i)[0].replace(" ","/"))		
						tvlan1000.append(re.findall(r"\d+\/\d+ \d+",i)[0].replace(" ","/"))
						#print(tvlan1000)
					if vlan_ == 3999:
						print("Не одиночный vlan:",vlan_)																#Не одиночный vlan: 3999
						print("Номер vlan:",vlan_,"Номер port:",re.findall(r"\d+\/\d+ \d+",i)[0].replace(" ","/"))		#Номер vlan: 3999 Номер port: 0/7/2
						tvlan3999.append(re.findall(r"\d+\/\d+ \d+",i)[0].replace(" ","/"))
						#print(tvlan3999)
	print("View vlan 1000","brief ports",tvlan1000)
	print("View vlan 3999","brief ports",tvlan3999)

	return tvlan1000,tvlan3999