import time

import pytest

from Pages.CarBase import CarBase
from Pages.HomePage import HomePage
from TestCases.baseTest import baseTest
from Utilities import dataProvider

import logging
from Utilities.LogUtil import Logger

# current filename in python -> __name__
log = Logger(__name__, logging.INFO)


class Test_Carwale(baseTest):

    @pytest.mark.skip
    def test_gotoNewCar(self):
        log.logger.info("************Inside new car test*******")
        home = HomePage(self.driver)
        home.gotoNewCars()

    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand,carTitle", dataProvider.get_data("NewCarsTest"))
    def test_selectCars(self, carBrand, carTitle):
        log.logger.info("Inside select cars test")
        home = HomePage(self.driver)
        car = CarBase(self.driver)
        """ ******the page object model -> whichever method is responsible to take you on next page should
        return the object of that page (mthod/function chaining)
        ***Single column in excel sheet will take value in form of list [BMW], when 2 column take string BMW"""
        if carBrand == "BMW":
            home.gotoNewCars().selectBMW()
        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
        title = car.getCarTitle()
        print("car title is: ", title)
        assert title== carTitle, "Not on the correct page"
        time.sleep(3)

    @pytest.mark.parametrize("carBrand,carTitle", dataProvider.get_data("NewCarsTest"))
    def test_carNamesandPrices(self, carBrand, carTitle):
        log.logger.info("Inside car names and prices test")
        home = HomePage(self.driver)
        car = CarBase(self.driver)
        """ ******the page object model -> whichever method is responsible to take you on next page should
        return the object of that page (mthod/function chaining)
        ***Single column in excel sheet will take value in form of list [BMW], when 2 column take string BMW"""
        if carBrand == "BMW":
            home.gotoNewCars().selectBMW()
        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
        title = car.getCarTitle()
        print("car title is: ", title)
        assert title == carTitle, "Not on the correct page"
        car.getCarNameandPrices()
        time.sleep(3)