# To get data of configure object definitions dropdown values
from login import login_instance
import time
from pynput.keyboard import Key, Controller


class SAPCOD_Task1:
    login_instance.login_method()
    driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
    hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance

    def task_1(self):
        link_1 = self.driver.current_url
        link_1_split = link_1.split('s.crb=')
        link_2 = "https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=2K8CkVQJqWwL%2brEcUnCDHjVd%2fb%2fqqmVKOrsyYQk9p7E%3d"
        link_2_split = link_2.split("s.crb=")
        COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1]
        self.driver.get(COD_Link)
        time.sleep(5)

        self.hw.ClickElement('//span[@id="19__write_toggle"]', 'xpath')         # to click no search dropdown
        time.sleep(5)
        self.hw.ClickElement('//a[@title="Object Definition"]', 'xpath')         # to click object definition
        time.sleep(5)
        self.hw.ClickElement('//span[@id="9__write_toggle"]', 'xpath')         # to click no selection dropdown
        time.sleep(5)

        keyboard = Controller()

        while True:
            try:
                hidden_element = self.hw.GetElement('//a[@title="単身赴任情報"]', 'xpath')        # Last Element
                if hidden_element.is_displayed():
                    x = self.hw.GetElementlistofattribute('//div[@class="primary"]//a', 'xpath', 'title')
                    for i in x:
                        print(i)
                    break
            except:
                pass

            keyboard.press(Key.down)
            keyboard.release(Key.down)
            time.sleep(0.1)


test = SAPCOD_Task1()
test.task_1()
