from pages.LoginPage import Login1
import pytest


# Launch the browser and navinagting to the url and the enter the login credentials
@pytest.mark.usefixtures("test_setup")
class Testloginforfitst:
    def test_loginact(self):
        driver=self.driver
        time=Login1(driver)
        time.logintime()




#logging out from the home page
# def test_logout():
#     driver.implicitly_wait(20)
#     driver.find_element_by_xpath("//a[text()='Logout']").click()












