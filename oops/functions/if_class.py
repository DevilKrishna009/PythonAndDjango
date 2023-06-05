class IfClass:
    def condition(self, num):
        if num > 0:
            return f"{num} is positive"
        else:
            return f"{num} is negative"


obj = IfClass()
print(obj.condition(3))

