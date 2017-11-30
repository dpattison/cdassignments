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

call1 = call(1, "Dave", "805-252-7999", "10:15am", "unhappy")
call2 = call(2, "Fred", "805-555-555", "10:15am", "unhappy")
call1.display()

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
            print "PHone: " + each.caller_phone
        return self

cc1 = callcenter()
cc1.add(call1).add(call2)
cc1.info()



