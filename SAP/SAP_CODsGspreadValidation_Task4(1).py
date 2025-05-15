# To validate the data of configure object definition values in the gspread
"""from SAP.SAP_CODs_Task1b import SAPCOD_Task1
from login import login_instance
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
    data_record = [vars(a) for a in data_list if a.Title in processing_heading]

    return data_record, processing_heading


class CODGspread_Task4:
    login_instance.login_method()
    driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
    hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance

    def COD_gspread_Task4(self):
        link_1 = self.driver.current_url
        link_1_split = link_1.split('s.crb=')
        data_record, processing_heading = model_controller()
        invalid_cell_format = {"backgroundColor": {"red": 1, "green": 0, "blue": 0}}
        valid_cell_format = {"backgroundColor": {"red": 0, "green": 1, "blue": 0}}
        processed_title = set()
        Previous_title = None

        for data in data_record:
            [ID, title, code, effectivedating, APIvisibility, status, MDFversionhistory, defaultscreen, label,
             description, APIsubversion, subjectuserfield, workflowrouting, pendingdata, todocategory,
             objectcategory] = data.values()

            link_2 = f"https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=J74wSY%2fbBYLLOtmmiPHIU28YdKC%2bPsiT3awOLDacaPE%3d#c=1&t=GOObjectDefinition&i={code}"
            link_2_split = link_2.split("s.crb=")
            COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1] + f"&t=GOObjectDefinition&i={code}"
            self.driver.get(COD_Link)
            time.sleep(5)

            object_definition = self.hw.GetElementText('//span[@class="pwhHeaderTitle globalHumanistText"]', 'xpath')
            object_definition_p1 = object_definition.split('(')
            object_definition_p2 = object_definition_p1[0].split(':')
            object_definition_p3 = object_definition_p2[1].strip()

            if Previous_title in processed_title:
                unique_objectdefinition = wks.find(f'{Previous_title}', in_column=18)
                cell = unique_objectdefinition.row
                wks.update(f'S{cell}', 'Processed')
            else:
                pass

            Previous_title = title
            processed_title.add(title)

            wks.format(f'B{ID + 1}', valid_cell_format) if title == object_definition_p3 else wks.format(f'B{ID + 1}', invalid_cell_format)

            code_value = self.hw.GetElementText('(//td[@class="field_value"])[1]', 'xpath')
            wks.format(f'C{ID + 1}', valid_cell_format) if code == code_value else wks.format(f'C{ID + 1}', invalid_cell_format)

            effectivedating_value = self.hw.GetElementText('(//td[@class="field_value"])[2]', 'xpath')
            wks.format(f'D{ID + 1}', valid_cell_format) if effectivedating == effectivedating_value else wks.format(f'D{ID + 1}', invalid_cell_format)

            APIvisibility_value = self.hw.GetElementText('(//td[@class="field_value"])[3]', 'xpath')
            wks.format(f'E{ID + 1}', valid_cell_format) if APIvisibility == APIvisibility_value else wks.format(f'E{ID + 1}', invalid_cell_format)

            status_value = self.hw.GetElementText('(//td[@class="field_value"])[4]', 'xpath')
            wks.format(f'F{ID + 1}', valid_cell_format) if status == status_value else wks.format(f'F{ID + 1}', invalid_cell_format)

            MDFversionhistory_value = self.hw.GetElementText('(//td[@class="field_value"])[5]', 'xpath')
            wks.format(f'G{ID + 1}', valid_cell_format) if MDFversionhistory == MDFversionhistory_value else wks.format(f'G{ID + 1}', invalid_cell_format)

            defaultscreen_value = self.hw.GetElementText('(//td[@class="field_value"])[6]', 'xpath')
            wks.format(f'H{ID + 1}', valid_cell_format) if defaultscreen == defaultscreen_value else wks.format(f'H{ID + 1}', invalid_cell_format)

            label_value = self.hw.GetElementText('(//td[@class="field_value"])[7]', 'xpath')
            wks.format(f'I{ID + 1}', valid_cell_format) if label == label_value else wks.format(f'I{ID + 1}', invalid_cell_format)

            description_value = self.hw.GetElementText('(//td[@class="field_value"])[8]', 'xpath')
            wks.format(f'J{ID + 1}', valid_cell_format) if description == description_value else wks.format(f'J{ID + 1}', invalid_cell_format)

            APIsubversion_value = self.hw.GetElementText('(//td[@class="field_value"])[9]', 'xpath')
            wks.format(f'K{ID + 1}', valid_cell_format) if APIsubversion == APIsubversion_value else wks.format(f'K{ID + 1}', invalid_cell_format)

            subjectuserfield_value = self.hw.GetElementText('(//td[@class="field_value"])[10]', 'xpath')
            wks.format(f'L{ID + 1}', valid_cell_format) if subjectuserfield == subjectuserfield_value else wks.format(f'L{ID + 1}', invalid_cell_format)

            workflowrouting_value = self.hw.GetElementText('(//td[@class="field_value"])[11]', 'xpath')
            wks.format(f'M{ID + 1}', valid_cell_format) if workflowrouting == workflowrouting_value else wks.format(f'M{ID + 1}', invalid_cell_format)

            pendingdata_value = self.hw.GetElementText('(//td[@class="field_value"])[12]', 'xpath')
            wks.format(f'N{ID + 1}', valid_cell_format) if pendingdata == pendingdata_value else wks.format(f'N{ID + 1}', invalid_cell_format)

            todocategory_value = self.hw.GetElementText('(//td[@class="field_value"])[13]', 'xpath')
            wks.format(f'O{ID + 1}', valid_cell_format) if todocategory == todocategory_value else wks.format(f'O{ID + 1}', invalid_cell_format)

            objectcategory_value = self.hw.GetElementText('(//td[@class="field_value"])[14]', 'xpath')
            wks.format(f'P{ID + 1}', valid_cell_format) if objectcategory == objectcategory_value else wks.format(f'P{ID + 1}', invalid_cell_format)

        last_objectdefinition = wks.find('Pending', in_column=19)
        cell_last_objectdefinition = last_objectdefinition.row
        wks.update(f'S{cell_last_objectdefinition}', 'Processed')


COD1_elements = SAPCOD_Task1()
COD_elements = COD1_elements.SAPCOD_task_1()
test = CODGspread_Task4()
test.COD_gspread_Task4()"""

from turtle import color
from SAP_CODs_Task1b import SAPCOD_Task1
from login import login_instance
import time
import gspread
from gspread import Cell
from gspread_formatting import *

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


class CODGspread_Task4:
    login_instance.login_method()
    driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
    hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance

    def COD_gspread_Task4(self):
        link_1 = self.driver.current_url
        link_1_split = link_1.split('s.crb=')
        data_record, processing_heading = model_controller()


        for data in data_record:
            [ID, Title, Code, Effective_Dating, API_Visibility, Status, MDF_Version_History, Default_Screen, Label,
             Description, API_Sub_Version, Subject_User_Field, Workflow_Routing, Pending_Data, Todo_Category,
             Object_Category] = data.item_id, data.Title, data.Code, data.Effective_Dating, data.API_Visibility, \
                               data.Status, data.MDF_Version_History, data.Default_Screen, data.Label, data.Description, \
                               data.API_Sub_Version, data.Subject_User_Field, data.Workflow_Routing, data.Pending_Data, \
                               data.Todo_Category, data.Object_Category

            link_2 = f"https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=J74wSY%2fbBYLLOtmmiPHIU28YdKC%2bPsiT3awOLDacaPE%3d#c=1&t=GOObjectDefinition&i={Code}"
            link_2_split = link_2.split("s.crb=")
            COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1] + f"&t=GOObjectDefinition&i={Code}"
            self.driver.get(COD_Link)
            time.sleep(2)

            # object_definition = self.hw.GetElementText('//span[@class="pwhHeaderTitle globalHumanistText"]', 'xpath')
            # object_definition_p1 = object_definition.split('(')
            # object_definition_p2 = object_definition_p1[0].split(':')
            # object_definition_p3 = object_definition_p2[1].strip()

            Cell_List = []
            attribute_names = [Code, Effective_Dating, API_Visibility, Status, MDF_Version_History, Default_Screen,
                               Label, Description, API_Sub_Version, Subject_User_Field, Workflow_Routing, Pending_Data,
                               Todo_Category, Object_Category]

            """for i, attr_name in enumerate(attribute_names, start=1):
                property_value = getattr(data, attr_name)
                cell_selector = f'(//tr[@class="form_field "])[{i}]//td[@class="field_value"]'

                if self.hw.isElementPresent(cell_selector, 'xpath'):
                    Cell_List.append(Cell(row=ID+1, col=i + 2, value=property_value))
                    format_cell_range(wks, [Cell(row=ID+1, col=i + 2)], valid_cell_format)
                else:
                    format_cell_range(wks, [Cell(row=ID+1, col=i + 2)], invalid_cell_format)
            attribute_names = ["Code", "Effective_Dating", "API_Visibility", "Status", "MDF_Version_History", "Default_Screen",
                               "Label", "Description", "API_Sub_Version", "Subject_User_Field", "Workflow_Routing", "Pending_Data",
                               "Todo_Category", "Object_Category"]"""
            i = 3
            red = CellFormat(backgroundColor=color(1, 0, 0))
            green = CellFormat(backgroundColor=color(0, 0, 1))
            for attr_name in attribute_names:
                attribute_name = attr_name.strip(" ")
                cell_selector = f'(//tr[@class="form_field "]//td//following-sibling::td/*/*//span[.="{attribute_name}"])[1]'
                element=self.hw.isElementPresent(cell_selector, 'xpath')
                if not element:
                    # format_cell_range(wks, f"C{ID+1}:P{ID+1}", red)
                    Cell_List.append(Cell(row=ID+1, col=i, value=red))
                else:
                    Cell_List.append(Cell(row=ID+1, col=i, value=green))

                i += 1
                format_cell_ranges(wks, Cell_List)




COD1_elements = SAPCOD_Task1()
COD_elements = COD1_elements.SAPCOD_task_1()
test = CODGspread_Task4()
test.COD_gspread_Task4()

