# To validate the data of configure object definition in the gspread
from SAP_CODs_Task1b import SAPCOD_Task1
from login import login_instance
import time
import gspread
from gspread_formatting import *

gc = gspread.service_account()
sh = gc.open("Gspread")
wks = sh.worksheet("Object_Definition")


class Model_ObjectDefinition:
    item_id = ""
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
    data_record = [a for a in data_list if a.Code in processing_heading]

    return data_record, processing_heading


def cell(col_num=1, col="B"):
    if col_num == 1:
        col = 'B'
    elif col_num == 2:
        col = 'C'
    elif col_num == 3:
        col = 'D'
    elif col_num == 4:
        col = 'E'
    elif col_num == 5:
        col = 'F'
    elif col_num == 6:
        col = 'G'
    elif col_num == 7:
        col = 'H'
    elif col_num == 8:
        col = 'I'
    elif col_num == 9:
        col = 'J'
    elif col_num == 10:
        col = 'K'
    elif col_num == 11:
        col = 'L'
    elif col_num == 12:
        col = 'M'
    elif col_num == 13:
        col = 'N'
    elif col_num == 14:
        col = 'O'
    elif col_num == 15:
        col = 'P'
    else:
        pass
    return col


class CODGspread_Task4:
    login_instance.login_method()
    driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
    hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance

    def COD_gspread_Task4(self):
        link_1 = self.driver.current_url
        link_1_split = link_1.split('s.crb=')
        data_record, processing_heading = model_controller()
        red = CellFormat(backgroundColor=Color(1, 0, 0))
        green = CellFormat(backgroundColor=Color(0, 1, 0))

        for data in data_record:
            dict_1 = {'ID': data.item_id, 'Code': data.Code, 'Effective Dating': data.Effective_Dating,
                      'API Visibility': data.API_Visibility, 'Status': data.Status,
                      'MDF Version History': data.MDF_Version_History, 'Default Screen': data.Default_Screen,
                      'Label': data.Label, 'Description': data.Description, 'API Sub Version': data.API_Sub_Version,
                      'Subject User Field': data.Subject_User_Field, 'Workflow Routing': data.Workflow_Routing,
                      'Pending Data': data.Pending_Data, 'Todo Category': data.Todo_Category,
                      'Object Category': data.Object_Category}
            link_2 = f"https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=J74wSY%2fbBYLLOtmmiPHIU28YdKC%2bPsiT3awOLDacaPE%3d#c=1&t=GOObjectDefinition&i={data.Code}"
            link_2_split = link_2.split("s.crb=")
            COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1] + f"&t=GOObjectDefinition&i={data.Code}"
            self.driver.get(COD_Link)
            time.sleep(2)

            Cell_List = []
            Col = 1
            for key, value in dict_1.items():
                ID = dict_1["ID"] + 1
                if key != "ID":
                    cell_selector = f'(//tr[@class="form_field "]//td[.="{key}"]//following-sibling::td/*/*//span[.="{str(value).rstrip()}"])[1]'  # instance label as key and instance label value as value
                    element = self.hw.isElementPresent(cell_selector, 'xpath')
                    cell_column = cell(Col, "A")
                    if not element:
                        Cell_List.append([f'{cell_column}{ID}', red])
                    else:
                        Cell_List.append([f'{cell_column}{ID}', green])
                    Col += 1
                else:
                    pass

            print(Cell_List)
            format_cell_ranges(wks, Cell_List)


COD1_elements = SAPCOD_Task1()
COD_elements = COD1_elements.SAPCOD_task_1()
test = CODGspread_Task4()
test.COD_gspread_Task4()
