﻿def GetColumnPositionByName(WebElement,ColumnName,strAttributeName = "data-title"):
  ColumnTitle = ""
  WebElementChildren = WebElement.children
  for index in range ( 0 , WebElement.childElementCount):
    CurrentNode = WebElementChildren.item(index);
    if(CurrentNode.hasAttribute(strAttributeName)):
      ColumnTitle =  CurrentNode.getAttribute(strAttributeName)
      if(ColumnName.strip() == ColumnTitle.strip()):
        Log.Checkpoint("Column Position is "+str(index+1)+"Column Name: "+ColumnName)          
        return (index+1);
      else:
        Log.Error("No Column Found: "+ColumnName)   
        
def GetInnerText(webElement):
  return webElement.innerText;

def GetContentText(webElement):
  return webElement.contentText;

def GetTextContent(webElement):
  return webElement.textContent
  
def GetAttribute(webElement, strAttributeName):
  return webElement.getAttribute(strAttributeName) if(webElement.hasAttribute(strAttributeName)) else None;