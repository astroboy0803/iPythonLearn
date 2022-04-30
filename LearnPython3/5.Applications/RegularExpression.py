import re

line = "Cats are smarter than dogs"
expression = r'(.*) are (.*?) .*'

# match
matchObj = re.match(expression, line, re.M | re.I)
if matchObj:
    print(matchObj.group())
    print(matchObj.group(1))
    print(matchObj.group(2))
else:
    print("No match")

# search
searchObj = re.search(expression, line, re.M | re.I)
if searchObj:
    print(searchObj.group())
    print(searchObj.group(1))
    print(searchObj.group(2))
else:
    print("Not Found!")

# match(從頭開始比對) vs search(所有符合substring)
dogExpression = r'dogs'
dogMatchObj = re.match(dogExpression, line, re.I | re.M)
if dogMatchObj:
    print(dogMatchObj.group())
else:
    print("(dogs)No Match")

dogSearchObj = re.search(dogExpression, line, re.I | re.M)
if dogSearchObj:
    print(dogSearchObj.group())
else:
    print("(dogs)Not Found!!")

# replacing
sno = "2315-648-997"
num = re.sub(r"#.*$", "", sno)
print(num)
num = re.sub(r"\D", "", sno)
print(num)
