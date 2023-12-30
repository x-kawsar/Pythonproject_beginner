
class Phone:
    def call(self):
        print('You can call')

    def message(self):
        print('You can message to me')


class Nokia(Phone):
    def Photo(self):
        print('You can take photo')
p = Phone()
p.message()

n = Nokia()
n.Photo()
n.message()

print(issubclass(Nokia, Phone))



