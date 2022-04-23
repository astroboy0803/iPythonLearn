# create
list1 = [1, 2, 3, 4, 5]
print(list1)
list2 = ["a", "b", "c", "d", "e"]
print(list2)
list3 = ['a', 1, 2.5, 'd']
print(list3)

# access, indexing and sliciing
print(list1[0])
print(list2[2:4])
print(list3[:3])
print(list3[2:])
L = ["C++", "Java", "Python"]
print(L[2])
print(L[-2])

# update
list1[0] = 100
print(list1[0])

# delete - del or remove
print(list1)
del list1[2]
print(list1)

# operations
print(len(list1))
list4 = list2 + list3
print(list4)
list5 = ['Hi!'] * 4
print(list5)
print('a' in list2)
print('a' not in list2)
for x in list1:
    print(x, end='')
print(max(list1))
print(min(list1))
list1.append(4)
print(list1)
list1.extend([6, 9, 100])
print(list1)
print(list1.count(4))
print(list1.index(4))
list1.insert(3, 60)
print(list1)
list1.remove(100)
print(list1)
# remove不存在的值會出現錯誤
# list1.remove(1000)
# print(list1)
list1.pop()
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)


def sortFunc(e):
    return e


list2.sort(reverse=True, key=sortFunc)
print(list2)

aTuple = (1, 2, 3, 4, 5)
print(aTuple)
tupleList = list(aTuple)
print(tupleList)  # convert a tuple into list
