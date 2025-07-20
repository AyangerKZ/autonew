from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://books.toscrape.com/')


    def clickk(self):
        iphone = self.driver.find_element(By.XPATH, '//a[text()="Tipping the Velvet"]')
        iphone.click()

    def clickk_product(self):
        historical = self.driver.find_element(By.XPATH, '(//a[contains(text(), "Historical")])[2]')
        historical.click()


