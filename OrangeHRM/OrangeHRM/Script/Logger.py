﻿def Error(strMsg):
  pass;
  
def Message(strMsg):
  pass;

def Warning(strMsg):
  pass;
  
def CheckPoint(strMsg):
  ObjAttributes = Log.CreateNewAttributes()
  ObjAttributes.Bold = True
  ObjAttributes.BackColor =  clYellow
  Log.Checkpoint(strMsg,'', pmNormal, ObjAttributes)