﻿import UsersSteps

def ValidateSystemUserPage():
  UsersSteps.NavigateToSystemUserPage();
  
def ValidateSorting(strSortingOn):
  UsersSteps.NavigateToSystemUserPage();
  UsersSteps.VerifySorting(strSortingOn)

def ValidateFilter(strFilterOn):
  UsersSteps.NavigateToSystemUserPage();
  UsersSteps.ApplyFilter(strFilterOn);