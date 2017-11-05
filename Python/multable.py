seed = 20
top = "x  "

for x in range(1, seed + 1):
    top = top + str(x) + " "
print top

for number1 in range(1, seed + 1):
    s = str(number1) + "  "
    for number2 in range(1, seed + 1):
        s = s + str(number1 * number2) + " "
    print s
