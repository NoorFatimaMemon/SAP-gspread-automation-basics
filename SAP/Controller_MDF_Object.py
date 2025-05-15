from TC_Model_MDF_Object import Model_ObjectDefinition, Processing_ObjectDefinitionStatus
from gspread import Cell


class Controller_MDF_Object:

    def Fill_Worksheet(self, gspread_Sheet, Model_array_List, RowNumber):
        Cell_List = []

        for data_object in Model_array_List:
            Cell_List.append(Cell(row=RowNumber, col=1, value=data_object.item_id))
            Cell_List.append(Cell(row=RowNumber, col=2, value=data_object.Title))
            Cell_List.append(Cell(row=RowNumber, col=23, value=data_object.Title))
            Cell_List.append(Cell(row=RowNumber, col=3, value=data_object.Code))
            Cell_List.append(Cell(row=RowNumber, col=4, value=data_object.Effective_Dating))
            Cell_List.append(Cell(row=RowNumber, col=5, value=data_object.API_Visibility))
            Cell_List.append(Cell(row=RowNumber, col=6, value=data_object.Status))
            Cell_List.append(Cell(row=RowNumber, col=7, value=data_object.MDF_Version_History))
            Cell_List.append(Cell(row=RowNumber, col=8, value=data_object.Default_Screen))
            Cell_List.append(Cell(row=RowNumber, col=9, value=data_object.Label))
            Cell_List.append(Cell(row=RowNumber, col=10, value=data_object.Description))
            Cell_List.append(Cell(row=RowNumber, col=11, value=data_object.API_Sub_Version))
            Cell_List.append(Cell(row=RowNumber, col=12, value=data_object.Subject_User_Field))
            Cell_List.append(Cell(row=RowNumber, col=13, value=data_object.Workflow_Routing))
            Cell_List.append(Cell(row=RowNumber, col=14, value=data_object.Pending_Data))
            Cell_List.append(Cell(row=RowNumber, col=15, value=data_object.Todo_Category))
            Cell_List.append(Cell(row=RowNumber, col=16, value=data_object.Object_Category))
            Cell_List.append(Cell(row=RowNumber, col=17, value=data_object.Secured))
            Cell_List.append(Cell(row=RowNumber, col=18, value=data_object.Permission_Category))
            Cell_List.append(Cell(row=RowNumber, col=19, value=data_object.RBP_Subject_User_Field))
            Cell_List.append(Cell(row=RowNumber, col=20, value=data_object.CREATE_Respects_Target_Criteria))
            Cell_List.append(Cell(row=RowNumber, col=21, value=data_object.Base_Date_Field_For_Blocking))

        RowNumber += 1
        gspread_Sheet.update_cells(Cell_List)

    def LoadData(self, gspread_Sheet):
        Sheet_Records = gspread_Sheet.get_all_records()
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
            Object_Definition_model.Secured = record["Secured"]
            Object_Definition_model.Permission_Category = record["Permission Category"]
            Object_Definition_model.RBP_Subject_User_Field = record["RBP Subject User Field"]
            Object_Definition_model.CREATE_Respects_Target_Criteria = record["CREATE Respects Target Criteria"]
            Object_Definition_model.Base_Date_Field_For_Blocking = record["Base Date Field For Blocking"]
            data_list.append(Object_Definition_model)

            processing_status.item_id = record["Item ID"]
            processing_status.Object_Definition = record["Object Definition"]
            processing_status.Object_Definition_Status = record["Object Definition Status"]
            processing_list.append(processing_status)

        processing_heading = [obj.Object_Definition for obj in processing_list if obj.Object_Definition_Status == 'Pending']
        data_record = [a for a in data_list if a.Title in processing_heading]

        return data_record, processing_heading


class ValidationProps:
    Title = "B"
    Code = "C"
    Effective_Dating = "D"
    API_Visibility = "E"
    Status = "F"
    MDF_Version_History = "G"
    Default_Screen = "H"
    Label = "I"
    Description = "J"
    API_Sub_Version = "K"
    Subject_User_Field = "L"
    Workflow_Routing = "M"
    Pending_Data = "N"
    Todo_Category = "O"
    Object_Category = "P"
    Secured = "Q"
    Permission_Category = "R"
    RBP_Subject_User_Field = "S"
    CREATE_Respects_Target_Criteria = "T"
    Base_Date_Field_For_Blocking = "U"
