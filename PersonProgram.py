import PersonClass as pc

# define the variables
name = "Dad"
address = "12103 Queensbury Ln"
phone_number = "713-366-2755"
customerno = 1234
mailinglist = True

# create an instance of the person class
person = pc.Person(name, address, phone_number)

# create an instance of the customer class
customer = pc.Customer(name, address, phone_number, customerno, mailinglist)

customer.print_person()


# print(person.print_person())
# print(customer.print_person())
