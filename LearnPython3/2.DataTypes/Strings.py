# create simply
var1 = 'Hello World!'
var2 = "Python Programming"
print(var1, var2)

# substring
print("var1[0] =", var1[0])
print("var2[1:5] =", var2[1:5])
print("Updated String:-", var1[:6] + 'Python')

# escape characters
print('\a')  # bell or alert
print('\b')  # backspace
print('\n')  # newline
print('\t')  # tab

# operators
var3 = var1 + ' ' + var2
print(var3)
var4 = var1 * 2
print(var4)
# 不像其它程式語言用contains, 符合python的易讀性
print('H' in var4)
print('H' not in var4)
# raw string, 不理會跳脫字元
print(r'\n')
print(R'\n')
print('C:\\nowhere')
print(r'C:\\nowhere')

# formatting operator
print("My name is %s and weight is %d kg!" % ('Zara', 80))  # like c
print('{0}, {1}, {2}'.format('a', 'b', 'c'))
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format(*'abc'))
print('{0}{1}{0}'.format('abra', 'cad'))
print('{:+f}; {:+f}'.format(3.14, -3.14))
print('{: f}; {: f}'.format(3.14, -3.14))
print('{:-f}; {:-f}'.format(3.14, -3.14))

# Triple Quotes - 多行字串
lines = """
this is a long string that is made up of several lines and non-printable characters such as 
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like this within the brackets [ \n ], or just a NEWLINE within the variable assignment will also show up
"""
print(lines)

# unicode - python 3 string已是unicode
varU = "가"  # value = 44032, hex = 0xAC00
print(varU.encode('unicode_escape'))
