# defining a function
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return  # 等同None


# Calling
printme('This is first call to the user defined function!')
printme('Again second call to the same function!')


# Parameters - Pass by Reference
def changeme(mylist):
    "This changes a passed list into this function"
    print("before change:", list)
    mylist[2] = 50
    print("after change:", list)
    return


mylist = [1, 2, 3, 4, 5]
changeme(mylist)
print("outside:", mylist)


def changeme2(mylist2):
    "This changes a passed list into this function"
    mylist = [10, 20, 30]  # 重新宣告List, 故與外面已為不同記憶體位置
    print("inside:", mylist)


mylist2 = [1, 2, 3, 4, 5]
changeme2(mylist2)
print("outside:", mylist2)

# required arguments
# printme()  # error, missing required positional argument

# keyword arguments
printme(str='hello')


def printinfo(name, age):
    "This prints a passed info into this function"
    print("Name:", name)
    print("Age:", age)
    return


printinfo(age=100, name='John')


# default arguments
def printinfo2(name, age=28):
    "This prints a passed info into this function"
    print("Name:", name)
    print("Age:", age)
    return


printinfo2(age=15, name='John')
printinfo2(name='John')


# variable-length arguments
def printinfo3(arg1, *vartuple):
    "This prints a variable passed arguments"
    print("Output is:")
    print(arg1)
    for val in vartuple:
        print(val)
    return


printinfo3(10)
printinfo3(70, 60, 50)

# anonymous function
sum = lambda arg1, arg2: arg1 + arg2
print("sum = ", sum(10, 20))
print("sum = ", sum(20, 20))

# return
# 如果function沒有return or 只有return(沒有回傳值), 結果會得到None
result = printme('abc')
print(result == None)


def noReturn(a, b):
    print(a, b)


rr = noReturn('a', 'b')
print(rr)


def sum(arg1, arg2):
    total = arg1 + arg2
    print("Inside:", total)
    return total


total = sum(50, 60)
print("Outside:", total)

# global and local variables
aTotal = 0


def aSum(arg1, arg2):
    aTotal = arg1 + arg2
    print("inside aTotal =", aTotal)
    return aTotal


aSum(10, 20)
print("outside aTotal =", aTotal)
