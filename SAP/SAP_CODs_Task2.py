# To get data of configure object definition like AbsencePayPolicy values
from login import login_instance
import time
from SAP_CODs_Task1b import SAPCOD_Task1


class SAPCOD_Task2:
    login_instance.login_method()
    driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
    hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance

    def Executeprocess(self):
        link_1 = self.driver.current_url
        link_1_split = link_1.split('s.crb=')
        link_2 = "https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=2K8CkVQJqWwL%2brEcUnCDHjVd%2fb%2fqqmVKOrsyYQk9p7E%3d"
        link_2_split = link_2.split("s.crb=")
        COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1]
        self.driver.get(COD_Link)
        time.sleep(5)

        self.hw.ClickElement('//span[@id="19__write_toggle"]', 'xpath')         # to click no search dropdown
        time.sleep(5)
        self.hw.ClickElement('//a[@title="Object Definition"]', 'xpath')         # to click object definition
        time.sleep(5)
        """self.hw.ClickElement('//span[@id="9__write_toggle"]', 'xpath')         # to click no selection dropdown
        time.sleep(5)"""

        _obj_Srch_Field = "//table[@class='MDFSearchBar']//tr//td[contains(text(),'Search')]/following-sibling::td[1]/span[3]//input"

        searchBox_id = str(self.hw.GetElementAttribute(_obj_Srch_Field, 'xpath', 'id')).split("__")[0] + "_"

        self.driver.execute_script("ECTUtil.getComponentById('" + searchBox_id + "')._model._searchFields.pageSize = 2000")

        objects_list_dict = self.driver.execute_script("return ECTUtil.getComponentById('" + searchBox_id + "')._model._searchDAO._staticData.results;")

    def SAPCOD_task_2(self):
        link_1 = self.driver.current_url
        link_1_split = link_1.split('s.crb=')
        COD_data = []
        Item_ID = 1

        for element in COD_elements[:5]:
            link_2 = f"https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=J74wSY%2fbBYLLOtmmiPHIU28YdKC%2bPsiT3awOLDacaPE%3d#c=1&t=GOObjectDefinition&i={element}"
            link_2_split = link_2.split("s.crb=")
            COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1] + f"&t=GOObjectDefinition&i={element}"
            self.driver.get(COD_Link)
            time.sleep(5)
            object_definition = self.hw.GetElementText('//span[@class="pwhHeaderTitle globalHumanistText"]', 'xpath')
            object_definition_p1 = object_definition.split('(')
            object_definition_p2 = object_definition_p1[0].split(':')
            object_definition_p3 = object_definition_p2[1].strip()
            data = {}

            for i in range(1, 15):
                data["Item ID"] = Item_ID
                data["Title"] = object_definition_p3
                COD_data_key = self.hw.GetElementText(f'(//td[@class="field_label"]//span[@class="text"])[{i}]', 'xpath')
                COD_data_value = self.hw.GetElementText(f'(//td[@class="field_value"])[{i}]', 'xpath')
                data.update({COD_data_key: COD_data_value})

            Item_ID = Item_ID + 1
            COD_data.append(data)

        print(COD_data)
        return COD_data


COD1_elements = SAPCOD_Task1()
COD_elements = COD1_elements.SAPCOD_task_1()
CODelements_to_gspread = SAPCOD_Task2()
"""CODelements_to_gspread.SAPCOD_task_2()"""

