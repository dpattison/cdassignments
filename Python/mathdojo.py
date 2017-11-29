class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *numbers):
        for number in numbers:
            if isinstance(number, list) or isinstance(number, tuple):
                for each in number:
                    self.result += each
            elif isinstance(number, int):
                    self.result += number
        return self
    def subtract(self, *numbers):
        for number in numbers:
            if isinstance(number, list) or isinstance(number, tuple):
                for each in number:
                    self.result -= each
            elif isinstance(number, int):
                    self.result -= number
        return self



md = MathDojo()
# print md.add([1,3,4],2).add(2,5).result
# print md.add(2).add(2,5).subtract(3,2).result
# print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result

print md.add((1,3,5,3),[1,1],2).result
