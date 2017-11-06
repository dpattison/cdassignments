def odd_even(number):
    for num in range(1, number + 1):

        if num % 2 == 0:
            print "Number is " + str(num) + ". This is an even number."
        else:
            print "Number is " + str(num) + ". This is an odd number."


# odd_even(2000)


a = [2, 4, 10, 16]


def comp(alist, multi):
    alist = [x * multi for x in alist]
    return alist


print comp(a, 19)
print comp([2, 4, 5], 3)


def layered_multiples(arr):
    new_array = [[1 for x in xrange(arr[x])] for x in xrange(len(arr))]
    return new_array


x = layered_multiples(comp([2, 4, 5, 6], 3))
print x


