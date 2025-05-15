from login import login_instance
from SuccessionSettings.TC_Model_Succession_Settings import Model_LiveProfiles, Model_Properties
from SuccessionSettings.Controller_Succession_Settings import Controller_Succession_Settings
import gspread
import time

gc = gspread.service_account()
sheet = gc.open("Gspread")
Worksheet = sheet.worksheet("Succession Settings")

login_instance.login_method()
driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance


class TC_Rev_Succession_Settings:
    RowNumber = 1

    def ExecuteProcess(self):
        link_1 = driver.current_url
        link_1_split = link_1.split('s.crb=')
        link_2 = "https://pmsalesdemo8.successfactors.com/acme?fbacme_o=admin&pess_old_admin=true&ap_param_action=succession_settings&itrModule=talent&_s.crb=9uGWwNWvwqfaIqVFqy1HHmhVSrOLfOht5kPUsObB4Y4%3d"
        link_2_split = link_2.split("s.crb=")
        time.sleep(2)
        COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1]
        driver.get(COD_Link)
        time.sleep(3)
        objectlist = ["LiveProfiles", "Properties"]
        self.ProcessObject(objectlist)

    def ProcessObject(self, objectlist):
        obj_LiveProfiles_list = []
        obj_Properties_list = []
        for Object in objectlist:
            if Object == "LiveProfiles":
                LiveProfiles = "//div[contains(@class, 'revolution_content')]//table[@cellpadding='15px']//tr//td//table//tr"
                LiveProfiles_list = hw.GetElementlistofText(LiveProfiles, 'xpath')
                Date = "(//div[contains(@class, 'revolution_content')]//table[@cellpadding='5px']//tr[.//td[.='{0}']]//input)[{1}]"
                for LiveProfile in LiveProfiles_list:
                    obj = Model_LiveProfiles()
                    self.RowNumber = self.RowNumber + 1
                    obj.item_id = self.RowNumber - 1
                    obj.Live_Profiles = LiveProfile
                    obj.Start_Date = hw.GetElementAttribute(Date.format(LiveProfile, "1"), 'xpath', 'value')
                    obj.End_Date = hw.GetElementAttribute(Date.format(LiveProfile, "2"), 'xpath', 'value')
                    obj_LiveProfiles_list.append(obj)

            if Object == "Properties":
                Check_box = "//div[contains(@class, 'revolution_content')]//table[@cellpadding='15px']//tr[.//td[.='{0}']]//input"
                obj_2 = Model_Properties()
                obj_2.item_id = 1
                obj_2.Usability = hw.GetElementAttribute(Check_box.format("Usability"), 'xpath', 'checked')
                obj_2.Position_Tile_View = hw.GetElementAttribute(Check_box.format("Position Tile View"), 'xpath', 'checked')
                obj_2.Notification = hw.GetElementAttribute(Check_box.format("Notification"), 'xpath', 'checked')
                obj_Properties_list.append(obj_2)

        Controller = Controller_Succession_Settings()
        Controller.Fill_Worksheet_LiveProfiles(gspread_Sheet=Worksheet, Model_array_List=obj_LiveProfiles_list, RowNumber=1)
        Controller.Fill_Worksheet_Properties(gspread_Sheet=Worksheet, Model_array_List=obj_Properties_list, RowNumber=2)


SuccessionSettings_Class = TC_Rev_Succession_Settings()
SuccessionSettings_Class.ExecuteProcess()
