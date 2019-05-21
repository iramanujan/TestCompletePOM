def GetColumnPositionByName(WebElement,ColumnName):
  ColumnTitle = ""
  WebElementChildren = WebElement.children
  for index in range ( 0 , WebElement.childElementCount):
    CurrentNode = WebElementChildren.item(index);
    if(CurrentNode.hasAttribute("data-title")):
      ColumnTitle =  CurrentNode.getAttribute("data-title")
      if(ColumnName.strip() == ColumnTitle.strip()):
        Log.Checkpoint("Column Position is "+str(index+1)+"Column Name: "+ColumnName)          
        return (index+1);
      else:
        Log.Error("No Column Found: "+ColumnName)   