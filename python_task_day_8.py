# Contact book dictionary:
contacts = {}

# Add a new contact:
def add_contact(name, phone, email):
    contacts[name] = {'Phone': phone, 'Email': email}

# Update existing contact:
def update_contact(name, phone, email):
    if name in contacts:
        contacts[name] = {'Phone': phone, 'Email': email}

# Retrieve contact details:
def get_contact(name):
    return contacts.get(name, "Contact not found..!")

# View all contacts:
def view_all_contacts():
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}")

# Example usage:
add_contact("Ali", "03356789876", "ali763@example.com")
add_contact("Bisma", "03345634987", "bisma98@example.com")

update_contact("Ali", "03356789876", "ali763@newmail.com")

print(get_contact("Ali"))
print(get_contact("Farman"))

view_all_contacts()
