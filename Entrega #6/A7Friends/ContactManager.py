import os
import tempfile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTACTS_FILE = os.path.join(BASE_DIR, "friendsContact.txt")

class ContactManager:
    @staticmethod
    def create_contact(name, number):
        try:
            if not os.path.exists(CONTACTS_FILE):
                with open(CONTACTS_FILE, 'w'): pass
            
            found = False
            with open(CONTACTS_FILE, 'r') as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split('!')
                        if len(parts) >= 2 and (parts[0] == name or parts[1] == str(number)):
                            found = True
                            break
            
            if not found:
                with open(CONTACTS_FILE, 'a') as file:
                    file.write(f"{name}!{number}\n")
                return True, "Contact added successfully"
            return False, "Contact already exists or number is registered"
            
        except Exception as e:
            return False, f"Error: {str(e)}"

    @staticmethod
    def find_contact(name):
        try:
            if not os.path.exists(CONTACTS_FILE) or os.path.getsize(CONTACTS_FILE) == 0:
                return None, "No contacts registered"
            
            with open(CONTACTS_FILE, 'r') as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split('!')
                        if len(parts) >= 2 and parts[0] == name:
                            return parts[1], None
            
            return None, "Contact not found"
            
        except Exception as e:
            return None, f"Error: {str(e)}"

    @staticmethod
    def update_contact(name, number):
        try:
            if not os.path.exists(CONTACTS_FILE):
                return False, "Contacts file does not exist"
            
            found = False
            temp_file = tempfile.NamedTemporaryFile('w', delete=False)
            
            with open(CONTACTS_FILE, 'r') as file, temp_file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split('!')
                        if len(parts) >= 2 and parts[0] == name:
                            temp_file.write(f"{name}!{number}\n")
                            found = True
                        else:
                            temp_file.write(line)
            
            if found:
                os.replace(temp_file.name, CONTACTS_FILE)
                return True, "Contact updated successfully"
            else:
                os.remove(temp_file.name)
                return False, "Contact not found"
            
        except Exception as e:
            return False, f"Error: {str(e)}"

    @staticmethod
    def delete_contact(name):
        try:
            if not os.path.exists(CONTACTS_FILE):
                return False, "Contacts file does not exist"
            
            found = False
            temp_file = tempfile.NamedTemporaryFile('w', delete=False)
            
            with open(CONTACTS_FILE, 'r') as file, temp_file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split('!')
                        if len(parts) >= 2 and parts[0] == name:
                            found = True
                        else:
                            temp_file.write(line)
            
            if found:
                os.replace(temp_file.name, CONTACTS_FILE)
                return True, "Contact deleted successfully"
            else:
                os.remove(temp_file.name)
                return False, "Contact not found"
            
        except Exception as e:
            return False, f"Error: {str(e)}"



