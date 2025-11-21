class Employee:
    def __init__(self,first_name, last_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.email = f"{first_name.lower()}.{last_name.lower()}@taitotalo.fi"
    def get_email(self):
        return self.email
    def set_email(self,new_email):
        self.email = new_email
    def print_email(self):
        print(self.email)
        
bob = Employee('Bob','Edwards')
bob.print_email()