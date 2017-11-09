word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna', 'Davoooo']
char = 'o'
new_list = []


for item in word_list:
    for letter in item:
        if letter == char:
            new_list.append(item)
            break

print new_list
