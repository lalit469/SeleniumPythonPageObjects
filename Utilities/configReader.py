"""
this file will read the info from config.ini file

"""

from configparser import ConfigParser
#
# config=ConfigParser()
# config.read("config.ini")
# print(config.get("locator","username"))
# print(config.get("basic info","browser"))


def configRead(section,key):

    config = ConfigParser()
    config.read("..//ConfigurationData/config.ini")
    return config.get(section,key)

# read=configRead("locators","name_CSS")
# print(read)


