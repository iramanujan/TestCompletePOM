﻿import BrowserFactry
import DateTime
import Waiter

def GetWebElement(FindBy, Value, All=False):
  WebElement = None;  
  ObjAttributes = Log.CreateNewAttributes()
  ObjAttributes.Bold = True
  ObjAttributes.BackColor = clLtGray
  Log.Message("Search Object With, How: {"+FindBy+"}, Using: {"+Value+"}",'', pmNormal, ObjAttributes);
  return  Waiter.Synchronization(FindBy,Value,All);

def FindElement(FindBy, Value, All=False):
  WebElement = None;
  if(FindBy == "cssSelector" and All == True):
    WebElement =FindElementsByQuerySelector(Value)
  elif(FindBy == "xpath" and All == True):
    WebElement =FindElementsByXpath(Value)
  elif(FindBy == "cssSelector" and All == False):
    WebElement =FindElementByQuerySelector(Value)
  elif(FindBy == "xpath" and All == False):
    WebElement =FindElementByXpath(Value);
  else:
    WebElement = None;
  return WebElement;
     
def FindElementByXpath(value): 
  webElement = None;
  try:
    webElement = BrowserFactry.GetPageObject().EvaluateXPath(value)[0];
  except:
    webElement = None;
  finally:
    return  webElement
    
def FindElementByQuerySelector(value):  
  webElement = None;
  try:
    webElement = BrowserFactry.GetPageObject().QuerySelector(value);
  except:
    webElement = None;
  finally:
    return  webElement
  
def FindElementsByXpath(value):  
  webElements = None;
  try:
    webElements = BrowserFactry.GetPageObject().EvaluateXPath(value);
  except:
    webElements = None;
  finally:
    return  webElements
    
def FindElementsByQuerySelector(value):  
  webElements = None;
  try:
   webElements = BrowserFactry.GetPageObject().QuerySelectorAll(value);
  except:
    webElements = None;
  finally:
    return  webElements
  
def IsVisible(WebElement):
  if(WebElement is None):return False;
  else:
  	Height = WebElement.offsetHeight
  	Width  = WebElement.offsetHeight
  return True if(Height > 0 or Width > 0)else False; 
