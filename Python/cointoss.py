import random


def cointoss(a):
    head = 0
    tail = 0
    for x in range(1, a + 1):
        toss = random.randint(1, 2)
        if toss == 1:
            result = "head"
            head+=1
        else:
            result = "tail"
            tail+=1

        print "Attempt #" + str(x) + ": Throwing a coin... It's a " + result + "! ... Got " + str(head) + " head(s) so far and " + str(tail) + " tail(s) so far"
    if head > tail:
        variance = head - (a * .5)
        print "Variance is heads +" + str(variance)
    else:
        variance = tail - (a * .5)
        print "Variance is tails +" + str(variance)
    


cointoss(5000)
