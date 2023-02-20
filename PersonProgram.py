import PersonClass as pc

person = pc.Person("Dad", "12103 Queensbury Ln", "713-366-2755")
customer = pc.Customer("Mom", "12103 Quensbury Ln", "832-266-7534", 75, True)

print(person.print_person())
print(customer.print_person())
