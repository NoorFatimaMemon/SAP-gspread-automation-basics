from login import login_instance
from TC_Model_MDF_Object import Model_ObjectDefinition
from Controller_MDF_Object import Controller_MDF_Object
import gspread
import time

gc = gspread.service_account()
sheet = gc.open("Gspread")
Worksheet = sheet.worksheet("Configure Object Definitions")


class TC_Rev_MDF_Object:
    login_instance.login_method()
    driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
    hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance
    RowNumber = 1

    def Executeprocess(self):
        link_1 = self.driver.current_url
        link_1_split = link_1.split('s.crb=')
        link_2 = "https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=2K8CkVQJqWwL%2brEcUnCDHjVd%2fb%2fqqmVKOrsyYQk9p7E%3d"
        link_2_split = link_2.split("s.crb=")
        COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1]
        self.driver.get(COD_Link)
        time.sleep(3)

        self.hw.ClickElement('//span[@id="19__write_toggle"]', 'xpath')  # to click no search dropdown
        time.sleep(1)
        self.hw.ClickElement('//a[@title="Object Definition"]', 'xpath')  # to click object definition
        time.sleep(1)

        _obj_Srch_Field = "//table[@class='MDFSearchBar']//tr//td[contains(text(),'Search')]/following-sibling::td[1]/span[3]//input"
        searchBox_id = str(self.hw.GetElementAttribute(_obj_Srch_Field, 'xpath', 'id')).split("__")[0] + "_"
        self.driver.execute_script(
            "ECTUtil.getComponentById('" + searchBox_id + "')._model._searchFields.pageSize = 2000")
        objects_list_dict = self.driver.execute_script(
            "return ECTUtil.getComponentById('" + searchBox_id + "')._model._searchDAO._staticData.results;")

        objects_list = [obj['code'] for obj in objects_list_dict]
        for MDF_obj in objects_list[:20]:
            self.ProcessObject(MDF_obj)

    def ProcessObject(self, MDF_Object):
        link_1 = self.driver.current_url
        link_1_split = link_1.split('s.crb=')
        link_2 = f"https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=J74wSY%2fbBYLLOtmmiPHIU28YdKC%2bPsiT3awOLDacaPE%3d#c=1&t=GOObjectDefinition&i={MDF_Object}"
        link_2_split = link_2.split("s.crb=")
        COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1] + f"&t=GOObjectDefinition&i={MDF_Object}"
        self.driver.get(COD_Link)
        time.sleep(2)

        obj_list = []
        self.RowNumber = self.RowNumber + 1

        obj = Model_ObjectDefinition()
        obj.item_id = self.RowNumber - 1
        title_pt1 = self.hw.GetElementText(
            "//div[@class='viewPanelContainer']//div//span[@class='pwhHeaderTitle globalHumanistText']", 'xpath').split("(")
        title = title_pt1[0].split(':')
        obj.Title = title[1].strip()

        text_xpath = "(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='{0}']]//td[contains(@class,'field_value')]//span[contains(@class,'read')])[1]"
        Description_text_xpath = "(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='{0}']]//td[contains(@class,'field_value')]//div[contains(@class,'read')])[1]"
        Security_xpath_1 = "((//div[contains(@class,'MDFViewPanel')]//tr//div[@class='MDFRepeatingForm']//table)[2]//span[contains(@class,'writeComp')]//input[@aria-label='{0}']//ancestor::div)[25]//span[@class='readonly readComp ectFieldshow']"
        Security_xpath_2 = "((//div[contains(@class,'MDFViewPanel')]//tr//div[@class='MDFRepeatingForm']//table)[2]//span[contains(@class,'writeComp')]//label[text()='{0}']//ancestor::div)[25]//span[@class='readonly readComp ectFieldshow']"

        obj.Code = self.hw.GetElementText(text_xpath.format("Code"), 'xpath')
        obj.Effective_Dating = self.hw.GetElementText(text_xpath.format("Effective Dating"), 'xpath')
        obj.API_Visibility = self.hw.GetElementText(text_xpath.format("API Visibility"), 'xpath')
        obj.Status = self.hw.GetElementText(text_xpath.format("Status"), 'xpath')
        obj.MDF_Version_History = self.hw.GetElementText(text_xpath.format("MDF Version History"), 'xpath')
        obj.Default_Screen = self.hw.GetElementText(text_xpath.format("Default Screen"), 'xpath')
        obj.Label = self.hw.GetElementText(text_xpath.format("Label"), 'xpath')
        obj.Description = self.hw.GetElementText(Description_text_xpath.format("Description"), 'xpath')
        obj.API_Sub_Version = self.hw.GetElementText(text_xpath.format("API Sub Version"), 'xpath')
        obj.Subject_User_Field = self.hw.GetElementText(text_xpath.format("Subject User Field	"), 'xpath')
        obj.Workflow_Routing = self.hw.GetElementText(text_xpath.format("Workflow Routing"), 'xpath')
        obj.Pending_Data = self.hw.GetElementText(text_xpath.format("Pending Data"), 'xpath')
        obj.Todo_Category = self.hw.GetElementText(text_xpath.format("Todo Category"), 'xpath')
        obj.Object_Category = self.hw.GetElementText(text_xpath.format("Object Category"), 'xpath')
        obj.Secured = self.hw.GetElementText(Security_xpath_1.format("Secured"), 'xpath')
        obj.Permission_Category = self.hw.GetElementText(Security_xpath_1.format("Permission Category"), 'xpath')
        obj.RBP_Subject_User_Field = self.hw.GetElementText(Security_xpath_2.format("RBP Subject User Field"), 'xpath')
        obj.CREATE_Respects_Target_Criteria = self.hw.GetElementText(Security_xpath_1.format("CREATE Respects Target Criteria"), 'xpath')
        obj.Base_Date_Field_For_Blocking = self.hw.GetElementText(Security_xpath_2.format("Base Date Field For Blocking"), 'xpath')
        obj_list.append(obj)

        Controller = Controller_MDF_Object()
        Controller.Fill_Worksheet(gspread_Sheet=Worksheet, Model_array_List=obj_list, RowNumber=self.RowNumber)


MDF_Object_class = TC_Rev_MDF_Object()
MDF_Object_class.Executeprocess()
