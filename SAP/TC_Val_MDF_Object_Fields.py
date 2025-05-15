from login import login_instance
from Controller_MDF_Object_Fields import Controller_MDF_Object_Fields, ValidationProps
import gspread
from gspread_formatting import *
import time

gc = gspread.service_account()
sheet = gc.open("Gspread")
Worksheet = sheet.worksheet("Fields COD")


def UpdateStatus(obj):
    UniqueCode_cell = Worksheet.find(f'{obj}', in_column=26).row
    Worksheet.update(f'AA{UniqueCode_cell}', 'Processed')


class TC_Validation_MDF_Object:
    login_instance.login_method()
    driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
    hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance
    Controller = Controller_MDF_Object_Fields()
    data_record, processing_heading = Controller.Load_Data(gspread_Sheet=Worksheet)
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
        link_1 = self.driver.current_url
        link_1_split = link_1.split('s.crb=')
        link_2 = f"https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=J74wSY%2fbBYLLOtmmiPHIU28YdKC%2bPsiT3awOLDacaPE%3d#c=1&t=GOObjectDefinition&i={MDF_Object}"
        link_2_split = link_2.split("s.crb=")
        time.sleep(2)
        COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1] + f"&t=GOObjectDefinition&i={MDF_Object}"
        self.driver.get(COD_Link)
        time.sleep(2)
        Cell_List = []

        for data in [d for d in self.data_record if MDF_Object == d.Code]:
            ID = data.item_id + 1

            if self.hw.isElementPresent(
                    '//span[@class="important-focus-msg"]//div[text()="Object does not Exist Or No Permission"]',
                    'xpath'):
                Cell_List.append([f'{ValidationProps.Code}{ID}:{ValidationProps.End_Of_Period}{ID}', self.red])
                self.hw.Popup(
                    '//span[@class="important-focus-msg"]//div[text()="Object does not Exist Or No Permission"]',
                    'xpath')

            else:
                if not self.hw.isElementPresent(
                        f"(//div[contains(@class,'MDFViewPanel')]//tr[.//td[.='Code']]//td[contains(@class,'field_value')]//span[.='{data.Code}' and contains(@class, 'read')])[1]",
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Code}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Code}{ID}', self.green])

                details_xpath = f'//table[@aria-label="Fields"]//td[contains(@id,"0")]//span[@class="writeComp ectFormFieldFocusMark textBox writeFieldUnchange"]//parent::span//span[text()="{data.Name}"]//ancestor::tr[contains(@id,"row")]//td//a[contains(@class,"readComp")]'
                self.hw.ClickElement(details_xpath, "xpath")
                time.sleep(2)
                details_dialogbox_textpath = '(//div[@role="dialog"]//div[contains(@class,"readMode")]//table[@role="none"]//tr[.//label[text()="{0}"]]//td[contains(@class,"field_value")]//span[.="{1}" and contains(@class,"read")])[1]'

                if not self.hw.isElementPresent(details_dialogbox_textpath.format("Name", data.Name), 'xpath'):
                    Cell_List.append([f'{ValidationProps.Name}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Name}{ID}', self.green])

                if not self.hw.isElementPresent(
                        details_dialogbox_textpath.format("Database Field Name", data.Database_Field_Name), 'xpath'):
                    Cell_List.append([f'{ValidationProps.Database_Field_Name}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Database_Field_Name}{ID}', self.green])

                if not self.hw.isElementPresent(
                        details_dialogbox_textpath.format("Maximum Length", data.Maximum_Length), 'xpath'):
                    Cell_List.append([f'{ValidationProps.Maximum_Length}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Maximum_Length}{ID}', self.green])

                if not self.hw.isElementPresent(details_dialogbox_textpath.format("Data Type", data.Data_Type),
                                                'xpath'):
                    Cell_List.append([f'{ValidationProps.Data_Type}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Data_Type}{ID}', self.green])

                if not self.hw.isElementPresent(
                        details_dialogbox_textpath.format("Valid Values Source", data.Valid_Values_Source),
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Valid_Values_Source}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Valid_Values_Source}{ID}', self.green])

                if not self.hw.isElementPresent(
                        details_dialogbox_textpath.format("Hide Old Value", data.Hide_Old_Value),
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Hide_Old_Value}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Hide_Old_Value}{ID}', self.green])

                if not self.hw.isElementPresent(
                        details_dialogbox_textpath.format("Decimal Precision", data.Decimal_Precision),
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Decimal_Precision}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Decimal_Precision}{ID}', self.green])

                if not self.hw.isElementPresent(
                        details_dialogbox_textpath.format("Include Inactive Users", data.Include_Inactive_Users),
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Include_Inactive_Users}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Include_Inactive_Users}{ID}', self.green])

                if not self.hw.isElementPresent(
                        details_dialogbox_textpath.format("UI Field Renderer", data.UI_Field_Renderer),
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.UI_Field_Renderer}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.UI_Field_Renderer}{ID}', self.green])

                if not self.hw.isElementPresent(details_dialogbox_textpath.format("Transient", data.Transient),
                                                'xpath'):
                    Cell_List.append([f'{ValidationProps.Transient}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Transient}{ID}', self.green])

                if not self.hw.isElementPresent(details_dialogbox_textpath.format("Help Text", data.Help_Text),
                                                'xpath'):
                    Cell_List.append([f'{ValidationProps.Help_Text}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Help_Text}{ID}', self.green])

                if not self.hw.isElementPresent(
                        details_dialogbox_textpath.format("Mask Value on UI", data.Mask_Value_on_UI),
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Mask_Value_on_UI}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Mask_Value_on_UI}{ID}', self.green])

                if not self.hw.isElementPresent(
                        details_dialogbox_textpath.format("Show Trailing Zeros", data.Show_Trailing_Zeros),
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Show_Trailing_Zeros}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Show_Trailing_Zeros}{ID}', self.green])

                if not self.hw.isElementPresent(details_dialogbox_textpath.format("Default Value", data.Default_Value),
                                                'xpath'):
                    Cell_List.append([f'{ValidationProps.Default_Value}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Default_Value}{ID}', self.green])

                if not self.hw.isElementPresent(details_dialogbox_textpath.format("Hide Seconds", data.Hide_Seconds),
                                                'xpath'):
                    Cell_List.append([f'{ValidationProps.Hide_Seconds}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Hide_Seconds}{ID}', self.green])

                if not self.hw.isElementPresent(details_dialogbox_textpath.format("Required", data.Required),
                                                'xpath'):
                    Cell_List.append([f'{ValidationProps.Required}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Required}{ID}', self.green])

                if not self.hw.isElementPresent(details_dialogbox_textpath.format("Visibility", data.Visibility),
                                                'xpath'):
                    Cell_List.append([f'{ValidationProps.Visibility}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Visibility}{ID}', self.green])

                if not self.hw.isElementPresent(details_dialogbox_textpath.format("Status", data.Status),
                                                'xpath'):
                    Cell_List.append([f'{ValidationProps.Status}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Status}{ID}', self.green])

                if not self.hw.isElementPresent(details_dialogbox_textpath.format("Label", data.Label),
                                                'xpath'):
                    Cell_List.append([f'{ValidationProps.Label}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Label}{ID}', self.green])

                if not self.hw.isElementPresent(details_dialogbox_textpath.format("Cascade", data.Cascade),
                                                'xpath'):
                    Cell_List.append([f'{ValidationProps.Cascade}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Cascade}{ID}', self.green])

                if not self.hw.isElementPresent(
                        details_dialogbox_textpath.format("Inactivated By", data.Inactivated_By),
                        'xpath'):
                    Cell_List.append([f'{ValidationProps.Inactivated_By}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.Inactivated_By}{ID}', self.green])

                if not self.hw.isElementPresent(details_dialogbox_textpath.format("End Of Period", data.End_Of_Period),
                                                'xpath'):
                    Cell_List.append([f'{ValidationProps.End_Of_Period}{ID}', self.red])
                else:
                    Cell_List.append([f'{ValidationProps.End_Of_Period}{ID}', self.green])

                self.hw.ClickElement('//button[@title="Done"]', 'xpath')
                time.sleep(3)

        format_cell_ranges(Worksheet, Cell_List)
        UpdateStatus(obj=MDF_Object)


MDF_Object_class = TC_Validation_MDF_Object()
MDF_Object_class.ExecuteProcess()
