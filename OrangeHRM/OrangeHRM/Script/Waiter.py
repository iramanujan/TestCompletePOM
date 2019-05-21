import BrowserFactry
import DateTime
import WebElement

def WaitTillDocumentReady():
	IsDocumentReady = False;
	TimeElapsed =  int(Project.Variables.VariableByName['TimeElapsed']);
	PageLoadTimeOut =  int(Project.Variables.VariableByName['PageLoadTimeOut']);
	ObjPage = BrowserFactry.GetPageObject();
	TimeStarted = DateTime.GetCurrentTime();
	#Waiter.Wait(1,"Wait For Page Load Completely")
	#if((ObjPage.contentDocument is not None) or (ObjPage.contentDocument.readyState == "complete")):
	  #IsDocumentReady = True
	  
	while((ObjPage.contentDocument is None) or (ObjPage.contentDocument.readyState != "complete")):
		if(TimeElapsed > PageLoadTimeOut):
		  Log.Message("Page Object is not ready")
		  return IsDocumentReady
		ObjPage = BrowserFactry.GetPageObject();
		TimeElapsed = DateTime.GetTimeDiffInMinutes(TimeStarted,DateTime.GetCurrentTime())
		IsDocumentReady = True

	return IsDocumentReady;
	
def Wait(TimeInSec,Msg=""):
  aqUtils.Delay(1000*TimeInSec,Msg);
  
def Synchronization(FindBy, Value, All=False,TimeOutInMin=int(Project.Variables.VariableByName['TimeOutInMin']),PollingEveryInSec=int(Project.Variables.VariableByName['PollingEveryInSec'])):
  webElement = None;
  TimeStarted = DateTime.GetCurrentTime();
  TimeElapsed = str(Project.Variables.VariableByName['TimeElapsed']);
  webElement =  WebElement.FindElement(FindBy,Value,All);
  while((webElement is None) and (int(TimeElapsed) < int(TimeOutInMin))):
    Waiter.Wait(PollingEveryInSec,"Waiting for Object, Find By: {"+FindBy+"}, Value: {"+Value+"}");
    if(TimeElapsed == 3):
      Log.Message("It's been 3 minutes finding this object, Please check app stat");
    webElement = WebElement.FindElement(FindBy,Value,All);
    TimeElapsed = DateTime.GetTimeDiffInMinutes(TimeStarted,DateTime.GetCurrentTime())

  return webElement;