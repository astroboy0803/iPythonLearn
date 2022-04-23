list = [1, 2, 3, 4, 5]
itor = iter(list)
print(next(itor))
itor = iter(list)
for x in itor:
    print(x, end="")

print("")
itor = iter(list)
while True:
    try:
        print(next(itor), end="")
    except StopIteration:
        break

print("")
for value in list:
    print(value)


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(5)
print(f)
while True:
    try:
        print(next(f), end=",")
    except StopIteration:
        break
