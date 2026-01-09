class person:
    def __init__(self,fisrt_name,last_name):
        self.first_name=fisrt_name
        self.last_name=last_name
        self.email=self.first_name+"."+self.last_name+"@gmail.com"
        
    def print_details(self):
        return f"First Name: {self.first_name}, Last Name: {self.last_name} with gmail as {self.email}"
    
    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }