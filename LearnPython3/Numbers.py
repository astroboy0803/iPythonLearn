import math
import decimal
import random

var1 = 1
var2 = 10
print(var1, var2)
del var1, var2
# delete後就不見, 故存取會出現compiler error
# print(var1, var2)

# 重新給值後才可以再次使用
var1 = "var1"
var2 = "var2"
print(var1, var2)

# integer
iDA = 1 # 10進制
iHA = 0xA # 16進制
iOA = 0o17 # 8進制
iNA = -120 # 負數
print(iDA, iHA, iOA, iNA)

# floating
fPA = 123.215 # 正數
fNA = -21.9 # 負數
fEA = 2E2 # 2 * 10的平方(E)
fEA2 = 2e2 # 2 * 10的平方(e)
print(fPA, fNA, fEA, fEA2)

# complex
cPA = 3.14j
cPA2 = 45.j
cNA = -.6465 + 0J
cEA = 3e2 + 26j
print(cPA, cPA2, cNA, cEA)

# conversion - 失敗會拋錯
# print(int('a'))
print(int('152'))
print(float('152'))
print(complex('152'))
print(complex(152, 65))

# mathematical function

# abs與fabs類似
# fabs: 只能用在integer和floating
# abs: 內置函數且所有number都可使用
print("abs與fabs")
print(abs(-5))
# print(math.fabs(complex(-5)))
print(math.fabs(-5.5))

# 大於小於
# ceil: 取得大於等於的整數
# floor: 取得小於等於的整數
print("大於小於")
print(math.ceil(-9.5))
print(math.ceil(9.4))
print(math.floor(-9.5))
print(math.floor(9.4))

# 指數與對數
print("指數與對數")
print(pow(10, 2)) # 內置函數(base的N次方)
print(math.exp(2)) # 自然底數e的平方
print(math.log(12))
print(math.log10(100))

# 最大最小值
print("最大最小值")
print(max(1,5,10,-1))
print(min(1,5,10,-1))

# 其它
print("其它")
print(math.sqrt(100))
print(math.modf(1256.354)) # return tuple = (小數, 整數)
print(round(125.345))
print(round(125.345, 1))
# 發現5沒辦法正確四捨五入
print(round(125.345, 2))
# decimal後發現值本身不精確 = 125.344999...
print(decimal.Decimal(125.345))
# 最好的做法是採用decimal.Context(prec = 轉置後的長度)
print(decimal.Context(prec=5, rounding=decimal.ROUND_HALF_UP).create_decimal(125.345))

# Random
print("Random")
print(random.choice([1, 2, 3, 5, 9]))
print(random.randrange(1, 100, 2)) # 1~100的奇數
print(random.randrange(100)) # 0~99
print(random.random()) # 0~1 浮點數
random.seed(10) # 使用種子10產生隨機數, 種子相同結果就相同
print(random.random()) # 0~1 浮點數
random.seed(10)
print(random.random()) # 0~1 浮點數
list = [20, 16, 10, 5]
random.shuffle(list) # 對sequence隨機排序
print(list)
random.shuffle(list)
print(list)
print(random.uniform(7, 14)) # 產生7~14(含上下限)的浮點數

# 三角函數
print("三角函數")
print(math.sin(math.pi/2))
print(math.cos(math.pi))
print(math.tan(0))
print(math.hypot(3, 4)) # sqrt(x*x + y*y)
print(math.degrees(math.pi/4)) # 弧度轉角度
print(math.radians(180 / math.pi))