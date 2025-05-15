import time
from Utilities.Task_4 import Task4
from gspread_formatting import *
import gspread


class Gspread_Task1:

    def gspreadTask1(self):
        gc = gspread.service_account()
        sh = gc.open("Gspread-Task 1")
        wks = sh.worksheet("Gspread-Task 1")

        # creating titles
        wks.update_cell(1, 1, "Item ID")
        wks.update_cell(1, 2, "Headings")
        wks.update_cell(1, 3, "Subheadings")
        wks.update_cell(1, 4, "Links")
        wks.update_cell(1, 6, "Unique_Headings")
        wks.update_cell(1, 7, "Status")

        wks.format("A1:D1",
                   {"backgroundColor": {"red": 100, "green": 64.7, "blue": 0.0}, "horizontalAlignment": "CENTER",
                    "textFormat": {"fontSize": 10, "bold": True}})

        wks.format("F1:Z1",
                   {"backgroundColor": {"red": 100, "green": 64.7, "blue": 0.0}, "horizontalAlignment": "CENTER",
                    "textFormat": {"fontSize": 10, "bold": True}})

        # for separator
        wks.format("E", {"backgroundColor": {"red": 0, "green": 0, "blue": 0}})

        # creating status column
        validation_rule = DataValidationRule(BooleanCondition('ONE_OF_LIST', ['Pending', 'Processed']),
                                             showCustomUi=True)
        set_data_validation_for_cell_range(wks, 'G2:G5', validation_rule)

        id_num = 1
        starting_row = 2
        unique_headings_row = 2
        unique_headings_list = []
        fg_columns_rows = 2

        for element in task4Elements:
            wks.batch_update([{'range': f'A{starting_row}', 'values': [[id_num]]}, {'range': f'B{starting_row}:D{starting_row}', 'values': [element]}])
            if element[0] not in unique_headings_list:
                unique_headings_list.append(element[0])
                wks.update_cell(unique_headings_row, 6, element[0])  # updating unique headings
                wks.update_cell(unique_headings_row, 7, 'Pending')
                unique_headings_row = unique_headings_row + 1
                unique_headings = wks.get(f'F{fg_columns_rows}')
                for unique_heading in unique_headings:
                    if unique_heading[0] != element[0]:
                        wks.update(f'G{fg_columns_rows}', 'Processed')
                        fg_columns_rows = fg_columns_rows + 1
                    else:
                        pass
            else:
                pass
            id_num = id_num + 1
            starting_row = starting_row + 1
            time.sleep(1)

        wks.update_cell(5, 7, 'Processed')


Task_4 = Task4()
task4Elements = Task_4.task_4()
test = Gspread_Task1()
test.gspreadTask1()
