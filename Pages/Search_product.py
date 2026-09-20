from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class Searchproduct:
    SEARCHINPUT=(By.NAME,"q")
    ITEMNAME=(By.XPATH,"//div[contains(text(),'LG 185 L') and contains(text(),'Single Door')]")
    ADDCART=(By.XPATH,"//*[name()='svg']//ancestor::button[1]")
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    def entersearchinput(self,searchinput):
        self.wait.until(EC.visibility_of_element_located(self.SEARCHINPUT)).send_keys(searchinput)
    def searchitem(self):
        element= self.wait.until(EC.element_to_be_clickable(self.ITEMNAME))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",element)
        return element
    def AddCart(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        ele=self.wait.until(EC.element_to_be_clickable(self.ADDCART))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});",ele)
        self.driver.switch_to.window(self.driver.window_handles[-1])