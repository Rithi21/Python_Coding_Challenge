import configparser
import os

class DBProperty:
    @staticmethod
    def get_property_string(file_name: str) -> dict:
        config = configparser.ConfigParser()
        file_path = os.path.join(os.getcwd(), file_name)
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Property file '{file_name}' not found in the current directory.")

        config.read(file_path)
        db_config = {
            "server": config["DEFAULT"]["server"],
            "database": config["DEFAULT"]["database"],
            "username": config["DEFAULT"]["username"],
            "password": config["DEFAULT"]["password"]
        }
        return db_config
