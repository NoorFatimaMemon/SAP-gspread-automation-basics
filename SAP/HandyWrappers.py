import time
from selenium.webdriver.common.by import By


class HandyWrappers:

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, LocatorType):
        LocatorType = LocatorType.lower()
        if LocatorType == 'id':
            return By.ID
        elif LocatorType == 'name':
            return By.NAME
        elif LocatorType == 'xpath':
            return By.XPATH
        elif LocatorType == 'classname':
            return By.CLASS_NAME
        elif LocatorType == 'css':
            return By.CSS_SELECTOR
        elif LocatorType == 'linktext':
            return By.LINK_TEXT
        elif LocatorType == 'tagname':
            return By.TAG_NAME
        else:
            print("Locator Type" + LocatorType + "not Correct or Supported")
        return False

    def GetElement(self, Locator, LocatorType='id'):
        element = None
        try:
            LocatorType = LocatorType.lower()
            ByType = self.getByType(LocatorType)
            element = self.driver.find_element(ByType, Locator)
            return element
        except:
            return element

    def GetElements(self, Locator, LocatorType='id'):
        Elements = []
        try:
            LocatorType = LocatorType.lower()
            ByType = self.getByType(LocatorType)
            Elements = self.driver.find_elements(ByType, Locator)
            if Elements not in [None, False]:
                print("Elements found")
            else:
                print("Elements list empty!")
        except:
            print("Elements Error!")
        return Elements

    def ClickElement(self, Locator, LocatorType='id'):
        try:
            Get_Element = self.GetElement(Locator, LocatorType)
            if Get_Element is not None or False:
                Get_Element.click()
                print('Element Clicked')
            else:
                pass
        except:
            pass

    def SendKeys(self, Locator, LocatorType='id', keys=""):
        try:
            Get_Element = self.GetElement(Locator, LocatorType)
            if Get_Element is not None or False:
                Get_Element.send_keys(keys)
            else:
                pass
        except:
            print("Element Error")

    def FillField_2(self, Locator, LocatorType='id', keys=""):
        try:
            attribute = self.GetElementAttribute(Locator, LocatorType, attribute='value')
            if attribute != keys:
                element = self.GetElement(Locator, LocatorType)
                element.clear()
                element.send_keys(keys)
            else:
                pass
        except:
            print("Element Error")

    def FillField(self, Locator, LocatorType='id', attribute='value', keys=""):
        try:
            attribute_value = self.GetElementAttribute(Locator, LocatorType, attribute)
            if attribute_value != keys:
                element = self.GetElement(Locator, LocatorType)
                element.clear()
                element.send_keys(keys)
            else:
                pass
        except:
            print("Element Error")

    def GetElementText(self, Locator, LocatorType='id'):
        Element_text = ''
        try:
            Get_Element = self.GetElement(Locator, LocatorType)
            if Get_Element is not None or False:
                Element_text = Get_Element.text
                print('Element Text: ' + Element_text)
            else:
                print("Element does not have any text")
        except:
            print('Element Error!')
        return Element_text

    def GetElementlistofText(self, Locator, LocatorType='id'):
        list_of_Text = []
        try:
            ElementlistofText = self.GetElements(Locator, LocatorType)
            for elements in ElementlistofText:
                if elements not in [None, False]:
                    text_elements = elements.text
                    list_of_Text.append(text_elements)
                else:
                    print("Element list not exist!")
            print(list_of_Text)
        except:
            print('Element error!')
        return list_of_Text

    def GetElementAttribute(self, Locator, LocatorType='id', attribute='class'):
        attribute_value = None
        try:
            Element = self.GetElement(Locator, LocatorType)
            if Element not in [None, False]:
                attribute_value = Element.get_attribute(attribute)
                print("Value of attribute is: " + attribute_value)
            else:
                print("Value of attribute does not exist")
        except:
            print('Value of attribute has error')
        return attribute_value

    def GetElementlistofattribute(self, Locator, LocatorType='id', attribute='class'):
        list_of_attribute = []
        try:
            elements = self.GetElements(Locator, LocatorType)
            for element in elements:
                if element not in [None, False]:
                    attribute_value = element.get_attribute(attribute)
                    list_of_attribute.append(attribute_value)
                else:
                    print('list of attribute value is empty')
            print(list_of_attribute)
        except:
            print('list of attribute value error')
        return list_of_attribute

    def isElementPresent(self, Locator, LocatorType='id'):
        try:
            element = self.GetElement(Locator, LocatorType)
            if element is not None:
                return True
            else:
                return False
        except:
            return False

    def ElementPresenceCheck(self, Locator, ByType):
        try:
            ElementList = self.driver.find_elements(ByType, Locator)
            if len(ElementList) > 0:
                print('Element is Present')
                return True
            else:
                print('Element Not Present')
                return False
        except:
            print('Element Not Present')
            return False

    def Popup(self, Locator, LocatorType='xpath'):
        popup_element = self.isElementPresent(Locator, LocatorType)
        time.sleep(1)

        if popup_element is True:
            self.GetElementText('//span[@class="important-focus-msg"]', 'xpath')
            yes_element = self.GetElement('//button[@title="Yes"]', 'xpath')
            time.sleep(1)

            if yes_element is None:
                return self.ClickElement('//button[@title="OK"]', 'xpath')
            else:
                return self.ClickElement('//button[@title="Yes"]', 'xpath')
        else:
            pass
        time.sleep(1)

    def Check_and_Select_Static_Dropdown(self, input_box, dropdown_icon, desired_value_xpath, desired_value):
        attribute_value = self.GetElementAttribute(input_box, 'xpath', 'value')
        time.sleep(1)
        if attribute_value != desired_value:
            self.ClickElement(dropdown_icon, 'xpath')
            time.sleep(1)
            if not self.isElementPresent(desired_value_xpath, 'xpath'):
                print("Drop-down value not found")
            else:
                self.ClickElement(desired_value_xpath, 'xpath')
                time.sleep(1)
        else:
            pass

        self.Popup("//div[@role='dialog']", 'xpath')

    def Check_and_Select_Dynamic_Dropdown(self, input_box, desired_value_xpath, desired_value):
        attribute_value = self.GetElementAttribute(input_box, 'xpath', 'value')
        if attribute_value != desired_value:
            self.ClickElement(input_box, 'xpath')
            time.sleep(1)
            if desired_value == '':
                Element = self.GetElement(input_box, 'xpath')
                Element.clear()
                time.sleep(1)
                self.ClickElement('//h1[@class="globalPageTitle"]', 'xpath')
            else:
                self.SendKeys(input_box, 'xpath', f'{desired_value.split("(")[0]}')
                time.sleep(2)
                if not self.isElementPresent(desired_value_xpath, 'xpath'):
                    print("Drop-down value not found")
                else:
                    self.ClickElement(desired_value_xpath, 'xpath')
        else:
            pass

    def CheckBox(self, checkboxpath, desiredvalue):
        attribute_value = self.GetElementAttribute(checkboxpath, 'xpath', 'checked')
        time.sleep(5)
        if attribute_value == desiredvalue or attribute_value is None and desiredvalue == '':
            pass
        else:
            self.ClickElement(checkboxpath, 'xpath')
