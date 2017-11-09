my_info = {"name": "Dave", "age": "45",
           "country of birth": "The United States", "favorite language": "Python"}

# print my_info


def printdict(a):
    for key, data in a.iteritems():
        print "My " + key + " is " + data


printdict(my_info)
