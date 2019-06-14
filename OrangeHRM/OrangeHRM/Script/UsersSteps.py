import Users
import BrowserFactry  
import Waiter
import LoginSteps
import WebElementHelper
import Logger
import Helper

def NavigateToSystemUserPage():
  LoginSteps.LoginWithValidInput();
  
  WebObjAdmin = Users.Admin()
  WebObjUsrMgmt = Users.UserManagement()
  
  WebObjAdmin.Click();
  WebObjUsrMgmt.Click();
  Waiter.Wait(5)
  strPageUrl = BrowserFactry.GetPageUrl()

  Logger.CheckPoint('Navigate To Sytem User Page Successfully: '+strPageUrl) if(aqString.Find(strPageUrl,'viewSystemUsers') != -1)else Log.Error('Navigate To Sytem User Page Failed: ' +strPageUrl)

def VerifySorting(strColumnName):  
  columnIndex = GetColumnIndexByName(strColumnName);
  WebObjsSort = Users.Sort(columnIndex);

  WebObjsSort.Click();
  Waiter.Wait(3)
  strAsc = WebObjsSort.getAttribute('class')

  strFirstRecord = Users.FirstRecord(columnIndex).contentText;
  strLastRecord = Users.LastRecord(columnIndex).contentText;
    
  WebObjsSort.Click();
  Waiter.Wait(3)
  strDesc = WebObjsSort.getAttribute('class')

  strFirstRecord2 = Users.FirstRecord(columnIndex).contentText    #textContent;
  strLastRecord2 = Users.LastRecord(columnIndex).contentText     #textContent;
  
  Log.Message("Order By: {"+strColumnName+" "+strAsc+"} First Value: {"+strFirstRecord+"}, Last Value: {"+strLastRecord+"}")
  Log.Message("Order By: {"+strColumnName+" "+strDesc+"} First Value: {"+strFirstRecord2+"}, Last Value: {"+strLastRecord2+"}")
  
  Logger.CheckPoint("Validate Sorting On Column {"+strColumnName+"} . Pass") if(strFirstRecord == strLastRecord2 and strLastRecord == strFirstRecord2) else Log.Error("Validate Sorting On Column {"+strColumnName+"}. Failed")
        
def GetColumnIndexByName(strColumnName):
  Waiter.Wait(1)
  WebObjsUserWebTable = Users.UserWebTable()
  count = BuiltIn.VarArrayHighBound(WebObjsUserWebTable,1);
  if (count > -1):
    for index in range (0,count+1):
      if(aqString.Trim(WebObjsUserWebTable[index].innerText) == strColumnName):
        Log.Message("Index Number of Column {"+strColumnName +"} is "+str(index+2))
        return index+2;
        
def GetRowCount(strColumnName):
  columnIndex = GetColumnIndexByName(strColumnName)
  WebObjsRowCount = Users.RowCount(columnIndex);
  return len(WebObjsRowCount);
        
def ApplyFilter(strFilterOn):  
  if(strFilterOn == 'Username'):
    lstColUsername = GetRowData(strFilterOn)
    strFilterValue = Helper.SelectRandomValueFromList(lstColUsername);
    WebObjUserName  = Users.UserName()
    Sys.Desktop.Keys(strFilterValue);
    
  if(strFilterOn == 'User Role'):
    WebObjUserType    = Users.UserType()
    listFilterValues = Helper.ConvertStringIntoList(WebObjUserType.wItemList,";")
    strFilterValue = Helper.SelectRandomValueFromList(listFilterValues);
    WebObjUserType.ClickItem(strFilterValue);
    if(WebObjUserType.wText == strFilterValue):
      Log.Checkpoint("Selected Value From {"+strFilterOn+"} Dropdown is: "+WebObjUserType.wText)
    else:
      Log.Error("Unable To Select Value {"+strFilterValue+"} from {"+strFilterOn+"} Dropdown");
    
  if(strFilterOn == 'Employee Name'):
    WebObjEmployeeName  = Users.EmployeeName()
    lstEmpName = GetRowData(strFilterOn)
    strFilterValue = Helper.SelectRandomValueFromListWithExclusion(lstEmpName,'');
    Sys.Desktop.Keys(strFilterValue);
    WebObjEmployeeNameList  = Users.EmployeeNameList(strFilterValue)
    WebObjEmployeeNameList.Click();
    
  if(strFilterOn == 'Status'):
    WebObjUserStatus  = Users.UserStatus()
    listFilterValues = Helper.ConvertStringIntoList(WebObjUserStatus.wItemList,";")
    strFilterValue = Helper.SelectRandomValueFromList(listFilterValues);
    WebObjUserStatus.ClickItem(strFilterValue);
    if(WebObjUserStatus.wText == strFilterValue):
      Log.Checkpoint("Selected Value From {"+strFilterOn+"} Dropdown is: "+WebObjUserStatus.wText)
    else:
      Log.Error("Unable To Select Value {"+strFilterValue+"} from {"+strFilterOn+"} Dropdown");

  if(strFilterValue == 'All'):
    preFilterRowCount = GetRowCount(strFilterOn);
    WebObjSearch  = Users.Search()
    WebObjSearch.Click();
    postFilterRowCount = GetRowCount(strFilterOn);
    if(postFilterRowCount != preFilterRowCount):
      Log.Error("Validate Filter For Condition {Where "+strFilterOn+" = "+strFilterValue+"} is Fail. Actual Row Count {"+str(postFilterRowCount)+"} Expected Value: {"+str(preFilterRowCount)+"}");
    else:
      Logger.CheckPoint("Validate Filter For Condition {Where "+strFilterOn+" = "+strFilterValue+"} is Pass. Actual Row Count {"+str(postFilterRowCount)+"} Expected Value: {"+str(preFilterRowCount)+"}");
  else:
    WebObjSearch  = Users.Search()
    WebObjSearch.Click();
    VerifyFilter(strFilterOn,strFilterValue);

def GetRowData(strColumnName):
  columnIndex     =     GetColumnIndexByName(strColumnName);
  rowCount           =      GetRowCount(strColumnName);
  rowList = list()
  for rowIndex in range (1,rowCount+1):
    cellValue = Users.Cell(columnIndex,rowIndex).textContent
    rowList.append(cellValue);
  return rowList
    
def VerifyFilter(strFilterOn,strFilterValue):
  lstRowValues = GetRowData(strFilterOn)
  if(lstRowValues is None or len(lstRowValues) == 0):
    Log.Message("No Record Found  For Condition {Where "+strFilterOn+" = "+strFilterValue+"}")
  else:
    for (index, value) in enumerate(lstRowValues):
      if(value != strFilterValue):
        Log.Error("Validate Filter For Condition {Where "+strFilterOn+" = "+strFilterValue+"} is Fail at Row Number {"+str(index+1)+"}. Actual Value: {"+value+"} Expected Value: {"+strFilterValue+"}");
        return;
    Logger.CheckPoint("Validate Filter For Condition {Where "+strFilterOn+" = "+strFilterValue+"} is Pass. Actual Value: {"+value+"} Expected Value: {"+strFilterValue+"}");