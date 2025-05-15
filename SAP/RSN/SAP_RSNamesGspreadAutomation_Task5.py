"""To change the data of rating scale names, description, score, score label and score description from gspread
to the instance (if any rating scale or score is not present then add those)"""

import time
from selenium import webdriver
from Utilities.HandyWrappers import HandyWrappers
import gspread

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
    data_record = [vars(a) for a in data_list if a.Scale_Name in processing_heading]

    return data_record, processing_heading


class Gspread_Task3:
    sourcelink = 'https://pmsalesdemo8.successfactors.com/sf/start/#/companyEntry'
    driver = webdriver.Chrome()
    hw = HandyWrappers(driver)
    driver.get(sourcelink)

    def gspreadTask3(self):
        self.hw.ClickElement('//input[@id="__input0-inner"]', 'xpath')
        time.sleep(1)
        self.hw.SendKeys('//input[@placeholder="Enter Company ID"]', 'xpath', 'SFPART065417')   # to enter company id
        time.sleep(1)
        self.hw.ClickElement('//button[@id="__button0"]', 'xpath')
        time.sleep(1)
        self.hw.SendKeys('//input[@placeholder="Username"]', 'xpath', 'codebotintern')  # to enter username
        time.sleep(1)
        self.hw.SendKeys('//input[@placeholder="Enter Password"]', 'xpath', 'partBos@DC88')     # to enter password
        time.sleep(1)
        self.hw.ClickElement('//*[@id="__button2-inner"]', 'xpath')
        time.sleep(1)

        link_1 = self.driver.current_url
        link_1_split = link_1.split('s.crb=')
        link_2 = "https://pmsalesdemo8.successfactors.com/acme?fbacme_o=admin&pess_old_admin=true&ap_param_action=form_rating_scale&itrModule=talent&_s.crb=A38Sok%2bYiCF0lB2TAi758Nnvn7SlJWGMVsXzGt3gmCc%3d"
        link_2_split = link_2.split("s.crb=")
        Rating_Scale_Link = link_2_split[0] + "s.crb=" + link_1_split[1]
        self.driver.get(Rating_Scale_Link)
        time.sleep(5)

        data_record, processing_heading = model_controller()
        processed_scale_names = set()
        tag_num = 1

        for data in data_record:
            [ScaleName, ScaleDescription, Score, ScoreLabel, ScoreDescription] = data.values()

            if ScaleName not in processed_scale_names:
                processed_scale_names.add(ScaleName)
                if len(processed_scale_names) <= 1:
                    ScaleName_check = self.hw.GetElementAttribute(f'//a[.="{ScaleName}"]', 'xpath', 'innerText')
                    ScaleDescription_check = self.hw.GetElementAttribute(f'//a[text()="{ScaleName}"]/ancestor::td[1]/following-sibling::td[2]//span', 'xpath', 'title')

                    if ScaleName_check is None:
                        self.hw.ClickElement('//*[@id="17:_label"]/span', 'xpath')      # to create a new rating scale
                        time.sleep(3)
                        self.hw.FillField_2(f'//input[@id="48:_txtFld"]', 'xpath', f'{ScaleName}')

                        self.hw.FillField_2(f'//textarea[@id="50:_txtArea"]', 'xpath', f'{ScaleDescription}')
                        time.sleep(3)

                        self.hw.ClickElement('//input[@id="53:_item_3"]', 'xpath')      # to click on Build your own
                        self.hw.ClickElement('//button[text()="OK"]', 'xpath')      # to click ok
                    else:
                        self.hw.ClickElement(f'//a[.="{ScaleName}"]', 'xpath')  # to click rating scale name heading
                        time.sleep(4)

                    popup = self.hw.GetElement(
                            '//div[@class="sfPanelComponent fd-message-box__content fd-message-box__content--compact globalContainer globalPortletBodyBackground globalRoundedCorners revolutionPanel sfDialogBox hasTitle"]',
                            'xpath')
                    if popup is not None:
                        self.hw.ClickElement('//button[@id="dlgButton_393:"][@title="OK"]', 'xpath')
                        time.sleep(5)

                    if ScaleName_check != ScaleName:
                        self.hw.FillField_2(f'//input[@id="48:_txtFld"]', 'xpath', f'{ScaleName}')
                    else:
                        pass

                    if ScaleDescription_check != ScaleDescription:
                        self.hw.FillField_2(f'//textarea[@id="50:_txtArea"]', 'xpath', f'{ScaleDescription}')
                        time.sleep(3)
                    else:
                        pass

                elif len(processed_scale_names) > 1:
                    tag_num = 1
                    self.hw.ClickElement('//span[@id="38:_outerBtn"]', 'xpath')  # Click the Save option
                    time.sleep(1)

                    self.hw.ClickElement('//a[text()="Rating Scale Designer"]', 'xpath')  # Click the Rating Scale option
                    time.sleep(5)

                    ScaleName_check = self.hw.GetElementAttribute(f'//a[.="{ScaleName}"]', 'xpath', 'innerText')
                    ScaleDescription_check = self.hw.GetElementAttribute(f'//a[text()="{ScaleName}"]/ancestor::td[1]/following-sibling::td[2]//span', 'xpath', 'title')

                    if ScaleName_check is None:
                        self.hw.ClickElement('//*[@id="17:_label"]/span', 'xpath')      # to create a new rating scale
                        time.sleep(3)
                        self.hw.FillField_2(f'//input[@id="48:_txtFld"]', 'xpath', f'{ScaleName}')

                        self.hw.FillField_2(f'//textarea[@id="50:_txtArea"]', 'xpath', f'{ScaleDescription}')
                        time.sleep(3)

                        self.hw.ClickElement('//input[@id="53:_item_3"]', 'xpath')      # to click on Build your own
                        time.sleep(1)
                        self.hw.ClickElement('//button[text()="OK"]', 'xpath')      # to click ok
                        time.sleep(3)
                    else:
                        self.hw.ClickElement(f'//a[.="{ScaleName}"]', 'xpath')  # to click rating scale name headings
                        time.sleep(4)

                    popup = self.hw.GetElement(
                            '//div[@class="sfPanelComponent fd-message-box__content fd-message-box__content--compact globalContainer globalPortletBodyBackground globalRoundedCorners revolutionPanel sfDialogBox hasTitle"]',
                            'xpath')
                    if popup is not None:
                        self.hw.ClickElement('//button[@id="dlgButton_393:"][@title="OK"]', 'xpath')
                        time.sleep(5)

                    if ScaleName_check != ScaleName:
                        self.hw.FillField_2(f'//input[@id="48:_txtFld"]', 'xpath', f'{ScaleName}')
                    else:
                        pass

                    if ScaleDescription_check != ScaleDescription:
                        self.hw.FillField_2(f'//textarea[@id="50:_txtArea"]', 'xpath', f'{ScaleDescription}')
                        time.sleep(3)
                    else:
                        pass

            Score_check = self.hw.GetElementAttribute(f'//table[@id="66:m-m-tbl"]//tr[{tag_num}]//input[@size="7"]', 'xpath',
                                                      'value')
            if Score_check != str(Score) or Score_check is None:
                score_element = self.hw.GetElement(f'//*[@id="66:m-m-tbl"]//tr[{tag_num}]//*[@size="7"]', 'xpath')
                if score_element is None:
                    self.hw.ClickElement('//a[.="Add New Score"]', 'xpath')
                    self.hw.FillField_2(f'//*[@id="66:m-m-tbl"]//tr[{tag_num}]//*[@size="7"]', 'xpath', f'{Score}')
                    time.sleep(3)
                else:
                    self.hw.FillField_2(f'//*[@id="66:m-m-tbl"]//tr[{tag_num}]//*[@size="7"]', 'xpath', f'{Score}')
            else:
                pass

            ScoreLabel_check = self.hw.GetElementAttribute(f'//table[@id="66:m-m-tbl"]//tr[{tag_num}]//input[@size="34"]',
                                                           'xpath', 'value')
            if ScoreLabel_check != ScoreLabel:
                self.hw.FillField_2(f'//table[@id="66:m-m-tbl"]//tr[{tag_num}]//input[@size="34"]', 'xpath', f'{ScoreLabel}')
                time.sleep(3)
            else:
                pass

            ScoreDescription_check = self.hw.GetElementAttribute(f'//table[@id="66:m-m-tbl"]//tr[{tag_num}]//textarea',
                                                                 'xpath', 'linkText')
            if ScoreDescription_check != ScoreDescription:
                self.hw.FillField_2(f'//table[@id="66:m-m-tbl"]//tr[{tag_num}]//textarea', 'xpath', f'{ScoreDescription}')
                time.sleep(3)
            else:
                pass
            tag_num = tag_num + 1

        time.sleep(3)
        self.hw.ClickElement('//span[@id="38:_outerBtn"]', 'xpath')  # Click the Save option
        time.sleep(5)


test = Gspread_Task3()
test.gspreadTask3()
