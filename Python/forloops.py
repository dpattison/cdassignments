# print all odd numbers from 1 to 1000
for num in range(1, 1000, 2):
    print num

#print all multiples of 5
for num in range(5, 1000000, 5):
    print num
    

# sum a list of numbers
a = [1, 2, 5, 10, 255, 3]
b = 0
for num in a:
    b = b + num

print b

# print average of numbers
a = [1, 2, 5, 10, 255, 3]
b = 0
for num in a:
    b = b + num

print b/len(a)
