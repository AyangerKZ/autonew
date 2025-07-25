from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self,driver):
        self.driver = driver


    def check_title(self,title):
        page_title = self.driver.find_element(By.CSS_SELECTOR, 'h1')
        assert page_title.text == title


    def check_product_title(self,count):
        page_elss = self.driver.find_elements(By.CSS_SELECTOR, ".image_container")
        assert len(page_elss) == count

