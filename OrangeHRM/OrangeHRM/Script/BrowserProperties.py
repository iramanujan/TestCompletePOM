import Helper
class BrowserProperties:
  TestBrowser = None;
  def __init__(self):
    pass;
   
  def GetTestBrowser(self):
    if(BrowserProperties.TestBrowser == None or Project.Variables.IsRunOnDefaultBrowser):
      BrowserProperties.TestBrowser = Project.Variables.DefaultBrowser;
      return BrowserProperties.TestBrowser
    else: 
      Path = Project.Path+"TempStore\TestBrowser.txt"
      Helper.OverWrieFile(Path,BrowserProperties.TestBrowser)
      return BrowserProperties.TestBrowser
      
  def SetTestBrowser(self):
    if(Project.Variables.IsRunOnDefaultBrowser):
      BrowserProperties.TestBrowser = Project.Variables.DefaultBrowser;
    else:
      TestBrowserList = Helper.ConvertStringIntoList(Project.Variables.TestBrowserList,";")
      Path = Project.Path+"TempStore\TestBrowser.txt"
      PreviousTestBrowser = Helper.ReadFile(Path)
      BrowserProperties.TestBrowser = Helper.SelectRandomValueFromListWithExclusion(TestBrowserList,PreviousTestBrowser);
    
  def GetDefaultTestBrowser():
   return  Project.Variables.DefaultBrowser;
    
  def GetBrowserVersion(self):
    strVersion = Browsers.Item[TestBrowser].Version;
    Log.Message("Browser Description: " + strVersion);
    return strVersion

  def BrowserDescription(self):
    strDescription = Browsers.Item[TestBrowser].Description;
    Log.Message("Browser Description: " + strDescription);
    return strDescription;