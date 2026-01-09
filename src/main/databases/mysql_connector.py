from loguru import logger
import mysql.connector
import configparser


class MySqlConnection:
    _instance = None  #singleton instance
    
    def __init__(self,config):
        self.config=config
        if MySqlConnection._instance is not None:
            raise Exception("use get_instance() method instead of creating a new object.")
        self.config=config
        self.connection=None
        self.connect()
        
    @classmethod
    def get_instance(cls,config=None):
        if cls._instance is None:
            cls._instance = cls(config)
        return cls._instance    
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.config["mysql_database"]["host"].strip(),
                user=self.config["mysql_database"]["user"].strip(),
                password=self.config["mysql_database"]["password"].strip(),
                database=self.config["mysql_database"]["database"].strip()
            )
            logger.info("Connected to MySQL database successfully.")
        except Exception as e:
            logger.error(f"Failed to connect to MySQL: {e}")
            raise e
        
        def close(self):
            if self.connection is not None and self.connection.is_connected():
                self.connection.close()
                logger.info("MySQL connection closed.")
            
