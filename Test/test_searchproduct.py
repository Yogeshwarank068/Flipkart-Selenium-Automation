from Pages.Search_product import Searchproduct
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
def test_searchvalid(driver):
    driver.get("https://www.flipkart.com")
    Search_product=Searchproduct(driver)
    Search_product.entersearchinput("fridge"+ Keys.ENTER)
    driver.get_screenshot_as_file("search.png")
    element=Search_product.searchitem()
    ActionChains(driver).double_click(element).perform()
    driver.get_screenshot_as_file("item.png")
    addcart=Search_product.AddCart()
    ActionChains(driver).click(addcart)
    driver.get_screenshot_as_file("Addcart.png")