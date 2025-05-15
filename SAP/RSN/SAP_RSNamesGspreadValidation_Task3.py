# To validate the data of rating scale names, description, score, score label and score description in the gspread
import time
from selenium import webdriver
from Utilities.HandyWrappers import HandyWrappers
import gspread

gc = gspread.service_account()
sh = gc.open("Gspread-Task 1")
wks = sh.worksheet("SAP")


class Model_RatingScale:
    item_id = ""
    Scale_Name = ""
    Scale_Description = ""
    Score = ""
    Score_Label = ""
    Score_Description = ""


class Processing_ScaleStatus:
    item_id = ""
    Rating_Scale_Name = ""
    Scale_Status = ""


def model_controller():
    Sheet_Records = wks.get_all_records()
    processing_list = []
    data_list = []

    for record in Sheet_Records:
        rating_scale_model = Model_RatingScale()
        processing_status = Processing_ScaleStatus()

        rating_scale_model.item_id = record["Item ID"]
        rating_scale_model.Scale_Name = record["Scale Name"]
        rating_scale_model.Scale_Description = record["Scale Description"]
        rating_scale_model.Score = record["Score"]
        rating_scale_model.Score_Label = record["Score Label"]
        rating_scale_model.Score_Description = record["Score Description"]
        data_list.append(rating_scale_model)

        processing_status.item_id = record["Item ID"]
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
        invalid_cell_format = {"backgroundColor": {"red": 1, "green": 0, "blue": 0}}
        valid_cell_format = {"backgroundColor": {"red": 0, "green": 1, "blue": 0}}
        processed_scale_names = set()
        Previous_scalename = None

        for data in data_record:
            [ID, ScaleName, ScaleDescription, Score, ScoreLabel, ScoreDescription] = data.values()

            if ScaleName not in processed_scale_names:
                if Previous_scalename in processed_scale_names:
                    unique_RSN = wks.find(f'{Previous_scalename}', in_column=8)
                    cell = unique_RSN.row
                    wks.update(f'I{cell}', 'Processed')
                else:
                    pass

                Previous_scalename = ScaleName

                # Check if the scale name is new and click the cancel option if it has changed
                processed_scale_names.add(ScaleName)

                if len(processed_scale_names) <= 1:
                    ScaleName_check = self.hw.GetElement(f'//a[text()="{ScaleName}"]', 'xpath')
                    wks.format(f'B{ID + 1}', invalid_cell_format) if ScaleName_check is None else wks.format(
                        f'B{ID + 1}', valid_cell_format)

                    ScaleDescription_check = self.hw.GetElement(
                        f'//a[text()="{ScaleName}"]/ancestor::td[1]/following-sibling::td[2]//span[.="{ScaleDescription}"]',
                        'xpath')
                    wks.format(f'C{ID + 1}', invalid_cell_format) if ScaleDescription_check is None else wks.format(
                        f'C{ID + 1}', valid_cell_format)
                    time.sleep(1)

                    self.hw.ClickElement(f'//a[.="{ScaleName}"]', 'xpath')  # to click rating scale name headings
                    time.sleep(4)

                    popup = self.hw.GetElement(
                        '//div[@class="sfPanelComponent fd-message-box__content fd-message-box__content--compact globalContainer globalPortletBodyBackground globalRoundedCorners revolutionPanel sfDialogBox hasTitle"]',
                        'xpath')
                    if popup is not None:
                        self.hw.ClickElement('//button[@id="dlgButton_393:"][@title="OK"]', 'xpath')
                        time.sleep(5)

                elif len(processed_scale_names) > 1:
                    self.hw.ClickElement('//a[@id="42:_link"]', 'xpath')  # Click the cancel option
                    time.sleep(1)

                    ScaleName_check = self.hw.GetElement(f'//a[text()="{ScaleName}"]', 'xpath')
                    wks.format(f'B{ID + 1}', invalid_cell_format) if ScaleName_check is None else wks.format(
                        f'B{ID + 1}', valid_cell_format)

                    ScaleDescription_check = self.hw.GetElement(
                        f'//a[text()="{ScaleName}"]/ancestor::td[1]/following-sibling::td[2]//span[.="{ScaleDescription}"]',
                        'xpath')
                    wks.format(f'C{ID + 1}', invalid_cell_format) if ScaleDescription_check is None else wks.format(
                        f'C{ID + 1}', valid_cell_format)
                    time.sleep(1)

                    self.hw.ClickElement(f'//a[.="{ScaleName}"]', 'xpath')  # to click rating scale name headings
                    # time.sleep(4)
                    time.sleep(1)

                    popup = self.hw.GetElement(
                        '//div[@class="sfPanelComponent fd-message-box__content fd-message-box__content--compact globalContainer globalPortletBodyBackground globalRoundedCorners revolutionPanel sfDialogBox hasTitle"]',
                        'xpath')
                    if popup is not None:
                        self.hw.ClickElement('//button[@id="dlgButton_393:"][@title="OK"]', 'xpath')
                        time.sleep(5)
            else:
                wks.format(f'B{ID + 1}', valid_cell_format)
                wks.format(f'C{ID + 1}', valid_cell_format)

            time.sleep(1)
            str_score = str(Score)
            Score_check = self.hw.GetElement(f'//span//input[@value="{str_score}"]', 'xpath')
            wks.format(f'D{ID + 1}', invalid_cell_format) if Score_check is None else wks.format(f'D{ID + 1}',
                                                                                                 valid_cell_format)
            ScoreLabel_check = self.hw.GetElement(f'//*[@value="{ScoreLabel}"]', 'xpath')
            wks.format(f'E{ID + 1}', invalid_cell_format) if ScoreLabel_check is None else wks.format(f'E{ID + 1}',
                                                                                                      valid_cell_format)
            ScoreDescription_check = self.hw.GetElement(f'//textarea[.="{ScoreDescription}"]', 'xpath')
            wks.format(f'F{ID + 1}', invalid_cell_format) if ScoreDescription_check is None else wks.format(
                f'F{ID + 1}', valid_cell_format)
            time.sleep(5)

        last_RatingScaleName = wks.find('Pending', in_column=9)
        cell_last_RatingScaleName = last_RatingScaleName.row
        wks.update(f'I{cell_last_RatingScaleName}', 'Processed')


test = Gspread_Task3()
test.gspreadTask3()
