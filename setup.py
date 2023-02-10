import random
import time
def write_baytes(value,baytes_Range):
	print_status=value
	for i in range(baytes_Range):
		print_status+=1
		bayts=random._urandom(100)*1000
		bayts=str(bayts)
		file_baytes=open('main.txt','a')
		file_baytes.write(bayts)
		print(f'download baytes : {i}{print_status}',end='\r')
	time.sleep(1)
	print_status_start='[*] Done:Start Ddos <python3 Iso-Dos.py -help>'
	print(print_status_start)
__main__=0
__name__=500
try:
	write_baytes(__main__,__name__)
except:
	print('Close')
	