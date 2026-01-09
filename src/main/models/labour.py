from src.main.models.person import person
from loguru import logger
class labour(person):
    #total_count=0   #class variable
    def __init__(self,first_name,last_name,wage,role):
        super().__init__(first_name,last_name)
        self.wage=wage  #private variable
        self.role=role
        #Labour.total_count +=1   #incrementing class variable
        
    def to_dict(self):
        data=super().to_dict()
        data.update({
            "wage": self.wage,
            "role": self.role,               
        })
        return data    