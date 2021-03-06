﻿import WebElement
ObjectRepository = {
                    "UserName": 
                                {
                                  "FindBy"       :   "cssSelector",
                                  "Value"         :   "#txtUsername",
                                  "All"              :   False
                                },

                    "Password": 
                                {
                                  "FindBy"       :   "cssSelector",
                                  "Value"         :   "#txtPassword",
                                  "All"              :   False
                                },
                    "Login": 
                                {
                                  "FindBy"       :   "cssSelector",
                                  "Value"         :   "#btnLogin",
                                  "All"              :   False
                                },
                    "Welcome": 
                                {
                                  "FindBy"       :   "cssSelector",
                                  "Value"         :   "#welcome",
                                  "All"              :   False
                                },   
                    "ErrMsg":   {
                                  "FindBy"                          :     "cssSelector",
                                  "Value"                             :    "#spanMessage",
                                  "All"                                  :     False,
                                  "UserEmpty"                   :     "Username cannot be empty",
                                  "PasswordEmpty"           :     "Password cannot be empty",
                                  "InvalidCredentials"       :    "Invalid credentials"
                                }  
                    } 
                             
                             
def UserName():
  FindBy = GetValueFromOR("UserName","FindBy");
  Value = GetValueFromOR("UserName","Value");
  All = GetValueFromOR("UserName","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  WebObject.value = ""
  WebObject.Click()
  return WebObject
     
def Password():
  FindBy = GetValueFromOR("Password","FindBy");
  Value = GetValueFromOR("Password","Value");
  All = GetValueFromOR("Password","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  WebObject.value = ""
  WebObject.Click()
  return WebObject
     
def Login():
  FindBy = GetValueFromOR("Login","FindBy");
  Value = GetValueFromOR("Login","Value");
  All = GetValueFromOR("Login","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  return WebObject
  
def ErrorMessage():
  FindBy = GetValueFromOR("ErrMsg","FindBy");
  Value = GetValueFromOR("ErrMsg","Value");
  All = GetValueFromOR("ErrMsg","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  return WebObject
  
def GetLoginUserName():
  FindBy = GetValueFromOR("Welcome","FindBy");
  Value = GetValueFromOR("Welcome","Value");
  All = GetValueFromOR("Welcome","All");
  WebObject = WebElement.GetWebElement(FindBy,Value,All)
  WebObject.focus
  return WebObject

def GetValueFromOR(FirstLevelKey, SecoundLevelKey):
  return ObjectRepository[FirstLevelKey][SecoundLevelKey];