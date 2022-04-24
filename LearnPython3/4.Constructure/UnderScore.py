# reference: https://medium.com/python-language/python-tricks-底線家族的秘密-d84a2ce9cde6

from MyMethods import *


# 前單底線
# 1.shall: 前次執行結果
# 2.程式:
# Python沒有真的Private
# 慣例上用來設定該變數僅內部使用(官網建議)
# 但其實還是可以存取到
# 前單底線的函式, 在from x import *時不會被import進來, 除非:
# 1.指定import該函式
# 2.或在__all__有設定
class Prefix:
    def __init__(self):
        self.public = 1
        self._hopePrivate = 100


prefix = Prefix()
print(prefix.public)
print(prefix._hopePrivate)  # 還是讀的到
prefix._hopePrivate = 30  # 可以更改
print(prefix._hopePrivate)

print(publicFunc())
print(_privateFunc2())


# NameError, 無法讀取__all__沒有設定
# 直接import該函式就可以執行(from MyMethods import _privateFunc)
# print(_privateFunc())

# 前雙底線
# Python會重新命名這個變數(namespace問題), 達到Private效果(但還是可存取)
# 重新命名規則 = _ClassName__AttributeName

class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
# print(counter.__secretCount)  # AttributeError
print(counter._JustCounter__secretCount)

# 後單底線
# 當變數名稱使用到Python保留字時, 會習慣(無強制)在變數後加上單底線
class_ = 'A'

# 前後雙底線
# 特殊用途使用, 表示該方法是要讓開發者覆寫(override)
# 像是__init__, __del__, __str__等
