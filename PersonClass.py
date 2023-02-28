class Person:

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def print_person(self):
        print(self.name, self.address, self.phone)

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def print_person(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("Phone:", self.phone)


class Customer(Person):
    def __init__(self, name, address, phone, customerno, mailinglist):
        Person.__init__(self, name, address, phone)

        self.customerno = customerno
        self.mailinglist = mailinglist

    def print_person(self):
        print(self.name, self.address, self.phone)

        print(f"Customer Number: {self.customerno}")

# Hidden attributes are not passed on in inheritance
#
