import pymysql
import os
import configparser

class Connection:
    def __init__(self, config = None):
        if config == None:
            config = self.get_cfg()

        self.config = config
        self.connection = self.connect(self.config)


    def connect(config):
        return pymysql.connect(
            host=config.get("CONNECTION", "hostname"),
            user=config.get("CONNECTION", "username"),
            password=config.get("CONNECTION", "password"),
            port=int(config.get("CONNECTION", "port")),
            database=config.get("CONNECTION", "database"),
            cursorclass=pymysql.cursors.DictCursor,  # Use DictCursor for fetching results as dictionaries
        )
    
    def get_cfg(cfg):
        cfg = os.getenv("CRUD_APP_CONFIG_FILE", default=".cfg")
        config = configparser.ConfigParser()
        config.read(cfg)
        return config
    

    #METER TODOS LOS MÉTODOS DE INTERACT AQUÍ
    #FUNCIÓN INTERACT LO PUEDO PONER PRIVADO CON __