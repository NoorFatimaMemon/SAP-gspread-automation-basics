import time
from gspread_Methods import gspread_Method
from selenium import webdriver
from HandyWrappers import HandyWrapper
import Model_FO_Config_obj
from Successfactor_Login_v1 import sf_login

gMethod=gspread_Method()
ws=gMethod.worksheetOpen(spreadsheetname="Gspread", worksheetname="SAP COD")

class TC_Valid_MDF_Object:
    driver = webdriver.Chrome()
    driver.maximize_window()
    url="https://pmsalesdemo8.successfactors.com"
    hw=HandyWrapper(driver)
    sf_login(driver, hw, url)
    Controller_FO_Obj = Model_FO_Config_obj.Controller_FO_Object()
    pending_record= Controller_FO_Obj.LoadData(ws)

    def Execute_Precoess(self):
        currentUrl=self.driver.current_url
        creds= currentUrl.split('_s.crb=')
        url2="https://pmsalesdemo8.successfactors.com/xi/ui/genericobject/pages/mdf/mdf.xhtml?co=1&_s.crb=" + creds[-1] + "#c=1&t=GOObjectDefinition&i="
        self.driver.get(url2)
        time.sleep(0.5)

        for record in self.pending_record:
            self.Process_Object(record)

    def Process_Object(self, record):
        ObjectUrl= self.driver.current_url + record.Code
        self.driver.get(ObjectUrl)
        time.sleep(1)
        Col=Model_FO_Config_obj.ValidationProps()
        processing_list_of_None=[]

        cell_List=[]
        if self.hw.isElementPresent("//div[.='Object does not Exist Or No Permission']", "xpath"):
            cell_List.append((f"B{record.Item_ID+1}:O{record.Item_ID+1}", False))
            processing_list_of_None.append(None)
        else:
            cell_List.append((f"{Col.Code}{record.Item_ID +1}", True))
            time.sleep(1)

            EDexistence=self.hw.isElementPresent(f"(//tr[@class='form_field ']//td[.='Effective Dating']//following-sibling::td/*/*//span[.='{record.Effective_Dating}'])[1]", "xpath")
            cell_List.append((f"{Col.Effective_Dating}{record.Item_ID + 1}", EDexistence))
            time.sleep(0.5)

            API_Vexistence=self.hw.isElementPresent(f"(//tr[@class='form_field ']//td[.='API Visibility']//following-sibling::td/*/*//span[.='{record.API_Visibility}'])[1]", "xpath")
            cell_List.append((f"{Col.API_Visibility}{record.Item_ID + 1}", API_Vexistence))
            time.sleep(0.5)

            StatusExistence=self.hw.isElementPresent(f"(//tr[@class='form_field ']//td[.='Status']//following-sibling::td/*/*//span[.='{record.Status}'])[1]", "xpath")
            cell_List.append((f"{Col.Status}{record.Item_ID + 1}", StatusExistence))
            time.sleep(0.5)

            MDF_existence=self.hw.isElementPresent(f"(//tr[@class='form_field ']//td[.='MDF Version History']//following-sibling::td/*/*//span[.='{record.MDF_Version_History}'])[1]", "xpath")
            cell_List.append((f"{Col.MDF_Version_History}{record.Item_ID + 1}", MDF_existence))
            time.sleep(0.5)

            D_Scr_existence= self.hw.isElementPresent(f"(//tr[@class='form_field ']//td[.='Default Screen']//following-sibling::td/*/*//span[.='{record.Default_Screen}'])[1]", "xpath")
            cell_List.append((f"{Col.Default_Screen}{record.Item_ID + 1}", D_Scr_existence))
            time.sleep(0.5)

            Label_existence=self.hw.isElementPresent(f"(//tr[@class='form_field ']//td[.='Label']//following-sibling::td/*/*//span[.='{record.Label}'])[1]", "xpath")
            cell_List.append((f"{Col.Label}{record.Item_ID + 1}", Label_existence))
            time.sleep(0.5)

            Des_exitence=self.hw.isElementPresent(f"(//tr[@class='form_field ']//td[.='Description']//following-sibling::td/*/*//span[.='{record.Description}'])[1]", "xpath")
            cell_List.append((f"{Col.Description}{record.Item_ID + 1}", Des_exitence))
            time.sleep(0.5)

            API_S_V_existence=self.hw.isElementPresent(f"(//tr[@class='form_field ']//td[.='API Sub Version']//following-sibling::td/*/*//span[.='{record.API_Sub_Version}'])[1]", "xpath")
            cell_List.append((f"{Col.API_Sub_Version}{record.Item_ID + 1}", API_S_V_existence))
            time.sleep(0.5)

            SUF_existence=self.hw.isElementPresent(f"(//tr[@class='form_field ']//td[.='Subject User Field']//following-sibling::td/*/*//span[.='{record.Subject_User_Field}'])[1]", "xpath")
            cell_List.append((f"{Col.Subject_User_Field}{record.Item_ID + 1}", SUF_existence))
            time.sleep(0.5)

            Work_R=self.hw.isElementPresent(f"(//tr[@class='form_field ']//td[.='Workflow Routing']//following-sibling::td/*/*//span[.='{record.Workflow_Routing}'])[1]", "xpath")
            cell_List.append((f"{Col.Workflow_Routing}{record.Item_ID + 1}", Work_R))
            time.sleep(0.5)

            PData=self.hw.isElementPresent(f"(//tr[@class='form_field ']//td[.='Pending Data']//following-sibling::td/*/*//span[.='{record.Pending_Data}'])[1]", "xpath")
            cell_List.append((f"{Col.Pending_Data}{record.Item_ID + 1}", PData))
            time.sleep(0.5)

            Todo_C=self.hw.isElementPresent(f"(//tr[@class='form_field ']//td[.='Todo Category']//following-sibling::td/*/*//span[.='{record.Todo_Category}'])[1]", "xpath")
            cell_List.append((f"{Col.Todo_Category}{record.Item_ID + 1}", Todo_C))
            time.sleep(0.5)

            Obj_C=self.hw.isElementPresent(f"(//tr[@class='form_field ']//td[.='Object Category']//following-sibling::td/*/*//span[.='{record.Object_Category}'])[1]", "xpath")
            cell_List.append((f"{Col.Object_Category}{record.Item_ID + 1}", Obj_C))
            time.sleep(0.5)

            gMethod.format_cell_List(ws, cell_List)

            if EDexistence == False or API_Vexistence == False or StatusExistence == False or MDF_existence == False or D_Scr_existence == False or Label_existence == False or Des_exitence == False or API_S_V_existence == False or SUF_existence ==False or Work_R==False or PData== False or Todo_C== False or Obj_C == False:
                processing_list_of_None.append(None)
            if None not in processing_list_of_None:
                ws.update_cell(record.Item_ID + 1, 18, "Processed")

TC_Valid_Obj=TC_Valid_MDF_Object()
TC_Valid_Obj.Execute_Precoess()
