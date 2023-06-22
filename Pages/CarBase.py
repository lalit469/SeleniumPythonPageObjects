"""it will contain the common functionality
used in other modules
"""
from selenium.webdriver.common.by import By

from Utilities import configReader


class CarBase():

    def __init__(self, driver):
        self.driver=driver

    def getCarTitle(self):
        return self.driver.find_element(By.XPATH, configReader.configRead("locators", "carTitle_XPATH")).text

    def getCarNameandPrices(self):
        carNames= self.driver.find_elements(By.XPATH, configReader.configRead("locators", "carNames_XPATH"))
        carPrices= self.driver.find_elements(By.XPATH, configReader.configRead("locators", "carPrices_XPATH"))


        for i in range(1,len(carPrices)):
            print(carNames[i].text+"----Prices are---"+carPrices[i].text)