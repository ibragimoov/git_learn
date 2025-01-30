class User:
    name = ''
    age = ''
    password = ''
    email = ''

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.email


user1 = User()
user1.name = 'Bob'
user1.email = 'bob@gmail.com'
print(user1.get_name())