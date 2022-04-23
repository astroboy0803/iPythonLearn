# create
set1 = set([1, 3, 5, 7, 9])
print(set1)
set2 = set(['a', 'b', 'c', 'd', 'e'])
print(set2)
set3 = set(['a', 1, 2.5, 'd'])
print(set3)
set4 = set([1, 2, 3, 3, 1, 2])  # 不會重複
print(set4)

# add and update
set1.add(10)
print(set1)
set1.add(5)
print(set1)

# delete
set1.remove(10)
print(set1)

# 集合操作
setB = set([3, 10, 100, 6, 9])
print(set1 & setB)
print(set1 | setB)
