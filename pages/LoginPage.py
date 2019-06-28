from pages.Webgeneric import Webgeneric

class Login1(Webgeneric):
    def __init__(self,driver):
        Webgeneric.__init__(self,driver)
        self.un_id="username"
        self.pwd_name="pwd"
        self.login_btn_id="loginButton"
        self.wg=Webgeneric(self.driver)

        # self.driver=driver

    def logintime(self):
        self.wg.enter(self.un_id,"shivanpuneeth50@gmail.com")
        # self.driver.find_element_by_id("username").send_keys("shivanpuneeth50@gmail.com")
        self.wg.enter(self.pwd_name,"manjushivu@1991")
        # self.driver.find_element_by_name("pwd").send_keys("manjushivu@1991")
        self.wg.submit(self.login_btn_id)
        # self.driver.find_element_by_id("loginButton").click()


