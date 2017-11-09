import random


def scores():
    print "Scores and Grades"
    for x in xrange(10):
        random_num = random.randint(60, 100)
        if random_num >= 60 and random_num <= 70:
            grade = "D"
        elif random_num >= 70 and random_num <= 79:
            grade = "C"
        elif random_num >= 80 and random_num <= 89:
            grade = "B"
        elif random_num >= 90 and random_num <= 100:
            grade = "B"
        print "Score: " + str(random_num) + "; Your grade is " + grade
    print "End of the program. Bye!"


scores()
