﻿import datetime
import time
 
def GetCurrentTime():
	return datetime.datetime.now().replace(microsecond=0);
		
def GetTimeDiffInSecond(StartTime,EndTime):
  return (EndTime-StartTime).total_seconds()
	  
def GetTimeDiffInMinutes(StartTime,EndTime):
  return ((EndTime-StartTime).total_seconds()/60);

def GetCurrTimeHMS():
  currentTime = datetime.datetime.now().strftime("%I:%M:%S")
  return currentTime
  
def GetTimeStamp():
  timeStamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H-%M-%S')
  return timeStamp
