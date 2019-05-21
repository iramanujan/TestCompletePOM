ObjPage = Sys.Browser("iexplore").Page("https://opensource-demo.orangehrmlive.com/");
  
def FindElementByXpath(value):
  webElement = ObjPage.EvaluateXPath(value)[0];
  return webElement
    
def FindElementByQuerySelector(value):
  webElement = ObjPage.QuerySelector(value);
  return webElement
  
def FindElementsByXpath(value):
  webElements = ObjPage.EvaluateXPath(value);
  return webElements
    
def FindElementsByQuerySelector(value):
  webElements = ObjPage.QuerySelectorAll(value);
  return webElements
