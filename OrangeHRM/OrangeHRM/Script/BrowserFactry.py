import Waiter
import Helper
from BrowserProperties import BrowserProperties 

AppUrl      =   str(Project.Variables.VariableByName['ApplicationURL']);
PageUrl     =   str(Project.Variables.VariableByName['PageURL']);
ObjBrowserProperties = BrowserProperties()
    
def GetPageObject():  
  TestBrowser = ObjBrowserProperties.GetTestBrowser();
  PageObj = Sys.Browser(TestBrowser).Page(PageUrl)
  return PageObj if(PageObj is not None) else Log.Error("Page Object Is None");
  
def GetPageTitle():
  strPageTitle = GetPageObject().contentDocument.title
  return strPageTitle if(strPageTitle is not None) else Log.Error("Page Title Is None");
  
def GetPageUrl():
  strPageUrl = GetPageObject().contentDocument.URL
  return strPageUrl if(strPageUrl is not None) else Log.Error("Page URL Is None");

def InitBrowser():
  TestBrowser = ObjBrowserProperties.GetTestBrowser();
  if(TestBrowser == "iexplore"):
    BrowserFactry.LaunchIE();
  elif(TestBrowser == "chrome"):
    BrowserFactry.LaunchChrome();
  elif(TestBrowser == "firefox"):
    BrowserFactry.LaunchFirefox();
  elif(TestBrowser == 'edge'):
    BrowserFactry.LaunchEdge()
  else:
    Log.Message("No Test Browser Found...");
    Runner.Stop();
    
  return GetPageObject() if(Waiter.WaitTillDocumentReady()) else None;
    
def LaunchChrome():
  TestBrowser = ObjBrowserProperties.GetTestBrowser();
  Browsers.Item[TestBrowser].RunOptions = "--incognito --disable-session-crashed-bubble --disable-infobars --disable-password-generation --clear-token-service --ignore-autocomplete-off-autofill";
  Browsers.Item[TestBrowser].Run(AppUrl);
  #Log Browser version
  Log.Message("Browser version: " + aqConvert.VarToStr(Browsers.Item[TestBrowser].Version));
  #Log Browser Description:
  Log.Message("Browser Description: " + Browsers.Item[TestBrowser].Description);
  #Maximize Browser    
  Sys.Browser().BrowserWindow(0).Maximize()

def LaunchFirefox():
  TestBrowser = ObjBrowserProperties.GetTestBrowser();
  Browsers.Item[TestBrowser].Run(AppUrl);
  #Log Browser version
  Log.Message("Browser version: " + aqConvert.VarToStr(Browsers.Item[TestBrowser].Version));
  #Log Browser Description:
  Log.Message("Browser Description: " + Browsers.Item[TestBrowser].Description);
  #Maximize Browser    
  Sys.Browser().BrowserWindow(0).Maximize()
  
def LaunchIE():
  TestBrowser = ObjBrowserProperties.GetTestBrowser();
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

def LaunchEdge():
  TestBrowser = ObjBrowserProperties.GetTestBrowser();
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