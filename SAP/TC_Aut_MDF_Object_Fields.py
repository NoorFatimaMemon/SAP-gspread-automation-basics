from login import login_instance
from Controller_MDF_Object_Fields import Controller_MDF_Object_Fields
import gspread
import time

gc = gspread.service_account()
sheet = gc.open("Gspread")
Worksheet = sheet.worksheet("Fields COD")


class TC_Automation_MDF_Object:
    login_instance.login_method()
    driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
    hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance
    Controller = Controller_MDF_Object_Fields()
    data_record, processing_heading = Controller.Load_Data(gspread_Sheet=Worksheet)

    def ExecuteProcess(self):
        link_1 = self.driver.current_url
        link_1_split = link_1.split('s.crb=')
        link_2 = "https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=2K8CkVQJqWwL%2brEcUnCDHjVd%2fb%2fqqmVKOrsyYQk9p7E%3d"
        link_2_split = link_2.split("s.crb=")
        time.sleep(2)
        COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1]
        time.sleep(2)
        self.driver.get(COD_Link)
        time.sleep(2)

        self.hw.ClickElement('//span[@id="19__write_toggle"]', 'xpath')  # to click no search dropdown
        time.sleep(1)
        self.hw.ClickElement('//a[@title="Object Definition"]', 'xpath')  # to click object definition
        time.sleep(1)

        for MDF_obj in self.processing_heading:
            self.ProcessObject(MDF_obj)

    def ProcessObject(self, MDF_Object):
        link_1 = self.driver.current_url
        link_1_split = link_1.split('s.crb=')
        link_2 = f"https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=J74wSY%2fbBYLLOtmmiPHIU28YdKC%2bPsiT3awOLDacaPE%3d#c=1&t=GOObjectDefinition&i={MDF_Object}"
        link_2_split = link_2.split("s.crb=")
        time.sleep(2)
        COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1] + f"&t=GOObjectDefinition&i={MDF_Object}"
        self.driver.get(COD_Link)
        time.sleep(2)

        self.hw.ClickElement(
            '//div[@class="viewPanelContainer"]//div[@class="ectFCTitle"]//button[@title="Take Action"]', 'xpath')
        time.sleep(5)
        self.hw.ClickElement('//div[@class="sfDropMenu"]//a[@title="Make Correction"]', 'xpath')
        time.sleep(3)

        for data in [a for a in self.data_record if MDF_Object == a.Code]:
            details_xpath = f'//table[@aria-label="Fields"]//tr//td[contains(@id,"0")]//parent::span//input[@value="{data.Name}"]//ancestor::tr[contains(@id,"row")]//td//a[contains(@class,"writeComp")]'
            time.sleep(1)
            input_box = '//div[@role="dialog"]//div[contains(@class,"writeMode")]//table[@role="none"]//tr[.//label[text()="{0}"]]//td[contains(@class,"field_value")]//input'
            dropdown_icon = '//div[@role="dialog"]//div[contains(@class,"writeMode")]//table[@role="none"]//tr[.//label[text()="{0}"]]//span[contains(@id, "write_toggle")]'
            desired_value = "//div[contains(@class,'globalContentBackground')]//ul//li[@role='option']//a[@title='{0}']"
            new_field = '//table[@aria-label="Fields"]//tr//td[contains(@id,"0")]//parent::span//input[@value="cust_"]'

            if not self.hw.isElementPresent(details_xpath, 'xpath'):
                self.hw.SendKeys(new_field,  'xpath', f'{data.Name}')
                self.hw.ClickElement('//h1[@class="globalPageTitle"]', 'xpath')
                new_field_details_xpath = f'//table[@aria-label="Fields"]//tr//td[contains(@id,"0")]//parent::span//input[@value="cust_{data.Name}"]//ancestor::tr[contains(@id,"row")]//td//a[contains(@class,"writeComp")]'
                self.hw.ClickElement(new_field_details_xpath, "xpath")
                time.sleep(2)

            else:
                self.hw.ClickElement(details_xpath, "xpath")
                time.sleep(2)

            self.hw.FillField(input_box.format("Maximum Length"), 'xpath', 'value', f'{data.Maximum_Length}')

            self.hw.Check_and_Select_Dynamic_Dropdown(input_box.format("Data Type"),
                                                      desired_value.format(data.Data_Type),
                                                      data.Data_Type)

            self.hw.FillField(input_box.format("Valid Values Source"), 'xpath', 'value', f'{data.Valid_Values_Source}')

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("Hide Old Value"),
                                                     dropdown_icon.format("Hide Old Value"),
                                                     desired_value.format(data.Hide_Old_Value),
                                                     data.Hide_Old_Value)

            self.hw.FillField(input_box.format("Decimal Precision"), 'xpath', 'value', f'{data.Decimal_Precision}')

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("Include Inactive Users"),
                                                     dropdown_icon.format("Include Inactive Users"),
                                                     desired_value.format(data.Include_Inactive_Users),
                                                     data.Include_Inactive_Users)

            self.hw.FillField(input_box.format("UI Field Renderer"), 'xpath', 'value', f'{data.UI_Field_Renderer}')

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("Transient"),
                                                     dropdown_icon.format("Transient"),
                                                     desired_value.format(data.Transient),
                                                     data.Transient)

            self.hw.FillField(input_box.format("Help Text"), 'xpath', 'value', f'{data.Help_Text}')

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("Mask Value on UI"),
                                                     dropdown_icon.format("Mask Value on UI"),
                                                     desired_value.format(data.Mask_Value_on_UI),
                                                     data.Mask_Value_on_UI)

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("Show Trailing Zeros"),
                                                     dropdown_icon.format("Show Trailing Zeros"),
                                                     desired_value.format(data.Show_Trailing_Zeros),
                                                     data.Show_Trailing_Zeros)

            self.hw.FillField(input_box.format("Default Value"), 'xpath', 'value', f'{data.Default_Value}')

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("Hide Seconds"),
                                                     dropdown_icon.format("Hide Seconds"),
                                                     desired_value.format(data.Hide_Seconds),
                                                     data.Hide_Seconds)

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("Required"),
                                                     dropdown_icon.format("Required"),
                                                     desired_value.format(data.Required),
                                                     data.Required)

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("Visibility"),
                                                     dropdown_icon.format("Visibility"),
                                                     desired_value.format(data.Visibility),
                                                     data.Visibility)

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("Status"),
                                                     dropdown_icon.format("Status"),
                                                     desired_value.format(data.Status),
                                                     data.Status)

            self.hw.FillField(input_box.format("Label"), 'xpath', 'value', f'{data.Label}')

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("Cascade"),
                                                     dropdown_icon.format("Cascade"),
                                                     desired_value.format(data.Cascade),
                                                     data.Cascade)

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("End Of Period"),
                                                     dropdown_icon.format("End Of Period"),
                                                     desired_value.format(data.End_Of_Period),
                                                     data.End_Of_Period)

            self.hw.ClickElement('//button[@title="Done"]', 'xpath')

        self.hw.ClickElement('//button[@title="Save"]', 'xpath')
        time.sleep(5)
        self.hw.Popup("//div[@role='dialog']", 'xpath')
        Cancel = self.hw.GetElement('//button[@title="Cancel"]', 'xpath')
        time.sleep(1)
        if Cancel.is_enabled():
            self.hw.ClickElement('//button[@title="Cancel"]', 'xpath')
            self.hw.ClickElement('//button[@title="Don’t Save"]', 'xpath')


MDF_Object_class = TC_Automation_MDF_Object()
MDF_Object_class.ExecuteProcess()
