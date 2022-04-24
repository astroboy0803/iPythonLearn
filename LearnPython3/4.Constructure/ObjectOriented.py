# create class
class Employee:
    'Common base class for all employees'
    empCount = 0  # class variable

    def __init__(self, name, salary):
        self.name = name  # instance variable
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("total employee %d" % (Employee.empCount))

    def displayEmployee(self):
        print(f"Name : {self.name}, Salary: {self.salary}")


# create instance object
emp1 = Employee("John", 100)
emp2 = Employee("Bird", 80)
emp1.displayEmployee()
emp2.displayEmployee()

# accessing attributes
print(f"total employee = {Employee.empCount}")

print(emp1.__dict__)
emp1.age = 30  # add attribute
emp1.salary = 110  # update attribute
print(emp1.__dict__)
del emp1.age  # delete attribute
# print(emp1.age) # error, age屬性已刪除

# 一般作法
# print(getattr(emp1, 'age')) # error, 沒有屬性就拋錯
print(emp1.__dict__)
if ~hasattr(emp1, 'age'):
    setattr(emp1, 'age', 18)
print(getattr(emp1, 'age'))
print(emp1.__dict__)
delattr(emp1, 'age')

# built-in class attributes
print(emp1.__dict__['name'])
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)
print(Employee.__dict__)


# destroy object
# python的記憶體管理
# GC(garbage collection)負責
# 不定期檢查目前使用的記憶體, 如果已不在使用就回收
# 判斷還有沒有使用採用RC(reference count)
# 被指定 or 放到container(list, tuple, dict...) -> RC + 1
# del or reassign or 離開scope -> RC - 1
# GC還是有辦法回收retain cycle的空間, 但必須
# 1. 單一的__del__, 可以確定回收順序
# 2. 須有GC去偵測與打破cycle, 故需要時間
# 會產生cycle的情況可以使用WeakRef來解決
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")


pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))
del pt1
print(pt2.__dict__)
del pt2
del pt3  # 當無其它參考後, 才會執行__del__
print('destroy done')


# Inheritance
# support 多重繼承
class Parent:
    parentAtt = 100

    def __init__(self):
        print("Calling parent constructor")

    def myMethod(self):
        print('Calling parent MyMethod')

    def parentMethod(self):
        print('Calling Parent Method')

    def setAttr(self, attr):
        Parent.parentAtt = attr

    def getAttr(self):
        print(f"Parent attribute = {Parent.parentAtt}")


class Child(Parent):
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')


child = Child()
child.childMethod()
child.parentMethod()
child.setAttr(200)
child.getAttr()
parent = Parent()
print(isinstance(child, Parent))
print(isinstance(child, Child))
print(isinstance(parent, Child))
print(issubclass(Child, Parent))
print(issubclass(Parent, Child))


# overriding method
class SChild(Parent):
    def myMethod(self):
        print('Calling child MyMethod')


schild = SChild()
schild.myMethod()


# Overloading Operator
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


vec1 = Vector(2, 10)
vec2 = Vector(5, -2)
print(vec1 + vec2)

# Data hidding - 參考UnderScore
