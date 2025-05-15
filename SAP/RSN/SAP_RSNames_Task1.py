# To get a dictionary of rating scale names, description, score, score label and score description
from selenium import webdriver
from Utilities.HandyWrappers import HandyWrappers
import time


class SAPTask1_2_3:
    sourcelink = 'https://pmsalesdemo8.successfactors.com/sf/start/#/companyEntry'
    driver = webdriver.Chrome()
    hw = HandyWrappers(driver)
    driver.get(sourcelink)
    driver.implicitly_wait(5)

    def SAPTask1_2_3(self):
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

        ratingscale_names_list = self.hw.GetElementlistofText('//table[@id="26:m-m-tbl"]//tr//td[1]', 'xpath')
        mydict1 = {}

        for name in range(len(ratingscale_names_list)):
            scale_description = self.hw.GetElementAttribute(f'//a[.="{ratingscale_names_list[name]}"]/ancestor::td[1]/following-sibling::td[2]', 'xpath', 'innerText')
            time.sleep(2)

            self.hw.ClickElement(f'//a[text()="{ratingscale_names_list[name]}"]', 'xpath')      # to click rating scale name headings

            popup = self.hw.GetElement('//*[@class="sfPanelComponent fd-message-box__content fd-message-box__content--compact globalContainer globalPortletBodyBackground globalRoundedCorners revolutionPanel sfDialogBox hasTitle"]', 'xpath')
            if popup is None:
                pass
            else:
                # click popup ok
                self.hw.ClickElement('//button[@class="globalRoundedCornersXSmall globalPrimaryButton fd-button fd-button--compact fd-button--emphasized"]',
                                     'xpath')

            list_of_scores = self.hw.GetElementlistofattribute('//input[@size="7"]', 'xpath', 'value')
            list_of_score_labels = self.hw.GetElementlistofattribute('//input[@size="34"]', 'xpath', 'value')
            list_of_score_descriptions = self.hw.GetElementlistofattribute('//textarea[@cols="42"]', 'xpath', 'value')
            list1 = []

            for i in range(len(list_of_scores)):
                mydict1[f'{ratingscale_names_list[name]}'] = list1
                list1.append([ratingscale_names_list[name], scale_description, list_of_scores[i], list_of_score_labels[i], list_of_score_descriptions[i]])

            self.hw.ClickElement('//a[@id="42:_link"]', 'xpath')    # to click cancel

        print(mydict1)
        return mydict1


"""test = SAPTask1_2_3()
test.SAPTask1_2_3()"""
