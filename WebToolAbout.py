# -*- coding: utf-8 -*-

from WebServiceTestTool.WebToolAboutUI import Ui_Dialog
from PyQt5 import QtWidgets, QtGui

class WebToolAboutDlg(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(WebToolAboutDlg, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dlg = WebToolAboutDlg()
    dlg.show()
    sys.exit(app.exec_())
