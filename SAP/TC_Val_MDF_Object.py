from login import login_instance
from Controller_MDF_Object import Controller_MDF_Object, ValidationProps
import gspread
from gspread_formatting import *
import time

gc = gspread.service_account()
sheet = gc.open("Gspread")
Worksheet = sheet.worksheet("Configure Object Definitions")


class TC_Validation_MDF_Object:
    login_instance.login_method()
    driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
    hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance
    Controller = Controller_MDF_Object()
    data_record, processing_heading = Controller.LoadData(gspread_Sheet=Worksheet)
    red = CellFormat(backgroundColor=Color(1, 0, 0))
    green = CellFormat(backgroundColor=Color(0, 1, 0))

    def ExecuteProcess(self):
        link_1 = self.driver.current_url
        link_1_split = link_1.split('s.crb=')
        link_2 = "https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=2K8CkVQJqWwL%2brEcUnCDHjVd%2fb%2fqqmVKOrsyYQk9p7E%3d"
        link_2_split = link_2.split("s.crb=")
        time.sleep(0.5)
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
        for data in [d for d in self.data_record if MDF_Object == d.Title]:
            link_1 = self.driver.current_url
            link_1_split = link_1.split('s.crb=')
            link_2 = f"https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=J74wSY%2fbBYLLOtmmiPHIU28YdKC%2bPsiT3awOLDacaPE%3d#c=1&t=GOObjectDefinition&i={data.Code}"
            link_2_split = link_2.split("s.crb=")
            time.sleep(2)
            COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1] + f"&t=GOObjectDefinition&i={data.Code}"
            self.driver.get(COD_Link)
            time.sleep(2)

            Cell_List = []
            ID = data.item_id + 1

            if self.hw.isElementPresent('//span[@class="important-focus-msg"]//div[text()="Object does not Exist Or No Permission"]', 'xpath'):
                Cell_List.append([f'{ValidationProps.Title}{ID}:{ValidationProps.Base_Date_Field_For_Blocking}{ID}', self.red])
                self.hw.Popup('//span[@class="important-focus-msg"]//div[text()="Object does not Exist Or No Permission"]', 'xpath')

            else:
                if not self.hw.isElementPresent(
                        f'//div[@class="viewPanelContainer"]//div[contains(@aria-label,"Object Definition: {data.Title}")]//div',
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Title}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Title}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Code']]//td[contains(@class,'field_value')]//span[.='{data.Code}' and contains(@class, 'read')])[1]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Code}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Code}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Effective Dating']]//td[contains(@class,'field_value')]//span[.='{data.Effective_Dating}' and contains(@class, 'read')])[1]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Effective_Dating}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Effective_Dating}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='API Visibility']]//td[contains(@class,'field_value')]//span[.='{data.API_Visibility}' and contains(@class, 'read')])[1]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.API_Visibility}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.API_Visibility}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Status']]//td[contains(@class,'field_value')]//span[.='{data.Status}' and contains(@class, 'read')])[1]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Status}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Status}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='MDF Version History']]//td[contains(@class,'field_value')]//span[.='{data.MDF_Version_History}' and contains(@class, 'read')])[1]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.MDF_Version_History}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.MDF_Version_History}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Default Screen']]//td[contains(@class,'field_value')]//span[.='{data.Default_Screen}' and contains(@class, 'read')])[1]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Default_Screen}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Default_Screen}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Label']]//td[contains(@class,'field_value')]//span[.='{data.Label}' and contains(@class, 'read')])[1]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Label}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Label}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Description']]//td[contains(@class,'field_value')]//div[.='{data.Description}'])[1]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Description}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Description}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='API Sub Version']]//td[contains(@class,'field_value')]//span[.='{data.API_Sub_Version}' and contains(@class, 'read')])[1]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.API_Sub_Version}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.API_Sub_Version}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Subject User Field']]//td[contains(@class,'field_value')]//span[.='{data.Subject_User_Field}' and contains(@class, 'read')])[1]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Subject_User_Field}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Subject_User_Field}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Workflow Routing']]//td[contains(@class,'field_value')]//span[.='{data.Workflow_Routing}' and contains(@class, 'read')])[1]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Workflow_Routing}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Workflow_Routing}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Pending Data']]//td[contains(@class,'field_value')]//span[.='{data.Pending_Data}' and contains(@class, 'read')])[1]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Pending_Data}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Pending_Data}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Todo Category']]//td[contains(@class,'field_value')]//span[.='{data.Todo_Category}' and contains(@class, 'read')])[1]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Todo_Category}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Todo_Category}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Object Category']]//td[contains(@class,'field_value')]//span[.='{data.Object_Category}' and contains(@class, 'read')])[1]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Object_Category}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Object_Category}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"((//div[contains(@class,'MDFViewPanel')]//tr//div[@class='MDFRepeatingForm']//table)[2]//span[contains(@class,'writeComp')]//input[@aria-label='Secured']//ancestor::div)[25]//span[text()='{data.Secured}' and contains(@class,'readComp')]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Secured}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Secured}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"((//div[contains(@class,'MDFViewPanel')]//tr//div[@class='MDFRepeatingForm']//table)[2]//span[contains(@class,'writeComp')]//input[@aria-label='Permission Category']//ancestor::div)[25]//span[text()='{data.Permission_Category}' and contains(@class,'readComp')]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Permission_Category}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Permission_Category}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"((//div[contains(@class,'MDFViewPanel')]//tr//div[@class='MDFRepeatingForm']//table)[2]//span[contains(@class,'writeComp')]//label[text()='RBP Subject User Field']//ancestor::div)[25]//span[.='{data.RBP_Subject_User_Field}' and contains(@class,'readComp')]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.RBP_Subject_User_Field}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.RBP_Subject_User_Field}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"((//div[contains(@class,'MDFViewPanel')]//tr//div[@class='MDFRepeatingForm']//table)[2]//span[contains(@class,'writeComp')]//input[@aria-label='CREATE Respects Target Criteria']//ancestor::div)[25]//span[text()='{data.CREATE_Respects_Target_Criteria}' and contains(@class,'readComp')]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.CREATE_Respects_Target_Criteria}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.CREATE_Respects_Target_Criteria}{ID}', self.green])

                if not self.hw.isElementPresent(
                        f"((//div[contains(@class,'MDFViewPanel')]//tr//div[@class='MDFRepeatingForm']//table)[2]//span[contains(@class,'writeComp')]//label[text()='Base Date Field For Blocking']//ancestor::div)[25]//span[.='{data.Base_Date_Field_For_Blocking}' and contains(@class,'readComp')]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Base_Date_Field_For_Blocking}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Base_Date_Field_For_Blocking}{ID}', self.green])

            format_cell_ranges(Worksheet, Cell_List)


MDF_Object_class = TC_Validation_MDF_Object()
MDF_Object_class.ExecuteProcess()
