from SuccessionSettings.TC_Model_Succession_Settings import Model_LiveProfiles, Model_Properties
from gspread import Cell


class Controller_Succession_Settings:

    def Fill_Worksheet_LiveProfiles(self, gspread_Sheet, Model_array_List, RowNumber):
        Cell_List = []

        for LiveProfiles_obj in Model_array_List:
            Cell_List.append(Cell(row=LiveProfiles_obj.item_id + RowNumber, col=1,
                                  value=LiveProfiles_obj.item_id))
            Cell_List.append(Cell(row=LiveProfiles_obj.item_id + RowNumber, col=2,
                                  value=LiveProfiles_obj.Live_Profiles))
            Cell_List.append(Cell(row=LiveProfiles_obj.item_id + RowNumber, col=3,
                                  value=LiveProfiles_obj.Start_Date))
            Cell_List.append(Cell(row=LiveProfiles_obj.item_id + RowNumber, col=4,
                                  value=LiveProfiles_obj.End_Date))

        gspread_Sheet.update_cells(Cell_List)

    def Fill_Worksheet_Properties(self, gspread_Sheet, Model_array_List, RowNumber):
        Cell_List = []

        for Properties_obj in Model_array_List:
            Cell_List.append(Cell(row=RowNumber, col=6, value=Properties_obj.Usability))
            Cell_List.append(Cell(row=RowNumber, col=7, value=Properties_obj.Position_Tile_View))
            Cell_List.append(Cell(row=RowNumber, col=8, value=Properties_obj.Notification))

        gspread_Sheet.update_cells(Cell_List)

    def Load_Data(self, gspread_Sheet):
        Sheet_Records = gspread_Sheet.get_all_records()
        LiveProfiles_model_list = []
        Properties_model = Model_Properties()

        for record in Sheet_Records:
            LiveProfilesSection_model = Model_LiveProfiles()

            LiveProfilesSection_model.item_id = record["Item ID"]
            LiveProfilesSection_model.Live_Profiles = record["Live Profiles"]
            LiveProfilesSection_model.Start_Date = record["Start Date"]
            LiveProfilesSection_model.End_Date = record["End Date"]
            LiveProfiles_model_list.append(LiveProfilesSection_model)

            if LiveProfilesSection_model.item_id == 1:
                Properties_model.item_id = record["Item ID"]
                Properties_model.Usability = record["Usability"]
                Properties_model.Position_Tile_View = record["Position Tile View"]
                Properties_model.Notification = record["Notification"]

        return LiveProfiles_model_list, Properties_model


class ValidationProps:
    Live_Profiles = "B"
    Start_Date = "C"
    End_Date = "D"
    Usability = "F"
    Position_Tile_View = "G"
    Notification = "H"
