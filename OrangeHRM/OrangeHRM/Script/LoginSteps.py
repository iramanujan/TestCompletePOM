﻿import Login
import BrowserFactry  
import Waiter

def LoginWithValidInput(StrUserName = str(Project.Variables.VariableByName['UserName']),StrPassword = str(Project.Variables.VariableByName['Password'])):
  BrowserFactry.InitBrowser();
  
  WebObjUserName = Login.UserName();
  Sys.Desktop.Keys(StrUserName);
  
  WebObjPassword = Login.Password();
  Sys.Desktop.Keys(StrPassword);
  
  WebObjLogin = Login.Login();
  WebObjLogin.Click()
  
  if(Waiter.WaitTillDocumentReady()):
    WebObjLoginUsrName = Login.GetLoginUserName();
  
    ActualLoginUsrName = WebObjLoginUsrName.textContent;
    
    Log.Message("Actual Login User Name: "+ActualLoginUsrName)
    Log.Message("Login User Name: "+StrUserName)
   
    if(ActualLoginUsrName == "Welcome "+StrUserName):
      Log.Checkpoint("Validation for Successful Login Pass. Login User Name: "+ActualLoginUsrName);
    else:
      Log.Error("Validation for Successful Login Failed. Actual User Name: "+ActualLoginUsrName+", Expected  User Name: "+StrUserName);
    
def LoginWithEmptyUserName():
  StrPassword = str(Project.Variables.VariableByName['Password']);
  BrowserFactry.InitBrowser();
    
  WebObjPassword = Login.Password();
  Sys.Desktop.Keys(StrPassword);
  
  WebObjLogin = Login.Login();
  WebObjLogin.Click()
  
  WebObjErrorMsg = Login.ErrorMessage();
  
  ActualErrorMsg = WebObjErrorMsg.textContent;
  Log.Message("Actual Error Msg: "+ActualErrorMsg)
  
  ExpectedErrorMsg =  Login.GetValueFromOR("ErrMsg","UserEmpty");
  Log.Message("Expected Error Msg: "+ExpectedErrorMsg)
  
  if(ActualErrorMsg == ExpectedErrorMsg):
    Log.Checkpoint("Validation for User Name Empty Error Message Pass. Error Msg:"+ActualErrorMsg);
  else:
    Log.Error("Validation for User Name Empty Error Message Failed. Actual Error Msg: "+ActualErrorMsg+", Expected Error Msg: "+ExpectedErrorMsg);
  
def LoginWithEmptyPassword():
  StrUserName = str(Project.Variables.VariableByName['UserName']);

  BrowserFactry.InitBrowser();
  
  WebObjUserName = Login.UserName();
  Sys.Desktop.Keys(StrUserName);
  
  WebObjLogin = Login.Login();
  WebObjLogin.Click()

  WebObjErrorMsg = Login.ErrorMessage();
  
  ActualErrorMsg = WebObjErrorMsg.textContent;
  Log.Message("Actual Error Msg: "+ActualErrorMsg)
    
  ExpectedErrorMsg =  Login.GetValueFromOR("ErrMsg","PasswordEmpty");
  Log.Message("Expected Error Msg: "+ExpectedErrorMsg)
  
  if(ActualErrorMsg == ExpectedErrorMsg):
    Log.Checkpoint("Validation for Password Empty Error Message Pass. Error Msg:"+ActualErrorMsg);
  else:
    Log.Error("Validation for Password Empty Error Message Failed. Actual Error Msg: "+ActualErrorMsg+", Expected Error Msg: "+ExpectedErrorMsg);
  
def LoginWithInvalidCredentials(StrUserName,StrPassword):  
  BrowserFactry.InitBrowser();
  
  WebObjUserName = Login.UserName();
  Sys.Desktop.Keys(StrUserName);
  
  WebObjPassword = Login.Password();
  Sys.Desktop.Keys(StrPassword);
  
  WebObjLogin = Login.Login();
  WebObjLogin.Click()
  Waiter.Wait(1,"Wait for Message.")
  
  WebObjErrorMsg = Login.ErrorMessage();
  
  ActualErrorMsg = WebObjErrorMsg.textContent;
  Log.Message("Actual Error Msg: "+ActualErrorMsg)
  
  ExpectedErrorMsg =  Login.GetValueFromOR("ErrMsg","InvalidCredentials");
  Log.Message("Expected Error Msg: "+ExpectedErrorMsg)
   
  if(ActualErrorMsg == ExpectedErrorMsg):
    Log.Checkpoint("Validation for Invalid Credentials Error Message Pass. Error Msg:"+ActualErrorMsg);
  else:
    Log.Error("Validation for Invalid Credentials Error Message Failed. Actual Error Msg: "+ActualErrorMsg+", Expected Error Msg: "+ExpectedErrorMsg);