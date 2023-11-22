class Person:
    def __init__(self, first_name, last_name, phone_number):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_phone_number(self):
        return self._phone_number

class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, person):
        self.contacts.append(person)
        print(person.get_first_name(), 'added👍')

    def display_contacts(self):
        if not self.contacts:
            print("Phone book is empty.")
        else:
            print("Contact list:")
            for person in self.contacts:
                print("First Name:", person.get_first_name())
                print("Last Name: ", person.get_last_name())
                print("Phone Number: ", person.get_phone_number())
                print('----------------')

def is_valid_phone_number(phone_number):
    return len(phone_number) == 11 and phone_number.isdigit()

# Create a phone book
phone_book = PhoneBook()

while True:
    print("\nMenu:")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        first_name = input("Please enter the first name: ")
        last_name = input("Please enter the last name: ")

        while True:
            phone_number = input("Please enter the 11-digit phone number: ")
            if is_valid_phone_number(phone_number):
                break
            else:
                print("Invalid phone number. Please enter exactly 11 digits.")

        person_object = Person(first_name, last_name, phone_number)
        phone_book.add_contact(person_object)

    elif choice == "2":
        phone_book.display_contacts()

    elif choice == "3":
        print("Exiting the phone book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
