class call(object):
    def __init__(self, caller_id, caller_name, caller_phone, time, reason):
        self.caller_id = caller_id
        self.caller_name = caller_name
        self.caller_phone = caller_phone
        self.time = time
        self.reason = reason

    def display(self):
        print "ID: " + str(self.caller_id)
        print "Name: " + self.caller_name
        print "Phone: " + self.caller_phone
        print "Time: " + self.time
        print "Reason: " + self.reason
        return self

call1 = call(1, "Dave", "805-252-7999", "10:16am", "unhappy")
call2 = call(2, "Fred", "805-555-5555", "10:10am", "unhappy")
# call1.display()

class callcenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def add(self, call):
        self.calls.append(call)
        self.queue_size += 1
        return self
    def remove(self):
        self.calls.remove[0]
        self.queue_size -= 1
        return self
    def info(self):
        print "Calls in Queue: " + str(self.queue_size)
        for each in self.calls:
            print "Name: " + each.caller_name
            print "Phone: " + each.caller_phone
            print "Time: " + each.time
            print
        return self
    def removecall(self, phonenum):
        for call in self.calls:
            if call.caller_phone == phonenum:
                self.calls.remove(call)
                self.queue_size -= 1
        return self
    def sortbytime(self):
        self.calls = sorted(self.calls, key = lambda call: call.time)

cc1 = callcenter()
cc1.add(call1).add(call2)
cc1.info()
cc1.sortbytime()
cc1.info()

# cc1.removecall("805-252-7999")
# cc1.info()