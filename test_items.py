import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_fiend_add_basket_btn(browser):
    browser.get(link)
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket").is_displayed()
    time.sleep(10)









