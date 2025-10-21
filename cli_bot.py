from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass
           
class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be exactly 10 digits.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
         phone = Phone(phone_number)
         self.phones.append(phone)
    
    def remove_phone(self, phone_number):
        for p in self.phones[:]:
            if p.value == phone_number:
                self.phones.remove(p)
                return "Phone removed successfully."
        raise ValueError(f"Phone number '{phone_number}' not found in contact.")
    
    def find_phone(self, phone_number):
        for p in self.phones[:]:
            if p.value == phone_number:
                return p
        raise ValueError(f"Phone number '{phone_number}' not found in contact.")
    
    def edit_phone(self, old_number, new_number):
        found_phone_object = self.find_phone(old_number)
        p = Phone(new_number) #validation of new number
        found_phone_object.value = new_number
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        user_name = record.name.value
        self.data[user_name] = record

    def find(self, name):
        return self.data[name]
    
    def delete(self, name):
        del self.data[name] #delete dictionary entry with given key       