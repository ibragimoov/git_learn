class User:
    _name = ''
    age = ''
    password = ''
    email = ''
    phone = ''
    address = ''

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_phone(self):
        return self.email

user1 = User()
user1.set_name('Боб')
print(user1.get_name())