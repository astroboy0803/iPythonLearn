# line and indentation
if True:
    print("true")
else:
    print("false")

# multiple line
days = [
    "Mon",
    "Tue",
    "Wen",
    "Thu",
    "Fri",
]
strDays = days[0] + "," + \
    days[1] + "," + \
    days[2] + "," + \
    days[3] + "," + \
    days[4]
print(strDays)

# quotation - string literal
single = 'a'
double = "a"
triple = """a
bcd
efg
"""
print(single, double, triple)

# waiting for the user
input("\n\nPress the enter key to exit.")

# multiple statement on a single line
country = 'Taiwan';print(country)

# multiple statement group as suites
# start keyword and end with colon
if single == 'abc':
    print("is abc")
elif single == "def":
    print("is def")
else:
    print("unknow", single)