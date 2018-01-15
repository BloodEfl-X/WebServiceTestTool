# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui
from WebServiceTestTool.AddWebAddressUI import Ui_dlgAddAddress

class AddWebAddressDlg(QtWidgets.QDialog, Ui_dlgAddAddress):
    def __init__(self):
        super(AddWebAddressDlg, self).__init__()
        self.setupUi(self)

        self.WebServiceAddres = ""
        self.macrosList = {
            "$WebIP$":"Web服务IP地址",
            "$Port$":"Web服务端口号"
        }

        for macros in self.macrosList:
            self.listMacros.addItem(QtWidgets.QListWidgetItem(macros))

        self.buttonSave.clicked["bool"].connect(self.save_web_address)
        self.buttonInsert.clicked["bool"].connect(self.insert_macros)
        self.listMacros.itemSelectionChanged.connect(self.macros_item_change)
        self.listMacros.itemDoubleClicked.connect(self.list_item_double_dlick)

    def save_web_address(self):
        self.WebServiceAddres = self.editWebAddress.text()
        self.accept()

    def insert_macros(self):
        item = self.listMacros.selectedItems()
        if (item == None or len(item) == 0):
            return
        macrosName = item[0].text()

        self.editWebAddress.insert(macrosName)

    def macros_item_change(self):
        item = self.listMacros.selectedItems()
        if(item == None or len(item) == 0):
            return

        macrosName = item[0].text()
        macrosLog = self.macrosList[macrosName]
        self.textMacrosLog.setText(macrosLog)

    def list_item_double_dlick(self, listItem):
        self.insert_macros()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlg = AddWebAddressDlg()
    dlg.show()
    sys.exit(app.exec_())