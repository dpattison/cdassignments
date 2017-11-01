
words = "It's thanksgiving day. It's my birthday,too!"
find = "day"
print words.find(find)
month = "month"
print words.replace(find, month)
x = [2, 54, -2, 7, 12, 98]
print min(x)
print max(x)

x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print x[0]
print x[len(x) - 1]
y = [x[0], x[len(x) - 1]]
print y

x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
x.sort()
print x
half = len(x) / 2
print half
half1 = x[:half]
half2 = x[half:]
print half1
print half2
half2.insert(0, half1)
print half2
