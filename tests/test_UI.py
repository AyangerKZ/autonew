from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from pages.product import ProductPage
from pages.homepage import HomePage


def test_open_chrome(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.clickk()
    product_page = ProductPage(driver)
    product_page.check_title('Tipping the Velvet')
   # driver.get('https://books.toscrape.com/')
   # iphone = driver.find_element(By.XPATH, '//a[text()="Tipping the Velvet"]')
   # iphone.click()
   # title = driver.find_element(By.CSS_SELECTOR, 'h1')
    #assert title.text == 'Tipping the Velvet'


def test_check_books(driver):

    homepage = HomePage(driver)
    homepage.open()
    homepage.clickk_product()
    product_page = ProductPage(driver)  # Создаем экземпляр ProductPage
    product_page.check_product_title(2)
    #driver.get('https://books.toscrape.com/')
   # historical = driver.find_element(By.XPATH, '(//a[contains(text(), "Historical")])[2]')
    #historical.click()
    #time.sleep(2)
    #elss = driver.find_elements(By.CSS_SELECTOR, ".image_container")
    #assert len(elss) == 2


