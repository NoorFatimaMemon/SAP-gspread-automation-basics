# To send data of configure object definition values to the gspread
import time
from gspread_formatting import *
import gspread
from SAP_CODs_Task2 import CODelements_to_gspread


class CODGspread_Task3:

    def COD_gspread_Task3(self):
        gc = gspread.service_account()
        sh = gc.open("Gspread-Task 1")
        wks = sh.worksheet("COD")

        wks.format("A1:P1",
                   {"backgroundColor": {"red": 100, "green": 64.7, "blue": 0.0}, "horizontalAlignment": "CENTER",
                    "textFormat": {"fontSize": 10, "bold": True}})

        # for separator
        wks.format("Q", {"backgroundColor": {"red": 0, "green": 0, "blue": 0}})

        wks.format("R1:S1",
                   {"backgroundColor": {"red": 100, "green": 64.7, "blue": 0.0}, "horizontalAlignment": "CENTER",
                    "textFormat": {"fontSize": 10, "bold": True}})

        # creating status column
        validation_rule = DataValidationRule(BooleanCondition('ONE_OF_LIST', ['Pending', 'Processed']),
                                             showCustomUi=True)
        set_data_validation_for_cell_range(wks, 'S2:S6', validation_rule)

        itemid_num = 1
        starting_row = 2
        CODtitles_row = 2
        CODtitles = []
        RS_columns_rows = 2

        elements_keys = list(COD_data[0].keys())
        wks.batch_update([{'range': f'A1:P1', 'values': [elements_keys]}])
        wks.update_cell(1, 18, "Object Definition")
        wks.update_cell(1, 19, "Object Definition Status")

        for elements in COD_data:
            elements_values = list(elements.values())
            wks.batch_update([{'range': f'A{starting_row}:P{starting_row}', 'values': [elements_values]}])
            title = elements_values[1]
            if title not in CODtitles:
                CODtitles.append(title)
                wks.update_cell(CODtitles_row, 18, title)  # updating unique title
                wks.update_cell(CODtitles_row, 19, 'Pending')        # updating unique title's status as pending
                CODtitles_row = CODtitles_row + 1
                Object_Definitions = wks.get(f'R{RS_columns_rows}')
                for object_definition in Object_Definitions:
                    if object_definition[0] != title:
                        wks.update(f'S{RS_columns_rows}', 'Processed')     # updating unique title's status as Processed
                        RS_columns_rows = RS_columns_rows + 1
                    else:
                        pass
            else:
                pass
            itemid_num = itemid_num + 1
            starting_row = starting_row + 1
            time.sleep(1)

        wks.update_cell(6, 19, 'Processed')


COD_data = CODelements_to_gspread.SAPCOD_task_2()
COD_Gsheet = CODGspread_Task3()
COD_Gsheet.COD_gspread_Task3()
