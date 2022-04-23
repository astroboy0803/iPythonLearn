
# assigning value to variable
counter = 100 # integer
miles = 1000.0 # floating
name = "John" # string
print(counter, miles, name)

# multiple assignment
a = b = c = 1
print(a, b, c)
a, b, c = 1, 2.0, "John"
print(a, b, c)

# 用來將變數刪除
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