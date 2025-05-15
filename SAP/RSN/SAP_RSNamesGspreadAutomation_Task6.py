"""To change the data of rating scale names, description, score, score label and score description from gspread
to the instance (if any rating scale or score is not present then add those)"""
from SAP.login import login_instance
import gspread
import time

gc = gspread.service_account()
sh = gc.open("Gspread-Task 1")
wks = sh.worksheet("SAP")


class Model_RatingScale:
    Scale_Name = ""
    Scale_Description = ""
    Score = ""
    Score_Label = ""
    Score_Description = ""


class Processing_ScaleStatus:
    Rating_Scale_Name = ""
    Scale_Status = ""


def model_controller():
    Sheet_Records = wks.get_all_records()
    processing_list = []
    data_list = []

    for record in Sheet_Records:
        rating_scale_model = Model_RatingScale()
        processing_status = Processing_ScaleStatus()

        rating_scale_model.Scale_Name = record["Scale Name"]
        rating_scale_model.Scale_Description = record["Scale Description"]
        rating_scale_model.Score = record["Score"]
        rating_scale_model.Score_Label = record["Score Label"]
        rating_scale_model.Score_Description = record["Score Description"]
        data_list.append(rating_scale_model)

        processing_status.Rating_Scale_Name = record["Rating Scale Name"]
        processing_status.Scale_Status = record["Scale Status"]
        processing_list.append(processing_status)

    processing_heading = [obj.Rating_Scale_Name for obj in processing_list if obj.Scale_Status == 'Pending']
    data_record = [a for a in data_list if a.Scale_Name in processing_heading]

    return data_record, processing_heading


class Main:
    login_instance.login_method()
    driver = login_instance.driver  # Access the existing login_instance's WebDriver instance
    hw = login_instance.hw  # Access the existing login_instance's HandyWrappers instance

    link_1 = driver.current_url
    link_1_split = link_1.split('s.crb=')
    link_2 = "https://pmsalesdemo8.successfactors.com/acme?fbacme_o=admin&pess_old_admin=true&ap_param_action=form_rating_scale&itrModule=talent&_s.crb=A38Sok%2bYiCF0lB2TAi758Nnvn7SlJWGMVsXzGt3gmCc%3d"
    link_2_split = link_2.split("s.crb=")
    Rating_Scale_Link = link_2_split[0] + "s.crb=" + link_1_split[1]
    driver.get(Rating_Scale_Link)
    time.sleep(5)

    data_record, processing_heading, = model_controller()

    def ExecuteProcess(self):
        for SN in self.processing_heading:
            self.ProcessObject(Object_name=SN)

    def ProcessObject(self, Object_name):
        ScaleName_check = self.hw.isElementPresent(f'//a[.="{Object_name}"]', 'xpath')
        ScaleDescription = self.data_record[0].Scale_Description

        if ScaleName_check is False:
            self.hw.ClickElement('//*[@id="17:_label"]/span', 'xpath')  # to create a new rating scale
            time.sleep(1)

            self.hw.ClickElement('//input[@id="53:_item_3"]', 'xpath')  # to click on Build your own
            self.hw.ClickElement('//button[text()="OK"]', 'xpath')  # to click ok
            time.sleep(1)

            self.hw.FillField_2(f'//input[@id="48:_txtFld"]', 'xpath', f'{Object_name}')  # to fill rating scale name

            self.hw.FillField_2(f'//textarea[@id="50:_txtArea"]', 'xpath',
                              f'{ScaleDescription}')  # fill scale description
            time.sleep(1)

        else:
            self.hw.ClickElement(f'//a[.="{Object_name}"]', 'xpath')  # to click rating scale name heading
            time.sleep(4)
            popup = self.hw.GetElement(
                '//div[@class="sfPanelComponent fd-message-box__content fd-message-box__content--compact globalContainer globalPortletBodyBackground globalRoundedCorners revolutionPanel sfDialogBox hasTitle"]',
                'xpath')
            if popup is not None:
                self.hw.ClickElement('//button[@id="dlgButton_393:"][@title="OK"]', 'xpath')
                time.sleep(5)
            self.hw.FillField_2(f'//textarea[@id="50:_txtArea"]', 'xpath', f'{ScaleDescription}')

        for data in self.data_record:
            SN, Score, ScoreLabel, ScoreDescription = data.Scale_Name, data.Score, data.Score_Label, data.Score_Description
            if Object_name == SN:
                Score_check = self.hw.isElementPresent(f'//input[@value="{Score}"]', 'xpath')

                if Score_check is True:
                    self.hw.FillField_2(
                        f'//input[@value="{Score}"]//parent::span//parent::div//parent::div//parent::div//parent::td//following-sibling::td//input',
                        'xpath', f'{ScoreLabel}')
                    self.hw.FillField_2(f'//input[@value="{Score}"]//ancestor::td[1]//following-sibling::td//textarea',
                                      'xpath', f'{ScoreDescription}')

                if Score_check is False:
                    if self.hw.isElementPresent('//input[@value="Score"]', 'xpath'):
                        self.hw.FillField_2(f'//input[@value="Score"]', 'xpath', f'{Score}')
                        self.hw.FillField_2(f'//input[@value="Give a short label for the score..."]', 'xpath', f'{ScoreLabel}')
                        self.hw.FillField_2(f'//textarea[.="Give detailed description..."]', 'xpath', f'{ScoreDescription}')
                        self.hw.ClickElement('//span[@id="38:_outerBtn"]', 'xpath')  # Click the Save option
                        time.sleep(3)
                    else:
                        self.hw.ClickElement('//a[.="Add New Score"]', 'xpath')
                        self.hw.FillField_2(f'//input[@value="Score"]', 'xpath', f'{Score}')
                        self.hw.FillField_2(f'//input[@value="Give a short label for the score..."]', 'xpath', f'{ScoreLabel}')
                        self.hw.FillField_2(f'//textarea[.="Give detailed description..."]', 'xpath', f'{ScoreDescription}')
                        self.hw.ClickElement('//span[@id="38:_outerBtn"]', 'xpath')  # Click the Save option
                        time.sleep(1)

                else:
                    pass

        self.hw.ClickElement('//span[@id="38:_outerBtn"]', 'xpath')  # Click the Save option
        time.sleep(1)

        self.hw.ClickElement('//a[text()="Rating Scale Designer"]', 'xpath')  # Click the Rating Scale option
        time.sleep(2)


Class = Main()
Class.ExecuteProcess()
