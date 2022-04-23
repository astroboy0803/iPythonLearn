# create
tup1 = (1, 2, 3, 4, 5)
print(tup1)
tup2 = 'a', 'b', 'c', 'd', 'e'
print(tup2)
tup3 = 'a', 1, 2.6, 'd', 8
print(tup3)
tupEmpty = ()
print(tupEmpty)
tupOneValue = ('a',)  # 必須加上,才可視為tuple
print(tupOneValue)
tupIllegial = ('a')  # 沒有, 被視為字串
print(tupIllegial)

# access
print(tup1[0])
print(tup2[2:4])
print(tup3[:3])
print(tup3[2:])
T = ("C++", "Java", "Python")
print(T[2])
print(T[-2])

# update - immutable

# delete - only remove an entire tuple
tupDel = tup3
print(tupDel)
del tupDel
# print(tupDel) # 已被刪除不存在, 無法讀取

# operations
print(len(tup1))
tup4 = tup1 + tup2
print(tup4)
tup5 = ('Hi!',) * 4
print(tup5)
print('a' in tup2)
print('a' not in tup2)
for x in tup1:
    print(x, end='')
print('')
print(max(tup1))
print(min(tup1))
