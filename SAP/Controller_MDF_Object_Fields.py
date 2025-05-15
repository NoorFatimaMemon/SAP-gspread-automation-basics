from TC_Model_MDF_Object_Fields import Model_ObjectDefinitionFields, Processing_ObjectDefinitionFieldsStatus
from gspread import Cell


class Controller_MDF_Object_Fields:

    def Fill_Worksheet(self, gspread_Sheet, Model_array_List, RowNumber):
        Cell_List = []

        for field_data_object in Model_array_List:
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=1, value=field_data_object.item_id))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=2, value=field_data_object.Code))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=3, value=field_data_object.Name))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=4, value=field_data_object.Database_Field_Name))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=5, value=field_data_object.Maximum_Length))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=6, value=field_data_object.Data_Type))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=7, value=field_data_object.Valid_Values_Source))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=8, value=field_data_object.Hide_Old_Value))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=9, value=field_data_object.Decimal_Precision))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=10, value=field_data_object.Include_Inactive_Users))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=11, value=field_data_object.UI_Field_Renderer))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=12, value=field_data_object.Transient))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=13, value=field_data_object.Help_Text))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=14, value=field_data_object.Mask_Value_on_UI))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=15, value=field_data_object.Show_Trailing_Zeros))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=16, value=field_data_object.Default_Value))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=17, value=field_data_object.Hide_Seconds))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=18, value=field_data_object.Required))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=19, value=field_data_object.Visibility))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=20, value=field_data_object.Status))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=21, value=field_data_object.Label))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=22, value=field_data_object.Cascade))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=23, value=field_data_object.Inactivated_By))
            Cell_List.append(Cell(row=field_data_object.item_id+RowNumber, col=24, value=field_data_object.End_Of_Period))

        gspread_Sheet.update_cells(Cell_List)

    def Fill_Worksheet_Sec2(self, gspread_Sheet, Model_array_List, RowNumber):
        uniqueCell_List = []

        for field_data_object in Model_array_List:
            uniqueCell_List.append(Cell(row=RowNumber, col=26, value=field_data_object.Code))
            uniqueCell_List.append(Cell(row=RowNumber, col=27, value="Processed"))

        gspread_Sheet.update_cells(uniqueCell_List)

    def Load_Data(self, gspread_Sheet):
        Sheet_Records = gspread_Sheet.get_all_records()
        processing_list = []
        data_list = []

        for record in Sheet_Records:
            Object_Definition_Fields_model = Model_ObjectDefinitionFields()
            processing_status = Processing_ObjectDefinitionFieldsStatus()

            Object_Definition_Fields_model.item_id = record["Item ID"]
            Object_Definition_Fields_model.Code = record["Code"]
            Object_Definition_Fields_model.Name = record["Name"]
            Object_Definition_Fields_model.Database_Field_Name = record["Database Field Name"]
            Object_Definition_Fields_model.Maximum_Length = record["Maximum Length"]
            Object_Definition_Fields_model.Data_Type = record["Data Type"]
            Object_Definition_Fields_model.Valid_Values_Source = record["Valid Values Source"]
            Object_Definition_Fields_model.Hide_Old_Value = record["Hide Old Value"]
            Object_Definition_Fields_model.Decimal_Precision = record["Decimal Precision"]
            Object_Definition_Fields_model.Include_Inactive_Users = record["Include Inactive Users"]
            Object_Definition_Fields_model.UI_Field_Renderer = record["UI Field Renderer"]
            Object_Definition_Fields_model.Transient = record["Transient"]
            Object_Definition_Fields_model.Help_Text = record["Help Text"]
            Object_Definition_Fields_model.Mask_Value_on_UI = record["Mask Value on UI"]
            Object_Definition_Fields_model.Show_Trailing_Zeros = record["Show Trailing Zeros"]
            Object_Definition_Fields_model.Default_Value = record["Default Value"]
            Object_Definition_Fields_model.Hide_Seconds = record["Hide Seconds"]
            Object_Definition_Fields_model.Required = record["Required"]
            Object_Definition_Fields_model.Visibility = record["Visibility"]
            Object_Definition_Fields_model.Status = record["Status"]
            Object_Definition_Fields_model.Label = record["Label"]
            Object_Definition_Fields_model.Cascade = record["Cascade"]
            Object_Definition_Fields_model.Inactivated_By = record["Inactivated By"]
            Object_Definition_Fields_model.End_Of_Period = record["End Of Period"]
            data_list.append(Object_Definition_Fields_model)

            processing_status.item_id = record["Item ID"]
            processing_status.Unique_Code = record["Unique Code"]
            processing_status.Processing_Status = record["Processing Status"]
            processing_list.append(processing_status)

        processing_heading = [obj.Unique_Code for obj in processing_list if obj.Processing_Status == 'Pending']
        data_record = [a for a in data_list if a.Code in processing_heading]

        return data_record, processing_heading


class ValidationProps:
    Code = "B"
    Name = "C"
    Database_Field_Name = "D"
    Maximum_Length = "E"
    Data_Type = "F"
    Valid_Values_Source = "G"
    Hide_Old_Value = "H"
    Decimal_Precision = "I"
    Include_Inactive_Users = "J"
    UI_Field_Renderer = "K"
    Transient = "L"
    Help_Text = "M"
    Mask_Value_on_UI = "N"
    Show_Trailing_Zeros = "O"
    Default_Value = "P"
    Hide_Seconds = "Q"
    Required = "R"
    Visibility = "S"
    Status = "T"
    Label = "U"
    Cascade = "V"
    Inactivated_By = "W"
    End_Of_Period = "X"
