import configparser

config=configparser.RawConfigParser()
config.read("..\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('basic_info','baseURL')
        return url
    @staticmethod
    def getUsername():
        username=config.get('basic_info','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('basic_info','password')
        return password
