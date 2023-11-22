from colorama import init, Fore


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
        print(Fore.GREEN, person.get_first_name(), 'added👍')

    def display_contacts(self):
        if not self.contacts:
            print(Fore.CYAN, "Phone book is empty.")
        else:
            print("Contact list:")
            for person in self.contacts:
                print(Fore.YELLOW, "First Name:", person.get_first_name())
                print(Fore.YELLOW, "Last Name: ", person.get_last_name())
                print(Fore.YELLOW, "Phone Number: ", person.get_phone_number())
                print(Fore.YELLOW, '----------------')

    def write_to_file(self, filename='contacts.txt'):
        with open(filename, 'w') as file:
            for person in self.contacts:
                file.write(
                    person.get_first_name() + '&' + person.get_last_name() + '@' + person.get_phone_number() + "\n")

    def read_from_file(self, filename='contacts.txt'):
        self.contacts = []  # Clear existing contacts
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split('@')
                    if len(parts) == 2:
                        first_last, phone_number = parts
                        first_name, last_name = first_last.split('&')
                        person_object = Person(first_name, last_name, phone_number)
                        # self.contacts.append(person_object)
                        self.add_contact(person_object)
        except FileNotFoundError:
            print(f"File '{filename}' not found. No contacts loaded.")


def is_valid_phone_number(phone_number):
    return len(phone_number) == 11 and phone_number.isdigit()


# Create a phone book
phone_book = PhoneBook()

while True:
    print(Fore.RED + "\nMenu:")
    print(Fore.RED + "1. Add Contact")
    print(Fore.RED + "2. Display Contacts")
    print(Fore.RED + "3. Write to File")
    print(Fore.RED + "4. Read from File")
    print(Fore.RED + "5. Exit")

    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
    print(Fore.RED + "\n")

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
        phone_book.write_to_file()
        print("Contacts written to file.")

    elif choice == "4":
        phone_book.read_from_file()
        print("Contacts read from file.")

    elif choice == "5":
        print("Exiting the phone book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
