from login import login_instance
from SuccessionSettings.Controller_Succession_Settings import Controller_Succession_Settings, ValidationProps
import gspread
from gspread_formatting import *
import time

gc = gspread.service_account()
sheet = gc.open("Gspread")
Worksheet = sheet.worksheet("Succession Settings")


class TC_Validation_Succession_Settings:
    login_instance.login_method()
    driver = login_instance.driver
    hw = login_instance.hw
    Controller = Controller_Succession_Settings()
    LiveProfiles_model_list, Properties_model = Controller.Load_Data(gspread_Sheet=Worksheet)
    red = CellFormat(backgroundColor=Color(1, 0, 0))
    green = CellFormat(backgroundColor=Color(0, 1, 0))

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
        Cell_List = []
        for Object in objectlist:
            if self.hw.isElementPresent('//span[@class="important-focus-msg"]//div[text()="Object does not Exist Or No Permission"]', 'xpath'):
                Cell_List.append([f'{ValidationProps.Live_Profiles}:{ValidationProps.End_Date}', self.red])
                Cell_List.append([f'{ValidationProps.Usability}:{ValidationProps.Notification}', self.red])
                self.hw.Popup('//span[@class="important-focus-msg"]//div[text()="Object does not Exist Or No Permission"]', 'xpath')

            else:
                if Object == "LiveProfiles":
                    for LiveProfilemodel in self.LiveProfiles_model_list:
                        Liveprofiles_rownumber = LiveProfilemodel.item_id + 1
                        Live_Profiles = "//div[contains(@class, 'revolution_content')]//table[@cellpadding='5px']//tr//td[text()='{0}']"
                        Date = "//div[contains(@class, 'revolution_content')]//table[@cellpadding='5px']//tr[.//td[.='{0}']]//input[@value='{1}']"

                        if not self.hw.isElementPresent(Live_Profiles.format(LiveProfilemodel.Live_Profiles), 'xpath'):
                            Cell_List.append([f'{ValidationProps.Live_Profiles}{Liveprofiles_rownumber}', self.red])
                        else:
                            Cell_List.append([f'{ValidationProps.Live_Profiles}{Liveprofiles_rownumber}', self.green])

                        if not self.hw.isElementPresent(Date.format(LiveProfilemodel.Live_Profiles, LiveProfilemodel.Start_Date), 'xpath'):
                            Cell_List.append([f'{ValidationProps.Start_Date}{Liveprofiles_rownumber}', self.red])
                        else:
                            Cell_List.append([f'{ValidationProps.Start_Date}{Liveprofiles_rownumber}', self.green])

                        if not self.hw.isElementPresent(Date.format(LiveProfilemodel.Live_Profiles, LiveProfilemodel.End_Date), 'xpath'):
                            Cell_List.append([f'{ValidationProps.End_Date}{Liveprofiles_rownumber}', self.red])
                        else:
                            Cell_List.append([f'{ValidationProps.End_Date}{Liveprofiles_rownumber}', self.green])

                if Object == "Properties":
                    Properties_rownumber = self.Properties_model.item_id + 1
                    Check_box = "//div[contains(@class, 'revolution_content')]//table[@cellpadding='15px']//tr[.//td[.='{0}']]//input[@checked='checked']"
                    Check_box_2 = "//div[contains(@class, 'revolution_content')]//table[@cellpadding='15px']//tr[.//td[.='{0}']]//input[.='{1}']"

                    if self.Properties_model.Usability == '':
                        if not self.hw.isElementPresent(Check_box_2.format("Usability", self.Properties_model.Usability), 'xpath'):
                            Cell_List.append([f'{ValidationProps.Usability}{Properties_rownumber}', self.red])
                        else:
                            Cell_List.append([f'{ValidationProps.Usability}{Properties_rownumber}', self.green])
                    else:
                        if not self.hw.isElementPresent(Check_box.format("Usability"), 'xpath'):
                            Cell_List.append([f'{ValidationProps.Usability}{Properties_rownumber}', self.red])
                        else:
                            Cell_List.append([f'{ValidationProps.Usability}{Properties_rownumber}', self.green])

                    if self.Properties_model.Position_Tile_View == '':
                        if not self.hw.isElementPresent(Check_box_2.format("Position Tile View", self.Properties_model.Position_Tile_View), 'xpath'):
                            Cell_List.append([f'{ValidationProps.Position_Tile_View}{Properties_rownumber}', self.red])
                        else:
                            Cell_List.append([f'{ValidationProps.Position_Tile_View}{Properties_rownumber}', self.green])
                    else:
                        if not self.hw.isElementPresent(Check_box.format("Position Tile View"), 'xpath'):
                            Cell_List.append([f'{ValidationProps.Position_Tile_View}{Properties_rownumber}', self.red])
                        else:
                            Cell_List.append([f'{ValidationProps.Position_Tile_View}{Properties_rownumber}', self.green])

                    if self.Properties_model.Notification == '':
                        if not self.hw.isElementPresent(Check_box_2.format("Notification", self.Properties_model.Notification), 'xpath'):
                            Cell_List.append([f'{ValidationProps.Notification}{Properties_rownumber}', self.red])
                        else:
                            Cell_List.append([f'{ValidationProps.Notification}{Properties_rownumber}', self.green])
                    else:
                        if not self.hw.isElementPresent(Check_box.format("Notification"), 'xpath'):
                            Cell_List.append([f'{ValidationProps.Notification}{Properties_rownumber}', self.red])
                        else:
                            Cell_List.append([f'{ValidationProps.Notification}{Properties_rownumber}', self.green])

        format_cell_ranges(Worksheet, Cell_List)


Succession_Settings_class = TC_Validation_Succession_Settings()
Succession_Settings_class.ExecuteProcess()
