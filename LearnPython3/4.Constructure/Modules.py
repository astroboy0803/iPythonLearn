# import語法: import module1 [, module2 [,...moduleN]
# ex: import support, MyMethods
# python會下列路徑依序搜尋module:
# 1.程式所在的directory(不含sub directory)
# 2.PYTHONPATH
# 3.Python的default path = python安裝路徑下的lib目錄部份位置
# 可以使用sys.path來確認
# 另一種import方式為 from...import, 語法:
# 1.載入部份: from modulename import name1[, name2[,...nameN]
# 2.全部載入: from modulename import *
# from...import不用加上moduleName作為前綴詞
# 每隻程式都有一個全域變數 __name__
# 當該程式為主程式運行時, __name__ == '__main__'
# 但若被import到別的程式中執行時, __name__ == module's name

import sys

from fib import fib
from support import *

# 可用sys.path來檢查
print(sys.path)

print(fib(100))
# print(fib2(100)) # NameError, 沒有import

# 非module == __main__
print("local __name__:", __name__)

# 使用from...import * = 全部載入, 所有方法都可以執行
print_func('John')
print_func2('John')

# namespace = dictionary + objects
# Python的變數可分local or global
# 1.local有local namespace
# 2.global有global namespace
# 3.在沒有特別使用namespace的情況下, local和global名字相同時, 以local為主
# 在function內指定值給變數時, 該變數都被視為local
# 若想要在function內指定資料給global, 必須告訴Python該變數為global
# 語法: global varName

money = 2000


# def AddMoney():
#     money = money + 1  # UnboundLocalError,
#
#
# print(money)
# AddMoney()
# print(money)

def AssigMoney():
    money = 3000


print(money)
AssigMoney()  # 無法更新global
print(money)


def AssigMoney2():
    global money  # 告訴python這是全域變數
    money = 3000


print(money)
AssigMoney2()
print(money)

# 使用dir得知module資訊
print(dir(sys))


def showAllNames():
    inVar = 100
    print("globals =", globals())  # 不會包含inVar
    print("locals =", locals())  # 只有inVar


showAllNames()

import Phone

Phone.Pots()
Phone.Isdn()
Phone.G3()
