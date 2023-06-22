from Pages.BasePage import BasePage

class RegistrationPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)



    def fillform(self,name,phone,email,country,city,username,password):
       self.type("name_CSS",name)
       self.type("phone_CSS",phone)
       self.type("email_XPATH", email)
       self.select("country_XPATH",country)
       self.type("city_XPATH",city)
       self.type("username_XPATH",username)
       self.type("password_XPATH",password)
       self.click("submit_XPATH")

