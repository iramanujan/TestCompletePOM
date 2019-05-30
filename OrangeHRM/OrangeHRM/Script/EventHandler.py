import Helper
from BrowserProperties import BrowserProperties 

def EventControl1_OnStartTest(Sender): 
  ObjBrowserProperties = BrowserProperties()
  TestBrowser = ObjBrowserProperties.SetTestBrowser();
  Helper.closeAllBrowser()

def EventControl2_OnStopTest(Sender):
  Log.UnlockEvents()
  if(Project.TestItems.Current == None):return
  intErrCount = Log.ErrCount
  intWarningCount = Log.WrnCount
  Project.Variables.TestExecutedCount
  Project.Variables.TestExecutedCount += 1
#  Log.Message("No of tests executed :" + str(Project.Variables.TestExecutedCount)) 
#  Log.Message("Total Pass Test Cases: "+str(Project.Variables.TestExecutedCount - Log.ErrCount))
#  Log.Message("Total Failed Test Cases: "+str(Log.ErrCount))
  Helper.closeAllBrowser()
