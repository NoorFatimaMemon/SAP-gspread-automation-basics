from login import login_instance
from TC_Model_MDF_Object_Fields import Model_ObjectDefinitionFields
from Controller_MDF_Object_Fields import Controller_MDF_Object_Fields
import gspread
import time

gc = gspread.service_account()
sheet = gc.open("Gspread")
Worksheet = sheet.worksheet("Fields COD")

login_instance.login_method()
driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance


def Get_MDF_Object_Record_List():
    hw.ClickElement('//span[@id="19__write_toggle"]', 'xpath')  # to click no search dropdown
    time.sleep(1)
    hw.ClickElement('//a[@title="Object Definition"]', 'xpath')  # to click object definition
    time.sleep(1)

    _obj_Srch_Field = "//table[@class='MDFSearchBar']//tr//td[contains(text(),'Search')]/following-sibling::td[1]/span[3]//input"
    searchBox_id = str(hw.GetElementAttribute(_obj_Srch_Field, 'xpath', 'id')).split("__")[0] + "_"
    driver.execute_script(
        "ECTUtil.getComponentById('" + searchBox_id + "')._model._searchFields.pageSize = 2000")
    objects_list_dict = driver.execute_script(
        "return ECTUtil.getComponentById('" + searchBox_id + "')._model._searchDAO._staticData.results;")

    return objects_list_dict


class TC_Rev_MDF_Object_Fields:
    RowNumber = 1
    UNI_RowNumber = 2

    def ExecuteProcess(self):
        link_1 = driver.current_url
        link_1_split = link_1.split('s.crb=')
        link_2 = "https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=2K8CkVQJqWwL%2brEcUnCDHjVd%2fb%2fqqmVKOrsyYQk9p7E%3d"
        link_2_split = link_2.split("s.crb=")
        COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1]
        driver.get(COD_Link)
        time.sleep(3)

        objects_list_dict = Get_MDF_Object_Record_List()
        objects_list = [obj['code'] for obj in objects_list_dict]
        for MDF_obj in objects_list[:10]:
            self.ProcessObject(MDF_obj)

    def ProcessObject(self, MDF_Object):
        link_1 = driver.current_url
        link_1_split = link_1.split('s.crb=')
        link_2 = f"https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=J74wSY%2fbBYLLOtmmiPHIU28YdKC%2bPsiT3awOLDacaPE%3d#c=1&t=GOObjectDefinition&i={MDF_Object}"
        link_2_split = link_2.split("s.crb=")
        COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1] + f"&t=GOObjectDefinition&i={MDF_Object}"
        driver.get(COD_Link)
        time.sleep(2)

        obj_list = []
        Code_value_xpath = "(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='{0}']]//td[contains(@class,'field_value')]//span[contains(@class,'read')])[1]"
        Name_xpath = '//table[@aria-label="Fields"]//td[contains(@id,"0")]//span[@class="writeComp ectFormFieldFocusMark textBox writeFieldUnchange"]//parent::span//span[@class="readonly readComp" and not(contains(@style, "text-align: inherit;")) and not(contains(text(), "cust_"))]'
        Names = hw.GetElementlistofText(Name_xpath, 'xpath')

        for Name in Names:
            obj = Model_ObjectDefinitionFields()
            self.RowNumber = self.RowNumber + 1
            obj.item_id = self.RowNumber - 1

            details_xpath = f'//table[@aria-label="Fields"]//td[contains(@id,"0")]//span[@class="writeComp ectFormFieldFocusMark textBox writeFieldUnchange"]//parent::span//span[text()="{Name}"]//ancestor::tr[contains(@id,"row")]//td//a[contains(@class,"readComp")]'
            hw.ClickElement(details_xpath, "xpath")
            time.sleep(1)
            details_dialogbox_textpath = '(//div[@role="dialog"]//div[contains(@class,"readMode")]//table[@role="none"]//tr[.//label[text()="{0}"]]//td[contains(@class,"field_value")]//span[contains(@class,"read")])[1]'

            obj.Code = hw.GetElementText(Code_value_xpath.format("Code"), 'xpath')
            obj.Name = hw.GetElementText(details_dialogbox_textpath.format("Name"), 'xpath')
            obj.Database_Field_Name = hw.GetElementText(details_dialogbox_textpath.format("Database Field Name"), 'xpath')
            obj.Maximum_Length = hw.GetElementText(details_dialogbox_textpath.format("Maximum Length"), 'xpath')
            obj.Data_Type = hw.GetElementText(details_dialogbox_textpath.format("Data Type"), 'xpath')
            obj.Valid_Values_Source = hw.GetElementText(details_dialogbox_textpath.format("Valid Values Source"), 'xpath')
            obj.Hide_Old_Value = hw.GetElementText(details_dialogbox_textpath.format("Hide Old Value"), 'xpath')
            obj.Decimal_Precision = hw.GetElementText(details_dialogbox_textpath.format("Decimal Precision"), 'xpath')
            obj.Include_Inactive_Users = hw.GetElementText(details_dialogbox_textpath.format("Include Inactive Users"), 'xpath')
            obj.UI_Field_Renderer = hw.GetElementText(details_dialogbox_textpath.format("UI Field Renderer"), 'xpath')
            obj.Transient = hw.GetElementText(details_dialogbox_textpath.format("Transient"), 'xpath')
            obj.Help_Text = hw.GetElementText(details_dialogbox_textpath.format("Help Text"), 'xpath')
            obj.Mask_Value_on_UI = hw.GetElementText(details_dialogbox_textpath.format("Mask Value on UI"), 'xpath')
            obj.Show_Trailing_Zeros = hw.GetElementText(details_dialogbox_textpath.format("Show Trailing Zeros"), 'xpath')
            obj.Default_Value = hw.GetElementText(details_dialogbox_textpath.format("Default Value"), 'xpath')
            obj.Hide_Seconds = hw.GetElementText(details_dialogbox_textpath.format("Hide Seconds"), 'xpath')
            obj.Required = hw.GetElementText(details_dialogbox_textpath.format("Required"), 'xpath')
            obj.Visibility = hw.GetElementText(details_dialogbox_textpath.format("Visibility"), 'xpath')
            obj.Status = hw.GetElementText(details_dialogbox_textpath.format("Status"), 'xpath')
            obj.Label = hw.GetElementText(details_dialogbox_textpath.format("Label"), 'xpath')
            obj.Cascade = hw.GetElementText(details_dialogbox_textpath.format("Cascade"), 'xpath')
            obj.Inactivated_By = hw.GetElementText(details_dialogbox_textpath.format("Inactivated By"), 'xpath')
            obj.End_Of_Period = hw.GetElementText(details_dialogbox_textpath.format("End Of Period"), 'xpath')
            obj_list.append(obj)

            hw.ClickElement('//button[@title="Done"]', 'xpath')
            time.sleep(3)

        Controller = Controller_MDF_Object_Fields()
        Controller.Fill_Worksheet(gspread_Sheet=Worksheet, Model_array_List=obj_list, RowNumber=1)
        Controller.Fill_Worksheet_Sec2(gspread_Sheet=Worksheet, Model_array_List=obj_list, RowNumber=self.UNI_RowNumber)
        self.UNI_RowNumber = self.UNI_RowNumber+1


MDF_Object_Fields_Class = TC_Rev_MDF_Object_Fields()
MDF_Object_Fields_Class.ExecuteProcess()
