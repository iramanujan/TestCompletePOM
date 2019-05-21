import UsersSteps

def ValidateSystemUserPage():
  UsersSteps.NavigateToSystemUserPage();
  
def ValidateSortingForStatus(strStatus):
  UsersSteps.NavigateToSystemUserPage();
  UsersSteps.VerifySorting(strStatus)
  
def ValidateSortingForUserRole(strUserRole):
  UsersSteps.NavigateToSystemUserPage();
  UsersSteps.VerifySorting(strUserRole)

def ValidateSortingForEmployeeName(strEmployeeName):
  UsersSteps.NavigateToSystemUserPage();
  UsersSteps.VerifySorting(strEmployeeName)

def ValidateSortingForUsername(strUsername):
  UsersSteps.NavigateToSystemUserPage();
  UsersSteps.VerifySorting(strUsername)