class Person:

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def print_person(self):
        print(self.name, self.address, self.phone)


class Customer(Person):
    def __init__(self, name, address, phone, customerno, mailinglist):
        Person.__init__(self, name, address, phone)

        self.customerno = customerno
        self.mailinglist = mailinglist

    def print_person(self):
        print(self.name, self.address, self.phone)
