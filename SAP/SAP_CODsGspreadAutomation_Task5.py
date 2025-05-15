# To change the data of configure object definition values from gspread to the instance
from login import login_instance
from SAP_CODs_Task1b import SAPCOD_Task1
import time
import gspread

gc = gspread.service_account()
sh = gc.open("Gspread-Task 1")
wks = sh.worksheet("COD")


class Model_ObjectDefinition:
    item_id = ""
    Title = ""
    Code = ""
    Effective_Dating = ""
    API_Visibility = ""
    Status = ""
    MDF_Version_History = ""
    Default_Screen = ""
    Label = ""
    Description = ""
    API_Sub_Version = ""
    Subject_User_Field = ""
    Workflow_Routing = ""
    Pending_Data = ""
    Todo_Category = ""
    Object_Category = ""


class Processing_ObjectDefinitionStatus:
    item_id = ""
    Object_Definition = ""
    Object_Definition_Status = ""


def model_controller():
    Sheet_Records = wks.get_all_records()
    processing_list = []
    data_list = []

    for record in Sheet_Records:
        Object_Definition_model = Model_ObjectDefinition()
        processing_status = Processing_ObjectDefinitionStatus()

        Object_Definition_model.item_id = record["Item ID"]
        Object_Definition_model.Title = record["Title"]
        Object_Definition_model.Code = record["Code"]
        Object_Definition_model.Effective_Dating = record["Effective Dating"]
        Object_Definition_model.API_Visibility = record["API Visibility"]
        Object_Definition_model.Status = record["Status"]
        Object_Definition_model.MDF_Version_History = record["MDF Version History"]
        Object_Definition_model.Default_Screen = record["Default Screen"]
        Object_Definition_model.Label = record["Label"]
        Object_Definition_model.Description = record["Description"]
        Object_Definition_model.API_Sub_Version = record["API Sub Version"]
        Object_Definition_model.Subject_User_Field = record["Subject User Field"]
        Object_Definition_model.Workflow_Routing = record["Workflow Routing"]
        Object_Definition_model.Pending_Data = record["Pending Data"]
        Object_Definition_model.Todo_Category = record["Todo Category"]
        Object_Definition_model.Object_Category = record["Object Category"]
        data_list.append(Object_Definition_model)

        processing_status.item_id = record["Item ID"]
        processing_status.Object_Definition = record["Object Definition"]
        processing_status.Object_Definition_Status = record["Object Definition Status"]
        processing_list.append(processing_status)

    processing_heading = [obj.Object_Definition for obj in processing_list if obj.Object_Definition_Status == 'Pending']
    data_record = [a for a in data_list if a.Title in processing_heading]

    return data_record, processing_heading


class Main:
    login_instance.login_method()
    driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
    hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance

    data_record, processing_heading, = model_controller()

    def ExecuteProcess(self):
        for objectdef_title in self.processing_heading:
            self.ProcessObject(Object_name=objectdef_title)

    def ProcessObject(self, Object_name):
        link_1 = self.driver.current_url
        link_1_split = link_1.split('s.crb=')
        obj_definition_title = Object_name.replace(" ", "")
        link_2 = f"https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=J74wSY%2fbBYLLOtmmiPHIU28YdKC%2bPsiT3awOLDacaPE%3d#c=1&t=GOObjectDefinition&i={obj_definition_title}"
        link_2_split = link_2.split("s.crb=")
        COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1] + f"&t=GOObjectDefinition&i={obj_definition_title}"
        self.driver.get(COD_Link)
        time.sleep(5)

        for data in self.data_record:
            [ID, title, code, effectivedating, APIvisibility, status, MDFversionhistory, defaultscreen, label,
             description, APIsubversion, subjectuserfield, workflowrouting, pendingdata, todocategory,
             objectcategory] = data.item_id, data.Title, data.Code.rstrip(), data.Effective_Dating.rstrip(), data.API_Visibility.rstrip(), \
                               data.Status.rstrip(), data.MDF_Version_History.rstrip(), data.Default_Screen.rstrip(), data.Label.rstrip(), data.Description.rstrip(), \
                               data.API_Sub_Version.rstrip(), data.Subject_User_Field.rstrip(), data.Workflow_Routing.rstrip(), data.Pending_Data.rstrip(), \
                               data.Todo_Category.rstrip(), data.Object_Category.rstrip()

            if Object_name == title:
                code_value = self.hw.GetElementText('(//td[@class="field_value"])[1]', 'xpath').rstrip()
                effectivedating_value = self.hw.GetElementText('(//td[@class="field_value"])[2]', 'xpath').rstrip()
                APIvisibility_value = self.hw.GetElementText('(//td[@class="field_value"])[3]', 'xpath').rstrip()
                status_value = self.hw.GetElementText('(//td[@class="field_value"])[4]', 'xpath').rstrip()
                MDFversionhistory_value = self.hw.GetElementText('(//td[@class="field_value"])[5]', 'xpath').rstrip()
                defaultscreen_value = self.hw.GetElementText('(//td[@class="field_value"])[6]', 'xpath').rstrip()
                label_value = self.hw.GetElementText('(//td[@class="field_value"])[7]', 'xpath').rstrip()
                description_value = self.hw.GetElementText('(//td[@class="field_value"])[8]', 'xpath').rstrip()
                APIsubversion_value = self.hw.GetElementText('(//td[@class="field_value"])[9]', 'xpath').rstrip()
                subjectuserfield_value = self.hw.GetElementText('(//td[@class="field_value"])[10]', 'xpath').rstrip()
                workflowrouting_value = self.hw.GetElementText('(//td[@class="field_value"])[11]', 'xpath').rstrip()
                pendingdata_value = self.hw.GetElementText('(//td[@class="field_value"])[12]', 'xpath').rstrip()
                todocategory_value = self.hw.GetElementText('(//td[@class="field_value"])[13]', 'xpath').rstrip()
                objectcategory_value = self.hw.GetElementText('(//td[@class="field_value"])[14]', 'xpath').rstrip()

                if code_value != code or effectivedating_value != effectivedating or APIvisibility_value != APIvisibility or status_value != status or MDFversionhistory_value != MDFversionhistory or defaultscreen_value != defaultscreen or label_value != label or description_value != description or APIsubversion_value != APIsubversion or subjectuserfield_value != subjectuserfield or workflowrouting_value != workflowrouting or pendingdata_value != pendingdata or todocategory_value != todocategory or objectcategory_value != objectcategory:
                    self.hw.ClickElement('//button[contains(@role,"button")]', 'xpath')
                    time.sleep(1)
                    self.hw.ClickElement('//a[@title="Make Correction"]', 'xpath')
                    self.hw.ClickElement('//h1[@class="globalPageTitle"]', 'xpath')
                    time.sleep(1)

                    self.hw.FillField2(f'//input[@value="{code_value}"]', 'xpath', 'value', f'{code}')
                    popup_1 = self.hw.GetElement('//div[@role="dialog"]', 'xpath')
                    if popup_1 is not None:
                        popup_text1 = self.hw.GetElementText('//span[@class="important-focus-msg"]', 'xpath')
                        print(popup_text1)
                        self.hw.ClickElement('//button[@title="OK"]', 'xpath')
                        self.hw.FillField2(f'//input[@value="{code_value}"]', 'xpath', 'value', f'{code_value}')
                        self.hw.ClickElement('//button[@title="OK"]', 'xpath')

                    if effectivedating_value != effectivedating:
                        self.hw.ClickElement('((//label[contains(.,"enter to see all list items")])[4]//following-sibling::span)[2]', 'xpath')
                        self.hw.ClickElement(f'//li[@role="option"]//a[@title="{effectivedating}"]', 'xpath')
                        popup = self.hw.GetElement('//div[@role="dialog"]', 'xpath')
                        if popup is not None:
                            popup_text = self.hw.GetElementText('//span[@class="important-focus-msg"]', 'xpath')
                            print(popup_text)
                            self.hw.ClickElement('//button[@title="OK"]', 'xpath')

                    if APIvisibility_value != APIvisibility:
                        self.hw.ClickElement('((//label[contains(.,"enter to see all list items")])[5]//following-sibling::span)[2]', 'xpath')
                        self.hw.ClickElement(f'//li[@role="option"]//a[@title="{APIvisibility}"]', 'xpath')
                        self.hw.ClickElement('//button[@title="Save"]', 'xpath')
                        popup = self.hw.GetElement('//div[@role="dialog"]', 'xpath')
                        if popup is not None:
                            popup_text = self.hw.GetElementText('//span[@class="important-focus-msg"]', 'xpath')
                            print(popup_text)
                            self.hw.ClickElement('//button[@title="OK"]', 'xpath')
                            self.hw.ClickElement('((//label[contains(.,"enter to see all list items")])[5]//following-sibling::span)[2]', 'xpath')
                            self.hw.ClickElement(f'//li[@role="option"]//a[@title="{APIvisibility_value}"]', 'xpath')

                    if status_value != status:
                        self.hw.ClickElement('((//label[contains(.,"enter to see all list items")])[6]//following-sibling::span)[2]', 'xpath')
                        self.hw.ClickElement(f'//li[@role="option"]//a[@title="{status}"]', 'xpath')
                        self.hw.ClickElement('//button[@title="Save"]', 'xpath')
                        popup = self.hw.GetElement('//div[@role="dialog"]', 'xpath')
                        if popup is not None:
                            popup_text = self.hw.GetElementText('//span[@class="important-focus-msg"]', 'xpath')
                            print(popup_text)
                            self.hw.ClickElement('//button[@title="OK"]', 'xpath')
                            self.hw.ClickElement('((//label[contains(.,"enter to see all list items")])[6]//following-sibling::span)[2]', 'xpath')
                            self.hw.ClickElement(f'//li[@role="option"]//a[@title="{status_value}"]', 'xpath')

                    if MDFversionhistory_value != MDFversionhistory:
                        self.hw.ClickElement('((//label[contains(.,"enter to see all list items")])[7]//following-sibling::span)[2]', 'xpath')
                        self.hw.ClickElement(f'//li[@role="option"]//a[@title="{MDFversionhistory}"]', 'xpath')
                        self.hw.ClickElement('//button[@title="Yes"]', 'xpath')
                        self.hw.ClickElement('//button[@title="Save"]', 'xpath')
                        popup = self.hw.GetElement('//div[@role="dialog"]', 'xpath')
                        if popup is not None:
                            popup_text = self.hw.GetElementText('//span[@class="important-focus-msg"]', 'xpath')
                            print(popup_text)
                            self.hw.ClickElement('//button[@title="OK"]', 'xpath')
                            self.hw.ClickElement('((//label[contains(.,"enter to see all list items")])[7]//following-sibling::span)[2]', 'xpath')
                            self.hw.ClickElement(f'//li[@role="option"]//a[@title="{MDFversionhistory_value}"]', 'xpath')
                            self.hw.ClickElement('//button[@title="Yes"]', 'xpath')

                    self.hw.FillField2('//input[@aria-label="Default Screen"]', 'xpath', 'title', f'{defaultscreen}')
                    defaultscreen_element = self.hw.GetElement(f'//a[contains(@title, "{defaultscreen}")]', 'xpath')
                    if defaultscreen_element is not None:
                        self.hw.ClickElement(f'//a[contains(@title, "{defaultscreen}")]', 'xpath')
                        self.hw.ClickElement('//button[@title="Save"]', 'xpath')
                        popup = self.hw.GetElement('//div[@role="dialog"]', 'xpath')
                        if popup is not None:
                            popup_text = self.hw.GetElementText('//span[@class="important-focus-msg"]', 'xpath')
                            print(popup_text)
                            self.hw.ClickElement('//button[@title="OK"]', 'xpath')
                            clear_element = self.hw.GetElement('//input[@aria-label="Default Screen"]', 'xpath')
                            clear_element.clear()
                            self.hw.ClickElement('//h1[@class="globalPageTitle"]', 'xpath')

                    self.hw.FillField2('(//td[@class="field_value"])[7]//input', 'xpath', 'innerText', f'{label}')
                    if description_value != description:
                        self.hw.FillField2('(//td[@class="field_value"])[8]//textarea', 'xpath', 'value', f'{description}')
                        self.hw.ClickElement('(//button[contains(@class,"compact writeComp")])[2]', 'xpath')
                        self.hw.ClickElement('(//button[contains(@class,"compact writeComp")])[2]', 'xpath')
                        time.sleep(2)
                        self.hw.FillField2('(//textarea)[2]', 'xpath', 'value', f'{description}')
                        self.hw.ClickElement('//button[@title="Done"]', 'xpath')

                    if APIsubversion_value != APIsubversion:
                        self.hw.ClickElement('((//label[contains(.,"enter to see all list items")])[8]//following-sibling::span)[2]', 'xpath')
                        time.sleep(1)
                        self.hw.ClickElement(f'//li[@role="option"]//a[@title="{APIsubversion}"]', 'xpath')

                    self.hw.FillField2('(//td[@class="field_value"])[10]//input', 'xpath', 'innerText', f'{subjectuserfield}')

                    if workflowrouting_value != workflowrouting:
                        workflowrouting_obj = workflowrouting.split('(')
                        workflowrouting_obj_2 = workflowrouting_obj[0].rstrip()
                        self.hw.ClickElement('//input[@aria-label="Workflow Routing"]', 'xpath')
                        self.hw.SendKeys('//input[@aria-label="Workflow Routing"]', 'xpath', f'{workflowrouting_obj_2}')
                        self.hw.ClickElement(f'//a[contains(@title, "{workflowrouting_obj_2}")]', 'xpath')

                    if pendingdata_value != pendingdata:
                        self.hw.ClickElement('((//label[contains(.,"enter to see all list items")])[9]//following-sibling::span)[2]', 'xpath')
                        self.hw.ClickElement(f'//li[@role="option"]//a[@title="{pendingdata}"]', 'xpath')

                    if objectcategory_value != objectcategory:
                        self.hw.ClickElement('((//label[contains(.,"Typed search results will be available")])[4]//following-sibling::span)[2]', 'xpath')
                        self.hw.ClickElement(f'//li[@role="option"]//a[@title="{objectcategory}"]', 'xpath')
                        self.hw.ClickElement('//button[@title="Save"]', 'xpath')
                        popup = self.hw.GetElement('//div[@role="dialog"]', 'xpath')
                        if popup is not None:
                            popup_text = self.hw.GetElementText('//span[@class="important-focus-msg"]', 'xpath')
                            print(popup_text)
                            self.hw.ClickElement('//button[@title="OK"]', 'xpath')
                            self.hw.ClickElement('((//label[contains(.,"Typed search results will be available")])[4]//following-sibling::span)[2]', 'xpath')
                            self.hw.ClickElement(f'//li[@role="option"]//a[@title="{objectcategory_value}"]', 'xpath')

                    self.hw.ClickElement('//button[@title="Save"]', 'xpath')
                    popup = self.hw.GetElement('//div[@role="dialog"]', 'xpath')
                    if popup is not None:
                        popup_text = self.hw.GetElementText('//span[@class="important-focus-msg"]', 'xpath')
                        print(popup_text)
                        popup_element = self.hw.GetElement('//button[@title="No"]', 'xpath')
                        if popup_element is not None:
                            self.hw.ClickElement('//button[@title="No"]', 'xpath')
                            time.sleep(2)
                        else:
                            self.hw.ClickElement('//button[@title="OK"]', 'xpath')
                            save_element = self.hw.GetElement('//button[@title="Save"]', 'xpath')
                            if save_element.is_enabled():
                                self.hw.ClickElement('//button[@title="Save"]', 'xpath')
                            else:
                                self.hw.ClickElement('//button[@title="Cancel"]', 'xpath')
                            time.sleep(2)
        time.sleep(2)


COD1_elements = SAPCOD_Task1()
COD_elements = COD1_elements.SAPCOD_task_1()
main_COD = Main()
main_COD.ExecuteProcess()
