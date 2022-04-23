a, b = 10, 21

# arithmetic
print(a + b)
print(a - b)
print(a * b)
print(b / a)  # 3.0後, 一般除法就會產生浮點數
print(b // a)  # 只取整數
print(b % a)
print(b ** 3)  # power用法

# comparison
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# assignment
c = a + b
print(c)
c += a
print(c)
c -= a
print(c)
c *= a
print(c)
c /= a
print(c)
c **= 2
print(c)
c //= 2
print(c)
c %= a
print(c)

# Bitwise
bitA = 0b00111100  # 60
bitB = 0b00001101  # 13
print(bin(bitA & bitB))
print(bin(bitA | bitB))
print(bin(bitA ^ bitB))
print(bin(~bitA))  # 補數
# 計算速度比原本加減快
print(bin(bitA << 2), bitA << 2)  # 等於bitA *= 4(2**2)
print(bin(bitA >> 2), bitA >> 2)  # 等於bitA /= 4(2**2)

# Logical
isA = True
isB = False
print(isA and isB)
print(isA or isB)
print(not (isA and isB))

# membership
list = ["a", "b", "c", "d", "e"]
print('a' in list)
print('a' not in list)

# identity - 比對兩物件的記憶體位置
list2 = list
print(list2 is list)
print(list2 is not list)
list3 = list.copy()
print(list3 is list)
print(list3 is not list)
