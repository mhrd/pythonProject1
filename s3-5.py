# pip install mysql-connector-python
import mysql.connector

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
        self.connection = mysql.connector.connect(
            host='localhost',
            user='test',
            password='Password',
            # database='your_database',
            port=3306
        )
        self.cursor = self.connection.cursor()
        self.DBinit()

    def DBinit(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS contacts")
        self.cursor.execute("USE contacts")
        create_table_query = """
        CREATE TABLE IF NOT EXISTS contacts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            phone_number VARCHAR(11)
        )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def add_contact(self, person):
        insert_query = "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)"
        values = (person.get_first_name(), person.get_last_name(), person.get_phone_number())
        self.cursor.execute(insert_query, values)
        self.connection.commit()
        print(person.get_first_name(), 'added👍')

    def display_contacts(self):
        select_query = "SELECT first_name, last_name, phone_number FROM contacts"
        self.cursor.execute(select_query)
        results = self.cursor.fetchall()

        if not results:
            print("Phone book is empty.")
        else:
            print("Contact list:")
            for result in results:
                print(f"First Name: {result[0]}")
                print(f"Last Name: {result[1]}")
                print(f"Phone Number: {result[2]}")
                print('----------------')

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
        print("Database connection closed.")

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
    print("\n")

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
        phone_book.close_connection()
        print("Exiting the phone book. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
