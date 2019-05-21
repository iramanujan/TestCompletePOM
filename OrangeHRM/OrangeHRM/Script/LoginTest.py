import LoginSteps;

def VerifyLogin():
  LoginSteps.LoginWithValidInput();
  
def VeriftEmptyUserNameErrorMsg():
  LoginSteps.LoginWithEmptyUserName()
    
def VeriftEmptyPasswordErrorMsg():
  LoginSteps.LoginWithEmptyPassword()
    
def VeriftInvalidCredentialsErrorMsg(strUserName,strPassword):
  LoginSteps.LoginWithInvalidCredentials(strUserName,strPassword)