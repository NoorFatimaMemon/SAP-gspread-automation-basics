import time
from selenium import webdriver
from Utilities.HandyWrappers import HandyWrappers
import gspread

gc = gspread.service_account()
sh = gc.open("Gspread-Task 1")
wks = sh.worksheet("Gspread-Task 1")


class Model_Reference:
    item_id = ""
    Heading = ""
    SubHeading = ""
    Link = ""


class Processing_status:
    item_id = ""
    unique_Heading = ""
    Status = ""


def model():
    model_reference = Model_Reference()
    processing_status = Processing_status()

    list_of_dicts = wks.get_all_records()
    processing_list = []
    data_list = []

    for i in list_of_dicts:
        model_reference.item_id = i["Item ID"]
        model_reference.Heading = i["Headings"]
        model_reference.SubHeading = i["Subheadings"]
        model_reference.Link = i["Links"]
        data_list.append(
            [model_reference.item_id, model_reference.Heading, model_reference.SubHeading, model_reference.Link])

        processing_status.item_id = i["Item ID"]
        processing_status.unique_Heading = i["Unique_Headings"]
        processing_status.Status = i["Status"]
        processing_list.append([processing_status.item_id, processing_status.unique_Heading, processing_status.Status])

    processing_heading = [o[1] for o in processing_list if o[2] == 'Pending']
    data_record = []
    for a in data_list:
        if a[1] in processing_heading:
            data_record.append(a)

    return data_record, processing_heading


class Gspread_Task3:
    sourcelink = 'https://www.w3schools.com/python/default.asp'
    driver = webdriver.Chrome()
    hw = HandyWrappers(driver)
    driver.get(sourcelink)

    def gspreadTask3(self):
        data_record, processing_heading = model()
        invalid_cell_format = {"backgroundColor": {"red": 1, "green": 0, "blue": 0}}
        valid_cell_format = {"backgroundColor": {"red": 0, "green": 1, "blue": 0}}

        unique_headings_row = 2
        unique_headings_list = []
        fg_columns_rows = 2

        for data in data_record:
            [ID, heading, subheading, link] = data

            heading_check = self.hw.GetElement(f'//h5[.="{heading}"]', 'xpath')
            if heading_check is None:
                wks.format(f'B{ID + 1}', invalid_cell_format)
            else:
                wks.format(f'B{ID + 1}', valid_cell_format)

            if heading not in unique_headings_list:
                unique_headings_list.append(heading)
                unique_headings_row = unique_headings_row + 1
                unique_headings = wks.get(f'F{fg_columns_rows}')
                for unique_heading in unique_headings:
                    if unique_heading[0] != heading:
                        wks.update(f'G{fg_columns_rows}', 'Processed')
                        fg_columns_rows = fg_columns_rows + 1
                    else:
                        pass

            subheading_check = self.hw.GetElement(f'//h5[.="{heading}"]//parent::*//parent::div//a[.="{subheading}"]',
                                                  'xpath')
            if subheading_check is None:
                wks.format(f'C{ID + 1}', invalid_cell_format)
            else:
                wks.format(f'C{ID + 1}', valid_cell_format)

            try:
                string_link = link.replace('https://www.w3schools.com', '')
            except:
                string_link = link

            link_check = self.hw.GetElement(f'//h5[.="{heading}"]//parent::*//parent::div//a[@href="{string_link}"]',
                                            'xpath')
            if link_check is None:
                wks.format(f'D{ID + 1}', invalid_cell_format)
            else:
                wks.format(f'D{ID + 1}', valid_cell_format)

            time.sleep(2)

        wks.update(f'G{fg_columns_rows}', 'Processed')

        last_Status = wks.find('Pending', in_column=9)
        cell_last_status = last_Status.row
        wks.update(f'I{cell_last_status}', 'Processed')


test = Gspread_Task3()
test.gspreadTask3()
