from loguru import logger

from src.main.models.labour import labour
class MistriService:
    def __init__(self,db_connection):
        self.db_connection=db_connection
        
    def create_mistri(self,mistri):
        cursor=self.db_connection.cursor()
        check_query=f"""SELECT id FROM skills where labour_id=%s"""
        check_values=(mistri.id,)
        cursor.execute(check_query,check_values)
        result=cursor.fetchall()
        logger.info(f"Data from skills table {result}")
        if result:
            logger.info(f"Labour already exists with ID: {result[0][0]}")
            return result[0][0]

        query="""INSERT INTO skills (labour_id, skill) VALUES (%s, %s)"""
        values=(mistri.id, mistri.skill)  
        cursor.execute(query,values)
        self.db_connection.commit()