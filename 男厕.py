binary_string = "111001111001010010110111"

# 将二进制转换为整数
integer_value = int(binary_string, 2)

# 将整数转换为字节串
byte_string = integer_value.to_bytes((integer_value.bit_length() + 7) // 8, "big")

# 将字节串解码为UTF-8编码的字符串
utf8_string = byte_string.decode("utf-8")

print(utf8_string)

#输出'男'代表的二进制数
x = bytes('男',encoding='utf-8')
print(x)
X = ''.join(format(byte, '08b') for byte in x)
print(X,end="\n\n")


#输出'小心地滑'代表的二进制数
y = bytes('小心地滑',encoding='utf-8')
print(y)
Y = ''.join(format(byte, '08b') for byte in y)
print(Y)
time = 0

#按照照片的形式输出
print("\n\t\t\t小心地滑")
for i in Y:
    print(i,end='')
    time = time + 1
    if time % 24 == 0:
        print("  ",end="")
        if time % 48 == 0:
            print("\n",end="")
