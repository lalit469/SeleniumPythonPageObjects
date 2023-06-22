import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest

from Utilities import configReader


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request,get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)

@pytest.fixture(params=["chrome","firefox"],scope="function")
def get_browser(request):

    global driver
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=chrome_options)

    if request.param == "firefox":
        driver = webdriver.Firefox()
    request.cls.driver=driver


    driver.get(configReader.configRead("basic info", "testsiteurl"))
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()