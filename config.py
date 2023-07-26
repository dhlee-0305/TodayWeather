import configparser as parser

def loadConfig():
    config = parser.ConfigParser()
    config.read('.\\config.ini', encoding="UTF-8")

    return config