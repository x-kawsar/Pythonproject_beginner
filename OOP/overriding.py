
class Phone:
    def __init__(self):
        print('I am in phone class')



class Nokia(Phone):
    def __init__(self):
        super().__init__()
        print('I\'m in Nokia Class')


n = Nokia()

print(issubclass(Nokia, Phone))



