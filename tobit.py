num = 9223653520505307912
num = 9223372036854775808


# ""
# "9223372036854775872" 荣耀平原 转换后
# 9223372036854775808  转换后0

# num = 25
# ""
get_bin = '0b000000000000000000000000000000000000000000000000000000000000000'

to_int = int(get_bin, 2)
to_bin = bin(num)

print(to_bin)

print(to_int)


# ""9223372036854775810"


# 0b1000000000000000000000000000000000000000000000000000000000000000
# 0b  1000 0000  0000 0001  0000 0000  0000 0010  0000 0101  0000 0000  0000 0011  0000 1000
# 0b  100 0000 0000 0000 0011 0000 1000
# 0b  11001
