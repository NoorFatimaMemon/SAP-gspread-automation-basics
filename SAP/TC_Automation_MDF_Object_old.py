# To validate the data of configure object definition in the gspread
from login import login_instance
from Controller_MDF_Object_Validation import Controller_MDF_Object_Validation
import gspread
import time

gc = gspread.service_account()
sheet = gc.open("Gspread")
Worksheet = sheet.worksheet("Configure Object Definitions")


class TC_Automation_MDF_Object:
    login_instance.login_method()
    driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
    hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance
    Controller = Controller_MDF_Object_Validation()
    data_record, processing_heading = Controller.LoadData(gspread_Sheet=Worksheet)

    def ExecuteProcess(self):
        link_1 = self.driver.current_url
        link_1_split = link_1.split('s.crb=')
        link_2 = "https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=2K8CkVQJqWwL%2brEcUnCDHjVd%2fb%2fqqmVKOrsyYQk9p7E%3d"
        link_2_split = link_2.split("s.crb=")
        COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1]
        self.driver.get(COD_Link)
        time.sleep(2)

        self.hw.ClickElement('//span[@id="19__write_toggle"]', 'xpath')  # to click no search dropdown
        time.sleep(1)
        self.hw.ClickElement('//a[@title="Object Definition"]', 'xpath')  # to click object definition
        time.sleep(1)

        for MDF_obj in self.processing_heading:
            self.ProcessObject(MDF_obj)

    def ProcessObject(self, MDF_Object):
        for data in self.data_record:
            if MDF_Object == data.Title:
                link_1 = self.driver.current_url
                link_1_split = link_1.split('s.crb=')
                MDF_Obj = MDF_Object.split("(")[-1].replace(")", "")
                link_2 = f"https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=J74wSY%2fbBYLLOtmmiPHIU28YdKC%2bPsiT3awOLDacaPE%3d#c=1&t=GOObjectDefinition&i={MDF_Obj}"
                link_2_split = link_2.split("s.crb=")
                COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1] + f"&t=GOObjectDefinition&i={MDF_Obj}"
                self.driver.get(COD_Link)
                time.sleep(2)

                ID, title, code, effectivedating, APIvisibility, status, MDFversionhistory, defaultscreen, label, \
                description, APIsubversion, subjectuserfield, workflowrouting, pendingdata, todocategory, \
                objectcategory = data.item_id, data.Title, data.Code.rstrip(), data.Effective_Dating.rstrip(), data.API_Visibility.rstrip(), \
                                 data.Status.rstrip(), data.MDF_Version_History.rstrip(), data.Default_Screen.rstrip(), data.Label.rstrip(), \
                                 data.Description.rstrip(), data.API_Sub_Version.rstrip(), data.Subject_User_Field.rstrip(), \
                                 data.Workflow_Routing, data.Pending_Data.rstrip(), data.Todo_Category.rstrip(), data.Object_Category.rstrip()

                code_check = self.hw.isElementPresent(
                    f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Code']]//td[contains(@class,'field_value')]//span[.='{code}'and contains(@class, 'read')])[1]",
                    'xpath')
                effectivedating_check = self.hw.isElementPresent(
                    f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Effective Dating']]//td[contains(@class,'field_value')]//span[.='{effectivedating}'and contains(@class, 'read')])[1]",
                    'xpath')
                APIvisibility_check = self.hw.isElementPresent(
                    f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='API Visibility']]//td[contains(@class,'field_value')]//span[.='{APIvisibility}'and contains(@class, 'read')])[1]",
                    'xpath')
                status_check = self.hw.isElementPresent(
                    f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Status']]//td[contains(@class,'field_value')]//span[.='{status}'and contains(@class, 'read')])[1]",
                    'xpath')
                MDFversionhistory_check = self.hw.isElementPresent(
                    f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='MDF Version History']]//td[contains(@class,'field_value')]//span[.='{MDFversionhistory}'and contains(@class, 'read')])[1]",
                    'xpath')
                defaultscreen_check = self.hw.isElementPresent(
                    f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Default Screen']]//td[contains(@class,'field_value')]//span[.='{defaultscreen}'and contains(@class, 'read')])[1]",
                    'xpath')
                """label_check = self.hw.isElementPresent(
                    f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Label']]//td[contains(@class,'field_value')]//span[.='{label}'and contains(@class, 'read')])[1]",
                    'xpath')
                description_check = self.hw.isElementPresent(
                    f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Description']]//td[contains(@class,'field_value')]//div[@class='readComp undefined ectFieldshow' and .='{description}'])[1]",
                    'xpath')"""
                APIsubversion_check = self.hw.isElementPresent(
                    f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='API Sub Version']]//td[contains(@class,'field_value')]//span[.='{APIsubversion}'and contains(@class, 'read')])[1]",
                    'xpath')
                """subjectuserfield_check = self.hw.isElementPresent(
                    f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Subject User Field']]//td[contains(@class,'field_value')]//span[.='{subjectuserfield}'and contains(@class, 'read')])[1]",
                    'xpath')"""
                workflowrouting_check = self.hw.isElementPresent(
                    f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Workflow Routing']]//td[contains(@class,'field_value')]//span[.='{workflowrouting}'and contains(@class, 'read')])[1]",
                    'xpath')
                pendingdata_check = self.hw.isElementPresent(
                    f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Pending Data']]//td[contains(@class,'field_value')]//span[.='{pendingdata}'and contains(@class, 'read')])[1]",
                    'xpath')
                """todocategory_check = self.hw.isElementPresent(
                    f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Todo Category']]//td[contains(@class,'field_value')]//span[.='{todocategory}'and contains(@class, 'read')])[1]",
                    'xpath')"""
                objectcategory_check = self.hw.isElementPresent(
                    f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Object Category']]//td[contains(@class,'field_value')]//span[.='{objectcategory}'and contains(@class, 'read')])[1]",
                    'xpath')

                if code_check is False:
                    self.hw.ClickElement('//button[contains(@role,"button")]', 'xpath')
                    time.sleep(1)
                    self.hw.ClickElement('//a[@title="Make Correction"]', 'xpath')
                    time.sleep(1)
                    self.hw.ClickElement('//h1[@class="globalPageTitle"]', 'xpath')
                    time.sleep(1)

                    code_attribute = self.hw.GetElementAttribute(
                        "//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Code']]//td[contains(@class,'field_value')]//input",
                        'xpath', 'value')
                    self.hw.FillField(
                        "//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Code']]//td[contains(@class,'field_value')]//input",
                        'xpath', 'value', f'{code}')
                    time.sleep(1)
                    code_popup = self.hw.GetElement('//div[@role="dialog"]', 'xpath')
                    time.sleep(2)
                    if code_popup is not None:
                        self.hw.GetElementText('//span[@class="important-focus-msg"]', 'xpath')
                        self.hw.ClickElement('//button[@title="OK"]', 'xpath')
                        time.sleep(1)
                        self.hw.FillField(
                            "//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Code']]//td[contains(@class,'field_value')]//input",
                            'xpath', 'value', f'{code_attribute}')
                        time.sleep(1)
                        self.hw.ClickElement('//button[@title="OK"]', 'xpath')
                        time.sleep(1)
                        self.hw.ClickElement('//button[@title="Cancel"]', 'xpath')
                        time.sleep(1)

                if effectivedating_check or APIvisibility_check or status_check or MDFversionhistory_check or defaultscreen_check or APIsubversion_check or workflowrouting_check or pendingdata_check or objectcategory_check is False:
                    self.hw.ClickElement('//button[contains(@role,"button")]', 'xpath')
                    time.sleep(1)
                    self.hw.ClickElement('//a[@title="Make Correction"]', 'xpath')
                    self.hw.ClickElement('//h1[@class="globalPageTitle"]', 'xpath')
                    time.sleep(1)

                    # Element that give popup immediately when their value is changed & automatically fill their input box with previous value
                    if effectivedating_check is False:
                        self.hw.ClickElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Effective Dating']]//td[contains(@class,'field_value')]//span[contains(@id, 'write_toggle')]", 'xpath')
                        self.hw.ClickElement(f"//div[contains(@class,'globalContentBackground')]//ul//li[@role='option']//a[@title='{effectivedating}']", 'xpath')
                        effectivedating_popup = self.hw.GetElement('//div[@role="dialog"]', 'xpath')
                        if effectivedating_popup is not None:
                            self.hw.GetElementText('//span[@class="important-focus-msg"]', 'xpath')
                            self.hw.ClickElement('//button[@title="OK"]', 'xpath')

                    # Elements that can be changed on the instance by user
                    self.hw.FillField("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Label']]//td[contains(@class,'field_value')]//input", 'xpath', 'value', f'{label}')
                    time.sleep(1)
                    self.hw.ClickElement('(//button[contains(@class,"compact writeComp")])[1]', 'xpath')
                    time.sleep(1)
                    self.hw.FillField("//div[contains(@aria-label,'Translations')]//tr[.//td[.='Default Value']]//td[contains(@class,'field_value')]//input", 'xpath', 'value', f'{MDF_Obj}')
                    self.hw.ClickElement("//div[contains(@aria-label,'Translations')]//button[@title='Done']", 'xpath')

                    self.hw.FillField("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Description']]//td[@class='field_value']//textarea", 'xpath', 'linkText', f'{description}')
                    time.sleep(1)
                    self.hw.ClickElement('(//button[contains(@class,"compact writeComp")])[2]', 'xpath')
                    self.hw.ClickElement('(//button[contains(@class,"compact writeComp")])[2]', 'xpath')
                    time.sleep(1)
                    self.hw.FillField("//div[contains(@aria-label,'Translations')]//tr[.//td[.='Default Value']]//td[contains(@class,'field_value')]//textarea", 'xpath', 'linkText', f'{description}')
                    self.hw.ClickElement("//div[contains(@aria-label,'Translations')]//button[@title='Done']", 'xpath')

                    if APIsubversion_check is False:
                        self.hw.ClickElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='API Sub Version']]//td[contains(@class,'field_value')]//span[contains(@id, 'write_toggle')]", 'xpath')
                        time.sleep(1)
                        self.hw.ClickElement(f"//div[contains(@class,'globalContentBackground')]//ul//li[@role='option']//a[@title='{APIsubversion}']", 'xpath')

                    if workflowrouting_check is False:
                        self.hw.ClickElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Workflow Routing']]//td[contains(@class,'field_value')]//input", 'xpath')
                        if workflowrouting == '':
                            input_element = self.hw.GetElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Workflow Routing']]//td[contains(@class,'field_value')]//input", 'xpath')
                            input_element.clear()
                            self.hw.ClickElement('//h1[@class="globalPageTitle"]', 'xpath')
                        else:
                            workflowrouting_obj = workflowrouting.split('(')
                            self.hw.SendKeys("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Workflow Routing']]//td[contains(@class,'field_value')]//input", 'xpath', f'{workflowrouting_obj[0]}')
                            self.hw.ClickElement(f"//div[contains(@class,'globalContentBackground')]//ul//li[@role='option']//a[@title='{workflowrouting}']", 'xpath')

                    if pendingdata_check is False:
                        self.hw.ClickElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Pending Data']]//td[contains(@class,'field_value')]//span[contains(@id, 'write_toggle')]", 'xpath')
                        self.hw.ClickElement(f"//div[contains(@class,'globalContentBackground')]//ul//li[@role='option']//a[@title='{pendingdata}']", 'xpath')

                    # Elements that give popup after clicking save button & need to be filled with previous value
                    # Initially getting elements attribute from instance that will be later considered as previous value
                    APIvisibility_attribute = self.hw.GetElementAttribute(
                        "//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='API Visibility']]//td[contains(@class,'field_value')]//input",
                        'xpath', 'value')
                    status_attribute = self.hw.GetElementAttribute(
                        "//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Status']]//td[contains(@class,'field_value')]//input",
                        'xpath', 'value')
                    MDFversionhistory_attribute = self.hw.GetElementAttribute(
                        "//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='MDF Version History']]//td[contains(@class,'field_value')]//input",
                        'xpath', 'value')
                    defaultscreen_attribute = self.hw.GetElementAttribute(
                        "//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Default Screen']]//td[contains(@class,'field_value')]//input",
                        'xpath', 'value')
                    subjectuserfield_attribute = self.hw.GetElementAttribute(
                        "//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Subject User Field']]//td[contains(@class,'field_value')]//input", 'xpath', 'value')
                    objectcategory_attribute = self.hw.GetElementAttribute(
                        "//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Object Category']]//td[contains(@class,'field_value')]//input",
                        'xpath', 'value')

                    if APIvisibility_check is False:
                        self.hw.ClickElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='API Visibility']]//td[contains(@class,'field_value')]//span[contains(@id, 'write_toggle')]", 'xpath')
                        self.hw.ClickElement(f"//div[contains(@class,'globalContentBackground')]//ul//li[@role='option']//a[@title='{APIvisibility}']", 'xpath')

                    if status_check is False:
                        self.hw.ClickElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Status']]//td[contains(@class,'field_value')]//span[contains(@id, 'write_toggle')]", 'xpath')
                        self.hw.ClickElement(f"//div[contains(@class,'globalContentBackground')]//ul//li[@role='option']//a[@title='{status}']", 'xpath')

                    if MDFversionhistory_check is False:
                        self.hw.ClickElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='MDF Version History']]//td[contains(@class,'field_value')]//span[contains(@id, 'write_toggle')]", 'xpath')
                        self.hw.ClickElement(f"//div[contains(@class,'globalContentBackground')]//ul//li[@role='option']//a[@title='{MDFversionhistory}']", 'xpath')
                        time.sleep(2)
                        MDFversionhistory_popup = self.hw.GetElement('//div[@role="dialog"]', 'xpath')
                        if MDFversionhistory_popup is not None:
                            self.hw.GetElementText('//span[@class="important-focus-msg"]', 'xpath')
                            self.hw.ClickElement('//button[@title="Yes"]', 'xpath')

                    if defaultscreen_check is False:
                        self.hw.ClickElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Default Screen']]//td[contains(@class,'field_value')]//input", 'xpath')
                        if defaultscreen == '':
                            input_element = self.hw.GetElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Default Screen']]//td[contains(@class,'field_value')]//input", 'xpath')
                            input_element.clear()
                            self.hw.ClickElement('//h1[@class="globalPageTitle"]', 'xpath')
                        else:
                            defaultscreen_obj = defaultscreen.split('(')
                            self.hw.SendKeys("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Default Screen']]//td[contains(@class,'field_value')]//input", 'xpath', f'{defaultscreen_obj[0]}')
                            self.hw.ClickElement(f'//div[contains(@class,"globalContentBackground")]//ul//li[@role="option"]//div[@class="primary"]//a[@title="{defaultscreen}"]', 'xpath')

                    self.hw.FillField("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Subject User Field']]//td[contains(@class,'field_value')]//input", 'xpath', 'value', f'{subjectuserfield}')
                    self.hw.ClickElement('//h1[@class="globalPageTitle"]', 'xpath')

                    if objectcategory_check is False:
                        self.hw.ClickElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Object Category']]//td[contains(@class,'field_value')]//span[contains(@id, 'write_toggle')]", 'xpath')
                        self.hw.ClickElement(f"//div[contains(@class,'globalContentBackground')]//ul//li[@role='option']//a[@title='{objectcategory}']", 'xpath')

                    self.hw.ClickElement('//button[@title="Save"]', 'xpath')
                    time.sleep(2)

                    # After popup elements' values will be changed at the instance with their previous values
                    popup = self.hw.GetElement('//div[@role="dialog"]', 'xpath')
                    if popup is not None:
                        self.hw.GetElementText('//span[@class="important-focus-msg"]', 'xpath')
                        self.hw.ClickElement('//button[@title="OK"]', 'xpath')

                        if APIvisibility_check is False:
                            self.hw.ClickElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='API Visibility']]//td[contains(@class,'field_value')]//span[contains(@id, 'write_toggle')]", 'xpath')
                            self.hw.ClickElement(f"//div[contains(@class,'globalContentBackground')]//ul//li[@role='option']//a[@title='{APIvisibility_attribute}']", 'xpath')

                        if status_check is False:
                            self.hw.ClickElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Status']]//td[contains(@class,'field_value')]//span[contains(@id, 'write_toggle')]", 'xpath')
                            self.hw.ClickElement(f"//div[contains(@class,'globalContentBackground')]//ul//li[@role='option']//a[@title='{status_attribute}']", 'xpath')

                        if MDFversionhistory_check is False:
                            self.hw.ClickElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='MDF Version History']]//td[contains(@class,'field_value')]//span[contains(@id, 'write_toggle')]", 'xpath')
                            self.hw.ClickElement(f"//div[contains(@class,'globalContentBackground')]//ul//li[@role='option']//a[@title='{MDFversionhistory_attribute}']", 'xpath')
                            time.sleep(2)
                            MDFversionhistory_popup = self.hw.GetElement('//div[@role="dialog"]', 'xpath')
                            if MDFversionhistory_popup is not None:
                                self.hw.GetElementText('//span[@class="important-focus-msg"]', 'xpath')
                                self.hw.ClickElement('//button[@title="Yes"]', 'xpath')

                        if defaultscreen_check is False:
                            self.hw.ClickElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Default Screen']]//td[contains(@class,'field_value')]//input", 'xpath')
                            if defaultscreen == '':
                                input_element = self.hw.GetElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Default Screen']]//td[contains(@class,'field_value')]//input", 'xpath')
                                input_element.clear()
                                self.hw.ClickElement('//h1[@class="globalPageTitle"]', 'xpath')
                            else:
                                defaultscreen_obj2 = defaultscreen_attribute.split('(')
                                self.hw.SendKeys("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Default Screen']]//td[contains(@class,'field_value')]//input", 'xpath', f'{defaultscreen_obj2[0]}')
                                self.hw.ClickElement(f"//div[contains(@class,'globalContentBackground')]//ul//li[@role='option']//a[@title='{defaultscreen_attribute}']", 'xpath')

                        self.hw.FillField("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Subject User Field']]//td[contains(@class,'field_value')]//input", 'xpath', 'value', f'{subjectuserfield_attribute}')
                        self.hw.ClickElement('//h1[@class="globalPageTitle"]', 'xpath')

                        if objectcategory_check is False:
                            self.hw.ClickElement("//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Object Category']]//td[contains(@class,'field_value')]//span[contains(@id, 'write_toggle')]", 'xpath')
                            self.hw.ClickElement(f"//div[contains(@class,'globalContentBackground')]//ul//li[@role='option']//a[@title='{objectcategory_attribute}']", 'xpath')

            save_element = self.hw.GetElement('//button[@title="Save"]', 'xpath')
            if save_element.is_enabled():
                self.hw.ClickElement('//button[@title="Save"]', 'xpath')
            else:
                self.hw.ClickElement('//button[@title="Cancel"]', 'xpath')
            time.sleep(2)


MDF_Object_class = TC_Automation_MDF_Object()
MDF_Object_class.ExecuteProcess()
