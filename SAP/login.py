from selenium import webdriver
from HandyWrappers import HandyWrappers
import time


class login:
    sourcelink = 'https://pmsalesdemo8.successfactors.com/sf/start/#/companyEntry'
    driver = webdriver.Chrome()
    hw = HandyWrappers(driver)  # Initialize HandyWrappers instance
    driver.get(sourcelink)

    def login_method(self):
        self.hw.ClickElement('//input[@id="__input0-inner"]', 'xpath')
        time.sleep(1)
        self.hw.SendKeys('//input[@placeholder="Enter Company ID"]', 'xpath', 'SFPART065417')   # to enter company id
        time.sleep(1)
        self.hw.ClickElement('//button[@id="__button0"]', 'xpath')
        time.sleep(1)
        self.hw.SendKeys('//input[@placeholder="Username"]', 'xpath', 'codebotintern')  # to enter username
        time.sleep(1)
        self.hw.SendKeys('//input[@placeholder="Enter Password"]', 'xpath', 'partBos@DC8@@')     # to enter password
        time.sleep(1)
        self.hw.ClickElement('//*[@id="__button2-inner"]', 'xpath')
        time.sleep(1)
        popup = self.hw.GetElement("//div[@role='dialog']", 'xpath')
        if popup is not None:
            self.hw.ClickElement('//button[@title="Accept"]', 'xpath')
            time.sleep(2)


login_instance = login()
