import pandas as pd
from colorama import init, Fore
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


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
        self.contacts = pd.DataFrame(columns=['First Name', 'Last Name', 'Phone Number'])

    def add_contact(self, person):
        self.contacts = self.contacts.append({
            'First Name': person.get_first_name(),
            'Last Name': person.get_last_name(),
            'Phone Number': person.get_phone_number()
        }, ignore_index=True)
        print(Fore.GREEN, person.get_first_name(), 'added👍')

    def display_contacts(self):
        if self.contacts.empty:
            print(Fore.CYAN, "Phone book is empty.")
        else:
            print("Contact list:")
            print(Fore.YELLOW, self.contacts)
            print('----------------')

    def write_to_file(self, filename='contacts.xlsx'):
        self.contacts.to_excel(filename, index=False)
        print(Fore.GREEN, "Contacts written to file.")

    def read_from_file(self, filename='contacts.xlsx'):
        try:
            self.contacts = pd.read_excel(filename)
            print(Fore.GREEN, "Contacts read from file.")
        except FileNotFoundError:
            print(Fore.RED, f"File '{filename}' not found. No contacts loaded.")


def is_valid_phone_number(phone_number):
    return len(phone_number) == 11 and phone_number.isdigit()


# Create a phone book
phone_book = PhoneBook()

while True:
    print(Fore.WHITE, "\nMenu:")
    print(Fore.WHITE, "1. Add Contact")
    print(Fore.WHITE, "2. Display Contacts")
    print(Fore.WHITE, "3. Write to File")
    print(Fore.WHITE, "4. Read from File")
    print(Fore.WHITE, "5. Exit")

    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
    print(Fore.WHITE, "\n")

    if choice == "1":
        first_name = input("Please enter the first name: ")
        last_name = input("Please enter the last name: ")

        while True:
            phone_number = input("Please enter the 11-digit phone number: ")
            if is_valid_phone_number(phone_number):
                break
            else:
                print(Fore.RED, "Invalid phone number. Please enter exactly 11 digits.")

        person_object = Person(first_name, last_name, phone_number)
        phone_book.add_contact(person_object)

    elif choice == "2":
        phone_book.display_contacts()

    elif choice == "3":
        phone_book.write_to_file()

    elif choice == "4":
        phone_book.read_from_file()

    elif choice == "5":
        print("Exiting the phone book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
