# assertion
def KelvinToFahrenheit(temperature):
    assert temperature >= 0, "Colder than absolute zero!"
    return (temperature - 273) * 1.8 + 32


print(KelvinToFahrenheit(273))
print(KelvinToFahrenheit(505.78))
# print(KelvinToFahrenheit(-5)) # assertionerror

# exception handling
# try: 只能一個
# except: 可有(1或多個)可無, 符合的exception才執行
# else: 可有(只能一個)可無, try沒拋exception才執行
# finally: 可有(只能一個)可無, 一定會執行
# except與finally至少要有一個
# 所有exception都是繼承BaseException
# except: or except BaseException: - 可以catch所有錯誤
try:
    KelvinToFahrenheit(-5)
# except AssertionError as error:
#     print(error)
except (RuntimeError, TypeError, NameError) as error:
    print('runtime or type or name error = ', error)
except BaseException as error:
    print(type(error) is AssertionError)
    print('base exception = ', error)
else:
    print('success')
finally:
    print('in finally..')


# raise exception - 拋錯
def roleLevel(level):
    if level < 1:
        raise Exception(level)
    return level


try:
    level = roleLevel(-10)
    print("level =", level)
except Exception as exception:
    print('exception =', exception.args[0])


# create custom exception
class LevelError(RuntimeError):
    def __init__(self, level):
        self.level = level
        super().__init__(self.level)


def roleLevel2(level):
    if level < 1:
        raise LevelError(level)
    return level


try:
    level = roleLevel2(-20)
    print("level =", level)
except LevelError as error:
    print('Level Error =', error)
