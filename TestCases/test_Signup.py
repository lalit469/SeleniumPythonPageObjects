import pytest
from Pages.RegisterationPage import RegistrationPage
from TestCases.baseTest import baseTest
from Utilities import dataProvider

import logging
from Utilities.LogUtil import Logger

#current filename in python -> __name__
log=Logger(__name__,logging.INFO)


class Test_SignUp(baseTest):

    @pytest.mark.parametrize("name,phone,email,country,city,username,password", dataProvider.get_data("LoginTest"))
    def test_doSignUp(self,name,phone,email,country,city,username,password):
        log.logger.info("Test do signup started")
        regPage=RegistrationPage(self.driver)
        regPage.fillform(name,phone,email,country,city,username,password)
        log.logger.info("Test do signup successfully executed")

   # assert 1 == 2
# allure.attach(driver.get_screenshot_as_png(),name="dologin",attachment_type=AttachmentType.PNG)
