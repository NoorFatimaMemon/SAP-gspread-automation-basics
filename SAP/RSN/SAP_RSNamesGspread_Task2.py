# To send data of rating scale names, description, score, score label and score description to the gspread
import time
from gspread_formatting import *
import gspread
from SAP.RSN.SAP_RSNames_Task1 import SAPTask1_2_3


class SAPGspread_Task1:

    def SAPgspreadTask1(self):
        gc = gspread.service_account()
        sh = gc.open("Gspread-Task 1")
        wks = sh.worksheet("SAP")

        # creating titles
        wks.update_cell(1, 1, "Item ID")
        wks.update_cell(1, 2, "Scale Name")
        wks.update_cell(1, 3, "Scale Description")
        wks.update_cell(1, 4, "Score")
        wks.update_cell(1, 5, "Score Label")
        wks.update_cell(1, 6, "Score Description")
        wks.update_cell(1, 8, "Rating Scale Name")
        wks.update_cell(1, 9, "Scale Status")

        wks.format("A1:I1",
                   {"backgroundColor": {"red": 100, "green": 64.7, "blue": 0.0}, "horizontalAlignment": "CENTER",
                    "textFormat": {"fontSize": 10, "bold": True}})

        # for separator
        wks.format("G", {"backgroundColor": {"red": 0, "green": 0, "blue": 0}})

        # creating status column
        validation_rule = DataValidationRule(BooleanCondition('ONE_OF_LIST', ['Pending', 'Processed']),
                                             showCustomUi=True)
        set_data_validation_for_cell_range(wks, 'I2:I16', validation_rule)

        itemid_num = 1
        starting_row = 2
        unique_ratingscales_row = 2
        unique_ratingscales = []
        HI_columns_rows = 2

        for elements in SAPtask3Elements.values():
            for element in elements:
                wks.batch_update([{'range': f'A{starting_row}', 'values': [[itemid_num]]}, {'range': f'B{starting_row}:F{starting_row}', 'values': [element]}])
                if element[0] not in unique_ratingscales:
                    unique_ratingscales.append(element[0])
                    wks.update_cell(unique_ratingscales_row, 8, element[0])  # updating unique headings
                    wks.update_cell(unique_ratingscales_row, 9, 'Pending')
                    unique_ratingscales_row = unique_ratingscales_row + 1
                    unique_headings = wks.get(f'H{HI_columns_rows}')
                    for unique_heading in unique_headings:
                        if unique_heading[0] != element[0]:
                            wks.update(f'I{HI_columns_rows}', 'Processed')
                            HI_columns_rows = HI_columns_rows + 1
                        else:
                            pass
                else:
                    pass
                itemid_num = itemid_num + 1
                starting_row = starting_row + 1
                time.sleep(1)
            time.sleep(3)

        wks.update_cell(16, 9, 'Processed')


SAPTasks = SAPTask1_2_3()
SAPtask3Elements = SAPTasks.SAPTask1_2_3()
test = SAPGspread_Task1()
test.SAPgspreadTask1()
