# create
dictEmpty = {}
print(dictEmpty)
dict1 = {
    'name': 'OOO',
    'radius': 5,
    'PI': 3.14,
}
print(dict1)

# Access
dict = {
    'Name': 'Zara',
    'Age': 7,
    'Class': 'F',
}
print(dict['Name'], dict['Age'])
# print(dict['PI']) # 存取不存在的資料會拋錯

# update and add
dict['Age'] = 8
dict['School'] = 'Warriors'
print(dict['Age'], dict['School'])

# delete
dictDel = dict.copy()
print(dictDel)
del dictDel['Name']  # remove with key 'Name'
print(dictDel)
dictDel.clear()  # remove all
print(dictDel)
del dictDel  # remove vairable
# print(dictDel)  # error, 變數已不存在

# keys must be immutable and hashable type
# dictError = {['Name']: 'Zara'}  # error, unhashable type: 'list'
# key可不同型別但一定要是immutable
dictKeyImmutable = {
    'name': 'XXX',
    6: 5,
    ('PI',): 3.14,
}
print(dictKeyImmutable)

# function and methods
print(str(dict))
print(len(dict))
print(type(dict))
print(dict.get('Name'))
print(dict.get('Sex'))  # 取不存在的值會得到None
print(dict.get('Sex', 'Male'))  # 不存在就給預設值, 但不會影響原本dictionary
print(dict)
print(dict.setdefault('Sex', 'Male'))  # 不存在就將預設值放入dictionary並回傳
print(dict)
print('Name' in dict)
print('Name' not in dict)
print('Zara' in dict)  # 這語法是檢查KEY不是VALUE
print(dict.items())
print(dict.keys())
print(dict.values())

dictFromKeys = dictEmpty.fromkeys(('key1', 'key2', 'key3'), 0)
print(dictFromKeys)
dictFromKeys.update(dict)
print(dictFromKeys)
