from src.main.models.labour import labour
from src.main.models.mistri import mistri
# from src.main.models.homebuyer import HomeBuyer

#it is a concept of  factory design pattern to create person objects.Simply we are creating the object based on the type of person requested.
class PersonFactory:
    @staticmethod
    def create_person(person_type, **kwargs):
        if person_type.lower() == "labour":
            return labour(kwargs["first_name"], kwargs["last_name"], kwargs["wage"], kwargs["role"])
        elif person_type.lower() == "mistri":
            return mistri(kwargs["first_name"], kwargs["last_name"], kwargs["wage"], kwargs["role"], kwargs["skill"])
        # elif person_type.lower() == "homebuyer":
        #     return HomeBuyer(kwargs["first_name"], kwargs["last_name"], kwargs["budget"], kwargs["location"])
        else:
            raise ValueError(f"Invalid person type: {person_type}")