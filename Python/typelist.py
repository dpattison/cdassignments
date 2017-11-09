l = ['magical unicorns', 19, 'hello', 98.98, 'world']
l = [2, 3, 1, 7, 4, 12]
l = ['magical', 'unicorns']

string = ""
total = 0
strings = False
numbers = False

for item in l:
    if isinstance(item, str):
        string = string + " " + item
        strings = True
    elif isinstance(item, int):
        total = total + item
        numbers = True

if strings and numbers:
    print "Mixed"
    print "String:", string
    print "Total:", total
elif strings and not numbers:
    print "Strings only"
    print "String:", string
elif not strings and numbers:
    print "Numbers only"
    print "Total:", total
