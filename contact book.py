contacts = {}

name = input("Enter Name: ")
phone = input("Enter Phone Number: ")

contacts[name] = phone

print("\nContact List")
for name, phone in contacts.items():
    print(name, "-", phone)