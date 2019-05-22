import Users
import BrowserFactry  
import Waiter
import LoginSteps
import WebElementHelper


def NavigateToSystemUserPage():
  LoginSteps.LoginWithValidInput();
  
  WebObjAdmin = Users.Admin()
  WebObjUsrMgmt = Users.UserManagement()
  
  WebObjAdmin.Click();
  WebObjUsrMgmt.Click();
  Waiter.WaitTillDocumentReady();

  strPageUrl = BrowserFactry.GetPageUrl()
  
  Log.Checkpoint('Navigate To Sytem User Page Successfully: '+strPageUrl) if(aqString.Find(strPageUrl,'viewSystemUsers') != -1)else Log.Error('Navigate To Sytem User Page Failed: ' +strPageUrl)

def VerifySorting(strColumnName):
  columnIndex = GetColumnIndexByName(strColumnName);
  WebObjsSort = Users.Sort(columnIndex);

  WebObjsSort.Click();
  Waiter.Wait(1)
  strAsc = WebObjsSort.getAttribute('class')

  strFirstRecord = Users.FirstRecord(columnIndex).textContent;
  strLastRecord = Users.LastRecord(columnIndex).textContent;
    
  WebObjsSort.Click();
  Waiter.Wait(1)
  strDesc = WebObjsSort.getAttribute('class')

  strFirstRecord2 = Users.FirstRecord(columnIndex).textContent;
  strLastRecord2 = Users.LastRecord(columnIndex).textContent;
  
  Log.Message("Order By: {"+strColumnName+" "+strAsc+"} First Value: {"+strFirstRecord+"}, Last Value: {"+strLastRecord+"}")
  Log.Message("Order By: {"+strColumnName+" "+strDesc+"} First Value: {"+strFirstRecord2+"}, Last Value: {"+strLastRecord2+"}")
  
  Log.Checkpoint("Validate Sorting On Column {"+strColumnName+"} . Pass") if(strFirstRecord == strLastRecord2 and strLastRecord == strFirstRecord2) else Log.Error("Validate Sorting On Column {"+strColumnName+"}. Failed")
        
def GetColumnIndexByName(strColumnName):
  WebObjsUserWebTable = Users.UserWebTable()
  count = BuiltIn.VarArrayHighBound(WebObjsUserWebTable,1);
  if (count > -1):
    for index in range (0,count+1):
      if(aqString.Trim(WebObjsUserWebTable[index].contentText) == strColumnName):
        Log.Message("Index Number of Column {"+strColumnName +"} is "+str(index+2))
        return index+2;