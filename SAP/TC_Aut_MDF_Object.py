from login import login_instance
from Controller_MDF_Object import Controller_MDF_Object
import gspread
import time

gc = gspread.service_account()
sheet = gc.open("Gspread")
Worksheet = sheet.worksheet("Configure Object Definitions")


class TC_Automation_MDF_Object:
    login_instance.login_method()
    driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
    hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance
    Controller = Controller_MDF_Object()
    data_record, processing_heading = Controller.LoadData(gspread_Sheet=Worksheet)

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
        for data in [a for a in self.data_record if MDF_Object == a.Title]:
            link_1 = self.driver.current_url
            link_1_split = link_1.split('s.crb=')
            link_2 = f"https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=J74wSY%2fbBYLLOtmmiPHIU28YdKC%2bPsiT3awOLDacaPE%3d#c=1&t=GOObjectDefinition&i={data.Code}"
            link_2_split = link_2.split("s.crb=")
            time.sleep(2)
            COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1] + f"&t=GOObjectDefinition&i={data.Code}"
            self.driver.get(COD_Link)
            time.sleep(2)

            self.hw.ClickElement(
                '//div[@class="viewPanelContainer"]//div[@class="ectFCTitle"]//button[@title="Take Action"]', 'xpath')
            time.sleep(5)
            self.hw.ClickElement('//div[@class="sfDropMenu"]//a[@title="Make Correction"]', 'xpath')
            time.sleep(3)

            input_box = "//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='{0}']]//td[contains(@class,'field_value')]//input"
            dropdown_icon = "//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='{0}']]//td[contains(@class,'field_value')]//span[contains(@id, 'write_toggle')]"
            desired_value = "//div[contains(@class,'globalContentBackground')]//ul//li[@role='option']//a[@title='{0}']"
            description_input_box = "//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='{0}']]//td[contains(@class,'field_value')]//textarea"
            security_input_box124 = "((//div[contains(@class,'MDFViewPanel')]//tr//div[@class='MDFRepeatingForm']//table)[2]//span[contains(@class,'writeComp')]//input[@aria-label='{0}']//ancestor::div)[25]//input"
            security_dropdown_icon = "((//div[contains(@class,'MDFViewPanel')]//tr//div[@class='MDFRepeatingForm']//table)[2]//span[contains(@class,'writeComp')]//input[@aria-label='{0}']//ancestor::div)[25]//span[contains(@id, 'write_toggle')]"
            security_input_box35 = "((//div[contains(@class,'MDFViewPanel')]//tr//div[@class='MDFRepeatingForm']//table)[2]//span[contains(@class,'writeComp')]//label[text()='{0}']//ancestor::div)[25]//input"

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("Effective Dating"),
                                                     dropdown_icon.format("Effective Dating"),
                                                     desired_value.format(data.Effective_Dating),
                                                     data.Effective_Dating)

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("API Visibility"),
                                                     dropdown_icon.format("API Visibility"),
                                                     desired_value.format(data.API_Visibility),
                                                     data.API_Visibility)

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("Status"),
                                                     dropdown_icon.format("Status"),
                                                     desired_value.format(data.Status),
                                                     data.Status)

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("MDF Version History"),
                                                     dropdown_icon.format("MDF Version History"),
                                                     desired_value.format(data.MDF_Version_History),
                                                     data.MDF_Version_History)

            self.hw.Check_and_Select_Dynamic_Dropdown(input_box.format("Default Screen"),
                                                      desired_value.format(data.Default_Screen),
                                                      data.Default_Screen)

            self.hw.FillField(input_box.format("Label"), 'xpath', 'value', f'{data.Label}')

            self.hw.FillField(description_input_box.format("Description"), 'xpath', 'innerText', f'{data.Description}')

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("API Sub Version"),
                                                     dropdown_icon.format("API Sub Version"),
                                                     desired_value.format(data.API_Sub_Version),
                                                     data.API_Sub_Version)

            self.hw.FillField(input_box.format("Subject User Field"), 'xpath', 'value',
                              f'{data.Subject_User_Field}')

            self.hw.Check_and_Select_Dynamic_Dropdown(input_box.format("Workflow Routing"),
                                                      desired_value.format(data.Workflow_Routing),
                                                      data.Workflow_Routing)

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("Pending Data"),
                                                     dropdown_icon.format("Pending Data"),
                                                     desired_value.format(data.Pending_Data),
                                                     data.Pending_Data)

            self.hw.Check_and_Select_Static_Dropdown(input_box.format("Object Category"),
                                                     dropdown_icon.format("Object Category"),
                                                     desired_value.format(data.Object_Category),
                                                     data.Object_Category)

            self.hw.Check_and_Select_Static_Dropdown(security_input_box124.format("Secured"),
                                                     security_dropdown_icon.format("Secured"),
                                                     desired_value.format(data.Secured),
                                                     data.Secured)

            self.hw.Check_and_Select_Dynamic_Dropdown(security_input_box124.format("Permission Category"),
                                                      desired_value.format(data.Permission_Category),
                                                      data.Permission_Category)

            self.hw.FillField(security_input_box35.format("RBP Subject User Field"), 'xpath', 'value',
                              f'{data.RBP_Subject_User_Field}')

            self.hw.Check_and_Select_Static_Dropdown(security_input_box124.format("CREATE Respects Target Criteria"),
                                                     security_dropdown_icon.format("CREATE Respects Target Criteria"),
                                                     desired_value.format(data.CREATE_Respects_Target_Criteria),
                                                     data.CREATE_Respects_Target_Criteria)

            self.hw.FillField(security_input_box35.format("Base Date Field For Blocking"), 'xpath', 'value',
                              f'{data.Base_Date_Field_For_Blocking}')

            self.hw.ClickElement('//button[@title="Save"]', 'xpath')
            time.sleep(4)
            self.hw.Popup("//div[@role='dialog']", 'xpath')
            Cancel = self.hw.GetElement('//button[@title="Cancel"]', 'xpath')
            time.sleep(1)
            if Cancel.is_enabled():
                self.hw.ClickElement('//button[@title="Cancel"]', 'xpath')
                self.hw.ClickElement('//button[@title="Don’t Save"]', 'xpath')


MDF_Object_class = TC_Automation_MDF_Object()
MDF_Object_class.ExecuteProcess()
