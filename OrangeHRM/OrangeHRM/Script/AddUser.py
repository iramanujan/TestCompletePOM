import WebElement

ObjectRepository = {
                                      "UserRole": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#systemUser_userType",
                                                    "All"               :   False
                                                  },
                                      "EmployeeName": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#systemUser_employeeName_empName",
                                                    "All"               :   False
                                                  },
                                      "EmployeeNameList": 
                                                  {
                                                    "FindBy"       :   "xpath",
                                                    "Value"         :   "//div[@class='ac_results']/ul/li/strong[text()='TEXT']",
                                                    "All"              :   False
                                                  },
                                      "UserName": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#systemUser_userName",
                                                    "All"               :   False
                                                  },
                                      "Status": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#systemUser_status",
                                                    "All"               :   False
                                                  },
                                      "Password": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#systemUser_password",
                                                    "All"               :   False
                                                  },
                                      "ConfirmPassword": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#systemUser_confirmPassword",
                                                    "All"               :   False
                                                  },
                                      "ConfirmPassword": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#systemUser_confirmPassword",
                                                    "All"               :   False
                                                  },
                                      "Save": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#btnSave",
                                                    "All"               :   False
                                                  },
                                      "Cancel": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#btnCancel",
                                                    "All"               :   False
                                                  },
                                      "ErrMsgEmpName": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "span.validation-error[for='systemUser_employeeName_empName']",
                                                    "All"               :   False,
                                                     "EmployeeDoesNotExist"                   :     "Employee does not exist",
                                                     "Required"                   :     "Required"
                                                  },
                                      "ErrMsgUserName": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "span.validation-error[for='systemUser_userName']",
                                                    "All"               :   False,
                                                     "MinimumChar"                   :     "Should have at least 5 characters",
                                                     "Required"                   :     "Required"
                                                  },
                                      "ErrMsgPassword": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "span.validation-error[for='systemUser_password']",
                                                    "All"               :   False,
                                                     "MinimumChar"                   :     "Should have at least 8 characters"
                                                  },
                                      "ErrMsgConfirmPassword": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "span.validation-error[for='systemUser_confirmPassword']",
                                                    "All"               :   False,
                                                     "MinimumChar"                   :     "Passwords do not match"
                                                  }
                                      }
 
                                      
def GetValueFromOR(FirstLevelKey, SecoundLevelKey):
  return ObjectRepository[FirstLevelKey][SecoundLevelKey];
                                                                                                                 
def UserRole():
  FindBy = GetValueFromOR("UserRole","FindBy");
  Value = GetValueFromOR("UserRole","Value");
  All = GetValueFromOR("UserRole","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  return WebObject
  
def EmployeeName():
  FindBy = GetValueFromOR("EmployeeName","FindBy");
  Value = GetValueFromOR("EmployeeName","Value");
  All = GetValueFromOR("EmployeeName","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  WebObject.value = ""
  WebObject.Click()
  return WebObject
  
def EmployeeNameList(strEmployeeName):
  FindBy = GetValueFromOR("EmployeeNameList","FindBy");
  Value = GetValueFromOR("EmployeeNameList","Value");
  UpdatedValue = aqString.Replace(Value,"TEXT",str(strEmployeeName))
  All = GetValueFromOR("EmployeeNameList","All");
  WebObject = WebElement.GetWebElement(FindBy,UpdatedValue,All)
  WebObject.focus
  return WebObject

def UserName():
  FindBy = GetValueFromOR("UserName","FindBy");
  Value = GetValueFromOR("UserName","Value");
  All = GetValueFromOR("UserName","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  WebObject.value = ""
  WebObject.Click()
  return WebObject
  
def Status():
  FindBy = GetValueFromOR("Status","FindBy");
  Value = GetValueFromOR("Status","Value");
  All = GetValueFromOR("Status","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  return WebObject;
 
def Password():
  FindBy = GetValueFromOR("Password","FindBy");
  Value = GetValueFromOR("Password","Value");
  All = GetValueFromOR("Password","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  WebObject.value = ""
  WebObject.Click()
  return WebObject
  
def ConfirmPassword():
  FindBy = GetValueFromOR("ConfirmPassword","FindBy");
  Value = GetValueFromOR("ConfirmPassword","Value");
  All = GetValueFromOR("ConfirmPassword","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  WebObject.value = ""
  WebObject.Click()
  return WebObject
  
def Save():
  FindBy = GetValueFromOR("Save","FindBy");
  Value = GetValueFromOR("Save","Value");
  All = GetValueFromOR("Save","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  return WebObject
  
def Cancel():
  FindBy = GetValueFromOR("Cancel","FindBy");
  Value = GetValueFromOR("Cancel","Value");
  All = GetValueFromOR("Cancel","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  return WebObject
    
def ErrMsgEmpName():
  FindBy = GetValueFromOR("ErrMsgEmpName","FindBy");
  Value = GetValueFromOR("ErrMsgEmpName","Value");
  All = GetValueFromOR("ErrMsgEmpName","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  return WebObject
  
def ErrMsgUserName():
  FindBy = GetValueFromOR("ErrMsgUserName","FindBy");
  Value = GetValueFromOR("ErrMsgUserName","Value");
  All = GetValueFromOR("ErrMsgUserName","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  return WebObject
  
def ErrMsgPassword():
  FindBy = GetValueFromOR("ErrMsgPassword","FindBy");
  Value = GetValueFromOR("ErrMsgPassword","Value");
  All = GetValueFromOR("ErrMsgPassword","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  return WebObject
  
def ErrMsgConfirmPassword():
  FindBy = GetValueFromOR("ErrMsgConfirmPassword","FindBy");
  Value = GetValueFromOR("ErrMsgConfirmPassword","Value");
  All = GetValueFromOR("ErrMsgConfirmPassword","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  return WebObject