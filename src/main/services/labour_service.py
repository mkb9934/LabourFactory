from loguru import logger
class LabourService:
    def __init__(self,db_connection):
        self.db_connection=db_connection
        
    def create_labour(self,labour):
        cursor=self.db_connection.cursor()
        check_query=f"""SELECT id FROM labours WHERE lower(first_name)=%s AND lower(last_name)=%s"""
        check_values=(labour.first_name.lower(),labour.last_name.lower())
        cursor.execute(check_query,check_values)
        result=cursor.fetchall()
        logger.info(f"Data from labours table {result}")
        if result:
            logger.info(f"Labour already exists with ID: {result[0][0]}")
            return result[0][0]
        
        query="""INSERT INTO labours (first_name, last_name, wage, role,email) VALUES (%s, %s, %s, %s, %s)"""
        values=(labour.first_name,labour.last_name,labour.wage,labour.role,labour.email)  
        cursor.execute(query,values)
        self.db_connection.commit()
        