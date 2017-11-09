students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def print_students(a):
    for item in a:
        print item["first_name"] + " " + item["last_name"]
 
#print_students(students)


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def print_users(a):
    for item, data in a.iteritems():
        print item
        for index, names in enumerate(data):
            print str(index + 1) + " - " + names["first_name"] + " " + names["last_name"] + " - " + str(len(names["first_name"])+len(names["last_name"]))
 
print_users(users)