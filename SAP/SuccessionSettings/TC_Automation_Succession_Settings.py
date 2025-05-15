from login import login_instance
from SuccessionSettings.Controller_Succession_Settings import Controller_Succession_Settings
import gspread
import time

gc = gspread.service_account()
sheet = gc.open("Gspread")
Worksheet = sheet.worksheet("Succession Settings")


class TC_Automation_Succession_Settings:
    login_instance.login_method()
    driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
    hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance
    Controller = Controller_Succession_Settings()
    LiveProfiles_model_list, Properties_model = Controller.Load_Data(gspread_Sheet=Worksheet)

    def ExecuteProcess(self):
        link_1 = self.driver.current_url
        link_1_split = link_1.split('s.crb=')
        link_2 = "https://pmsalesdemo8.successfactors.com/acme?fbacme_o=admin&pess_old_admin=true&ap_param_action=succession_settings&itrModule=talent&_s.crb=9uGWwNWvwqfaIqVFqy1HHmhVSrOLfOht5kPUsObB4Y4%3d"
        link_2_split = link_2.split("s.crb=")
        COD_Link = link_2_split[0] + "s.crb=" + link_1_split[1]
        self.driver.get(COD_Link)
        time.sleep(3)
        objectlist = ["LiveProfiles", "Properties"]
        self.ProcessObject(objectlist)

    def ProcessObject(self, objectlist):
        for Object in objectlist:
            if Object == "LiveProfiles":
                for LiveProfilemodel in self.LiveProfiles_model_list:
                    date = "(//div[contains(@class, 'revolution_content')]//table[@cellpadding='5px']//tr[.//td[.='{0}']]//input)[{1}]"
                    self.hw.FillField(date.format(LiveProfilemodel.Live_Profiles, "1"), 'xpath', 'value', f'{LiveProfilemodel.Start_Date}')
                    self.hw.FillField(date.format(LiveProfilemodel.Live_Profiles, "2"), 'xpath', 'value', f'{LiveProfilemodel.End_Date}')

            if Object == "Properties":
                check_box = "//div[contains(@class, 'revolution_content')]//table[@cellpadding='15px']//tr[.//td[.='{0}']]//input"
                self.hw.CheckBox(checkboxpath=check_box.format('Usability'), desiredvalue=self.Properties_model.Usability)
                self.hw.CheckBox(checkboxpath=check_box.format('Position Tile View'), desiredvalue=self.Properties_model.Position_Tile_View)
                self.hw.CheckBox(checkboxpath=check_box.format('Notification'), desiredvalue=self.Properties_model.Notification)

        self.hw.ClickElement('//button[@id="save_btn"]', 'xpath')
        time.sleep(5)


Succession_Settings_class = TC_Automation_Succession_Settings()
Succession_Settings_class.ExecuteProcess()
