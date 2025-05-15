# To get data of configure object definitions dropdown values
from login import login_instance
import time


class SAPCOD_Task1:
    login_instance.login_method()
    driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
    hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance

    def SAPCOD_task_1(self):
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

        object_id_list = []
        for key in objects_list_dict:
            object_id_list.append(key['code'])

        # print(object_id_list)
        return object_id_list
