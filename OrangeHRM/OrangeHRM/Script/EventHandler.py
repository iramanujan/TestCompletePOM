import Helper

def EventControl1_OnStartTest(Sender):
    Helper.closeAllBrowser()

def EventControl2_OnStopTest(Sender):
    Helper.closeAllBrowser()
