from src.main.models.mistri import mistri
from src.main.factories.person_factory import PersonFactory
from src.main.services.labour_service import LabourService
from src.main.services.attendance_service import AttendanceService
from src.main.databases.mysql_connector import MySqlConnection
from src.main.utility.lec25_encrypt_decrypt import decrypt
from loguru import logger

import configparser
config=configparser.ConfigParser()
config.read(r"C:\Users\mkb99\VSCODEPRACTICE\Assignments\src\resources\config_file.ini")
config.set("mysql_database","password",decrypt(config["mysql_database"]["password"]))

db=MySqlConnection.get_instance(config)

#function to create a new labour dynamically using factory design pattern
def create_labour(first_name,last_name,wage,role):
        labour_obj=PersonFactory.create_person("labour",first_name=first_name,last_name=last_name,wage=wage,role=role)
        logger.info(f"Labour created: {labour_obj.to_dict()}")
        labour_service=LabourService(db.connection)
        labour_id=labour_service.create_labour(labour_obj)
        return labour_id
    
#function handle login/logout of labour
def labour_login_logout(id=None,first_name=None,last_name=None):
    attendance_service=AttendanceService(db.connection)  
    attendance_service.login_logout(id, first_name, last_name)
    return "Attendance recorded successfully."


result = create_labour("manish", "kumar", 500, "helper")
logger.info(f"Labour added with Id {result}")
# print(login_logout(first_name="manish", last_name="kumar"))    
    