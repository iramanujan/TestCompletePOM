def HelloDud():
  UserName    =   str(Project.Variables.VariableByName['UserName']);
  Password    =   str(Project.Variables.VariableByName['Password']);
  AppUrl      =   str(Project.Variables.VariableByName['ApplicationURL']);
  PageUrl     =   str(Project.Variables.VariableByName['PageURL']);
  BrowserType =   str(Project.Variables.VariableByName['Chrome']);
  
  Log.Message("User Name: " + UserName)
  Log.Message("Password: " + Password)
  Log.Message("Application URL: " + AppUrl)
  Log.Message("Page URL: " + PageUrl)
  Log.Message("Browser Name: " + BrowserType)
  
  
# Specify the browser using a test parameter
def Test1():
  Browsers.Item['iexplore'].Run("http://smartbear.com");
  
  

def Test2():
  Browsers.Item[btChrome].Navigate("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers")
  fieldset = Aliases.browser.pageOrangehrm.formSearchForm.fieldset
  vselect = fieldset.selectUserRole
  vselect.Click(212, 14)
  vselect.ClickItem("Admin")
  fieldset.selectStatus.ClickItem("Disabled")
  fieldset.selectStatus.wText

def Test3():
  browser = Aliases.browser
  OCR.Recognize(browser.BrowserWindow).BlockByText("OrangeHRM", spLeftMost).Click()
  Browsers.Item[btChrome].Navigate("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers?sortField=u.Employee.emp_firstname&sortOrder=DESC")
  page = browser.pageOrangehrm
  table = page.panelCustomerlist.formFrmlistOhrmlistcomponent.tableResulttable
  table.link.Click();
  Log.Message(table.link.getAttribute('class'))
  page.Wait()
