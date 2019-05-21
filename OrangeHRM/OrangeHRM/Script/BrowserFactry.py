﻿import Waiter

AppUrl      =   str(Project.Variables.VariableByName['ApplicationURL']);
PageUrl     =   str(Project.Variables.VariableByName['PageURL']);
TestBrowser =   str(Project.Variables.VariableByName['TestBrowser']);
  
def GetPageObject():
  PageObj = Sys.Browser(TestBrowser).Page(PageUrl)
  return PageObj
  
def GetPageTitle():
  strPageTitle = GetPageObject().contentDocument.title
  Log.Message("Page Title: "+ strPageTitle);
  return strPageTitle
  
def GetPageUrl():
  strPageUrl = GetPageObject().contentDocument.URL
  Log.Message("Page URL "+ strPageUrl);
  return strPageUrl

  
def InitBrowser():
  if(TestBrowser == "iexplore"):
    BrowserFactry.LaunchIE();
  elif(TestBrowser == "chrome"):
    BrowserFactry.LaunchChrome();
  else:
    Log.Message("")
    
  return GetPageObject() if(Waiter.WaitTillDocumentReady()) else None;
    
def LaunchChrome():
  Browsers.Item[TestBrowser].RunOptions = "--incognito --disable-session-crashed-bubble --disable-infobars --disable-password-generation --clear-token-service --ignore-autocomplete-off-autofill";
  Browsers.Item[TestBrowser].Run(AppUrl);
  #Log Browser version
  Log.Message("Browser version: " + aqConvert.VarToStr(Browsers.Item[TestBrowser].Version));
  #Log Browser Description:
  Log.Message("Browser Description: " + Browsers.Item[TestBrowser].Description);
  #Maximize Browser    
  Sys.Browser().BrowserWindow(0).Maximize()

         
def LaunchIE():
  Browsers.Item[TestBrowser].Run(AppUrl);
  #Log Browser version
  Log.Message("Browser version: " + aqConvert.VarToStr(Browsers.Item[TestBrowser].Version));
  #Log Browser Description:
  Log.Message("Browser Description: " + Browsers.Item[TestBrowser].Description);
  #Maximize Browser   
  Sys.Browser().BrowserWindow(0).Maximize()
  #Handle website’s security certificate.
  try:
    Overridelink = BrowserFactry.GetPageObject().EvaluateXPath("//a[@id='overridelink']")
    if(Overridelink is not None):
      Overridelink[0].Click();
      aqUtils.Delay(2000)
    else:
      Overridelink = BrowserFactry.GetPageObject().EvaluateXPath("//a[@id='overridelink']")
      if(Overridelink is not None):
        Overridelink[0].Click()
  except Exception as e:
    Log.Message(str(e))
      
def RefreshPage():
  GetPageObject().Keys("[F5]")
  return GetPageObject() if(Waiter.WaitTillDocumentReady()) else None;