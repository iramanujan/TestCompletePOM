﻿import WebElement
ObjectRepository = {
                                      "Admin": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#menu_admin_viewAdminModule",
                                                    "All"               :   False
                                                  },
                                      "UserManagement": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#menu_admin_UserManagement",
                                                    "All"               :   False
                                                  },
                                      "User": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#menu_admin_viewSystemUsers",
                                                    "All"               :   False
                                                  },
                                      "UserName": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#searchSystemUser_userName",
                                                    "All"               :   False
                                                  },  
                                      "UserType": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#searchSystemUser_userType",
                                                    "All"               :   False
                                                  },
                                      "EmployeeName": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#searchSystemUser_employeeName_empName",
                                                    "All"              :   False
                                                  },
                                      "EmployeeNameList": 
                                                  {
                                                    "FindBy"       :   "xpath",
                                                    "Value"         :   "//div[@class='ac_results']/ul/li/strong[text()='TEXT']",
                                                    "All"              :   False
                                                  },
                                      "UserStatus": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#searchSystemUser_status",
                                                    "All"               :   False
                                                  },
                                      "Search": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#searchBtn",
                                                    "All"              :   False
                                                  },
                                      "Reset": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#resetBtn",
                                                    "All"               :   False
                                                  },
                                      "UserWebTable": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#resultTable > thead > tr  a",
                                                    "All"               :   True
                                                  },
                                      "FirstRecord": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#resultTable > tbody > tr:first-child > td:nth-child(COLUMNINDEX)",
                                                    "All"               :   False
                                                  },
                                      "LastRecord": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#resultTable > tbody > tr:last-child > td:nth-child(COLUMNINDEX)",
                                                    "All"               :   False
                                                  },
                                      "Cell": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#resultTable > tbody > tr:nth-child(ROWINDEX) > td:nth-child(COLUMNINDEX)",
                                                    "All"               :   False
                                                  },
                                      "RowCount": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#resultTable > tbody > tr > td:nth-child(COLUMNINDEX)",
                                                    "All"               :   True
                                                  },
                                      "Sort": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#resultTable > thead > tr > th:nth-child(COLUMNINDEX) > a",
                                                    "All"               :   False
                                                  },
                                      "Add": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#btnAdd",
                                                    "All"               :   False
                                                  },
                                      "Delete": 
                                                  {
                                                    "FindBy"       :   "cssSelector",
                                                    "Value"         :   "#btnDelete",
                                                    "All"               :   False
                                                  }    
                                                  
                                     } 
       
def GetValueFromOR(FirstLevelKey, SecoundLevelKey):
  return ObjectRepository[FirstLevelKey][SecoundLevelKey];

def User():
  FindBy = GetValueFromOR("User","FindBy");
  Value = GetValueFromOR("User","Value");
  All = GetValueFromOR("User","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  return WebObject
  
def Admin():
  FindBy = GetValueFromOR("Admin","FindBy");
  Value = GetValueFromOR("Admin","Value");
  All = GetValueFromOR("Admin","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  return WebObject

def UserManagement():
    FindBy = GetValueFromOR("UserManagement","FindBy");
    Value = GetValueFromOR("UserManagement","Value");
    All = GetValueFromOR("UserManagement","All");
    WebObject = WebElement.GetWebElement(FindBy,Value,All)
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
  
def UserType():
  FindBy = GetValueFromOR("UserType","FindBy");
  Value = GetValueFromOR("UserType","Value");
  All = GetValueFromOR("UserType","All");
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
  
def UserStatus():
  FindBy = GetValueFromOR("UserStatus","FindBy");
  Value = GetValueFromOR("UserStatus","Value");
  All = GetValueFromOR("UserStatus","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  return WebObject;
  
def UserWebTable():
  FindBy = GetValueFromOR("UserWebTable","FindBy");
  Value = GetValueFromOR("UserWebTable","Value");
  All = GetValueFromOR("UserWebTable","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  return WebObject;
  
def Search():
  FindBy = GetValueFromOR("Search","FindBy");
  Value = GetValueFromOR("Search","Value");
  All = GetValueFromOR("Search","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  return WebObject
  
def Reset():
  FindBy = GetValueFromOR("Reset","FindBy");
  Value = GetValueFromOR("Reset","Value");
  All = GetValueFromOR("Reset","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  return WebObject

def Add():
  FindBy = GetValueFromOR("Add","FindBy");
  Value = GetValueFromOR("Add","Value");
  All = GetValueFromOR("Add","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  return WebObject

def Delete():
  FindBy = GetValueFromOR("Delete","FindBy");
  Value = GetValueFromOR("Delete","Value");
  All = GetValueFromOR("Delete","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  return WebObject

def FirstRecord(columnIndex):
  FindBy = GetValueFromOR("FirstRecord","FindBy");
  Value = GetValueFromOR("FirstRecord","Value");
  UpdatedValue = aqString.Replace(Value,"COLUMNINDEX",str(columnIndex))
  All = GetValueFromOR("FirstRecord","All");
  WebObject = WebElement.GetWebElement(FindBy,UpdatedValue,All)
  WebObject.focus
  return WebObject
  
def LastRecord(columnIndex):
  FindBy = GetValueFromOR("LastRecord","FindBy");
  Value = GetValueFromOR("LastRecord","Value");
  UpdatedValue = aqString.Replace(Value,"COLUMNINDEX",str(columnIndex))
  All = GetValueFromOR("LastRecord","All");
  WebObject = WebElement.GetWebElement(FindBy,UpdatedValue,All)
  WebObject.focus
  return WebObject
  
def Sort(columnIndex):
  FindBy = GetValueFromOR("Sort","FindBy");
  Value = GetValueFromOR("Sort","Value");
  UpdatedValue = aqString.Replace(Value,"COLUMNINDEX",str(columnIndex))
  All = GetValueFromOR("Sort","All");
  WebObject = WebElement.GetWebElement(FindBy,UpdatedValue,All)
  WebObject.focus
  return WebObject

def Cell(columnIndex,rowIndex):
  FindBy = GetValueFromOR("Cell","FindBy");
  Value = GetValueFromOR("Cell","Value");
  UpdatedValue = aqString.Replace(Value,"COLUMNINDEX",str(columnIndex))
  UpdatedValue2 =  aqString.Replace(UpdatedValue,"ROWINDEX",str(rowIndex))
  All = GetValueFromOR("Cell","All");
  WebObject = WebElement.GetWebElement(FindBy,UpdatedValue2,All)
  WebObject.focus
  return WebObject
  
def RowCount(columnIndex):
  FindBy = GetValueFromOR("RowCount","FindBy");
  Value = GetValueFromOR("RowCount","Value");
  UpdatedValue = aqString.Replace(Value,"COLUMNINDEX",str(columnIndex))
  All = GetValueFromOR("RowCount","All");
  WebObject = WebElement.GetWebElement(FindBy,UpdatedValue,All)
  return WebObject
  
def EmployeeNameList(strEmployeeName):
  FindBy = GetValueFromOR("EmployeeNameList","FindBy");
  Value = GetValueFromOR("EmployeeNameList","Value");
  UpdatedValue = aqString.Replace(Value,"TEXT",str(strEmployeeName))
  All = GetValueFromOR("EmployeeNameList","All");
  WebObject = WebElement.GetWebElement(FindBy,UpdatedValue,All)
  return WebObject