from selenium import webdriver
from Utilities.HandyWrappers import HandyWrappers
import gspread
import time


class Gspread_Task3:
    sourcelink = 'https://www.w3schools.com/python/default.asp'
    driver = webdriver.Chrome()
    hw = HandyWrappers(driver)
    driver.get(sourcelink)
    # driver.implicitly_wait(1)

    def gspreadTask3(self):
        gc = gspread.service_account()
        sh = gc.open("Gspread-Task 1")
        wks = sh.worksheet("Gspread-Task 1")

        sheet_data = wks.get("B2:D51")
        dropdown_values = wks.get("G2:G")
        headings = wks.get("B2:B")

        for dropdown_value in dropdown_values:
            if dropdown_value[0] == 'Pending':
                idx_1 = dropdown_values.index(dropdown_value)
                f_column_pending_value = wks.get(f"F{idx_1 + 2}")
                [[heading_value]] = f_column_pending_value
                heading_value_index = headings.index([heading_value])
                idx_2 = heading_value_index + 2
                new_list = []

                for data in sheet_data:
                    [heading, subheading, link] = data
                    if heading == heading_value:
                        heading_check = self.hw.GetElement(f'//h5[text()="{heading}"]', 'xpath')
                        if heading_check is None:
                            wks.format(f'B{idx_2}', {"backgroundColor": {"red": 1, "green": 0, "blue": 0}})
                            new_list.append(heading_check)
                        else:
                            wks.format(f'B{idx_2}', {"backgroundColor": {"red": 0, "green": 1, "blue": 0}})

                        subheading_check = self.hw.GetElement(f'//a[text()="{subheading}"]', 'xpath')
                        if subheading_check is None:
                            wks.format(f'C{idx_2}', {"backgroundColor": {"red": 1, "green": 0, "blue": 0}})
                            new_list.append(subheading_check)
                        else:
                            wks.format(f'C{idx_2}', {"backgroundColor": {"red": 0, "green": 1, "blue": 0}})

                        link_check = self.hw.GetElement(
                            f'//a[contains(text(),"{subheading}") and contains(@href,"{link}")]', 'xpath')
                        try:
                            new_link = "www.w3schools.com".split(link_check)
                            new_list.append(new_link)
                        except:
                            new_link = link_check

                        if new_link is None:
                            wks.format(f'D{idx_2}', {"backgroundColor": {"red": 1, "green": 0, "blue": 0}})
                            new_list.append(new_link)
                        else:
                            wks.format(f'D{idx_2}', {"backgroundColor": {"red": 0, "green": 1, "blue": 0}})
                        idx_2 = idx_2 + 1
                else:
                    pass
                time.sleep(1)
                wks.update(f"G{idx_1 + 2}", 'Processed')


test = Gspread_Task3()
test.gspreadTask3()
