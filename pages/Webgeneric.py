from pages.Locatorgeneric import Locatorgeneric

class Webgeneric(Locatorgeneric):
    def __init__(self,driver):
        Locatorgeneric. __init__(self,driver)

    def enter(self,locator_type,locator_val,input_val):
        self.driver.find_element_by_id("username").send_keys("shivanpuneeth50@gmail.com")
        var=self.locator(locator_type,locator_val)
        var.send_keys(input_val)

    def enter(self,locator,input_val):
         self.driver.find_element_by_name("pwd").send_keys("manjushivu@1991")


    def submit(self,locator):
        self.driver.find_element_by_id("loginButton").click()



