# -*- coding: utf-8 -*-

import os
from PyQt5 import QtWidgets, QtCore
from WebServiceTestTool.WebToolConfigUI import Ui_dlgConfig
from WebServiceTestTool.AddWebAddress import AddWebAddressDlg

class WebToolConfig(QtWidgets.QDialog, Ui_dlgConfig):
    def __init__(self):
        super(WebToolConfig, self).__init__()
        self.setupUi(self)
        self.configFileName = "WebToolConfig.ini"
        self.wsZemrAddressList = [
            "http://$WebIP$/wsZEMR/wsZEMR.dll?Handler=GenBaseEMRWSDL",
            "http://$WebIP$/wsZEMR/wsZEMR.dll?Handler=GenClinicPathWSDL",
            "http://$WebIP$/wsZEMR/wsZEMR.dll?Handler=GenCommonWSDL",
            "http://$WebIP$/wsZEMR/wsZEMR.dll?Handler=GenDoctorConsulationWSDL",
            "http://$WebIP$/wsZEMR/wsZEMR.dll?Handler=GenEMRUserWSDL",
            "http://$WebIP$/wsZEMR/wsZEMR.dll?Handler=GenEventRegisterWSDL",
            "http://$WebIP$/wsZEMR/wsZEMR.dll?Handler=GenHQMSWSDL",
            "http://$WebIP$/wsZEMR/wsZEMR.dll?Handler=GenLisPacsWSDL",
            "http://$WebIP$/wsZEMR/wsZEMR.dll?Handler=GenNurseEMRWSDL",
            "http://$WebIP$/wsZEMR/wsZEMR.dll?Handler=GenPatientWSDL",
            "http://$WebIP$/wsZEMR/wsZEMR.dll?Handler=GenPatientDiagnosisWSDL",
            "http://$WebIP$/wsZEMR/wsZEMR.dll?Handler=GenPatientEMRWSDL",
            "http://$WebIP$/wsZEMR/wsZEMR.dll?Handler=GenSegmentOwnerWSDL",
            "http://$WebIP$/wsZEMR/wsZEMR.dll?Handler=GenTemperatureWSDL",
            "http://$WebIP$/wsZEMR/wsZEMR.dll?Handler=GenTransBloodRecordWSDL",
            "http://$WebIP$/wsZEMR/wsZEMR.dll?Handler=GenwstemperatureWSDL"
        ]

        if(not os.path.exists(self.configFileName)):
            settingConfig = QtCore.QSettings(self.configFileName, QtCore.QSettings.IniFormat)
            settingConfig.beginGroup("WebServiceInfo")
            settingConfig.setValue("WebServiceIP", "192.168.1.48")
            settingConfig.setValue("Port", "80")
            settingConfig.setValue("WebServiceAddress", self.wsZemrAddressList)
            settingConfig.endGroup()

        self.buttonAddAddress.clicked.connect(self.add_web_address)
        self.buttonBox.accepted.connect(self.save_config_info)
        self.tableWebAddress.itemDoubleClicked.connect(self.itemd_double_click)

    def init_config_info(self):
        settingConfig = QtCore.QSettings(self.configFileName, QtCore.QSettings.IniFormat)

        webIp = settingConfig.value("WebServiceInfo/WebServiceIP")
        port =settingConfig.value("WebServiceInfo/Port")
        self.editWebIp.setText(webIp)
        self.editPort.setText(port)

        webAddressList = settingConfig.value("WebServiceInfo/WebServiceAddress")
        self.tableWebAddress.setRowCount(len(webAddressList))
        itemIndex = 0
        for webAddress in webAddressList:
            self.tableWebAddress.setItem(itemIndex, 0, QtWidgets.QTableWidgetItem(webAddress))
            item = QtWidgets.QTableWidgetItem("删除")
            item.setToolTip("双击删除")
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setForeground(QtCore.Qt.blue)
            self.tableWebAddress.setItem(itemIndex, 1, item)
            itemIndex += 1

    def save_config_info(self):
        settingConfig = QtCore.QSettings(self.configFileName, QtCore.QSettings.IniFormat)

        webIp = self.editWebIp.text()
        port = self.editPort.text()
        webAddressList = []
        for rowIndex in range(self.tableWebAddress.rowCount()):
            item = self.tableWebAddress.item(rowIndex, 0)
            webAddressList.append(item.text())

        settingConfig.beginGroup("WebServiceInfo")
        settingConfig.setValue("WebServiceIP", webIp)
        settingConfig.setValue("Port", port)
        settingConfig.setValue("WebServiceAddress", webAddressList)
        settingConfig.endGroup()

        self.accept()

    def add_web_address(self):
        dlgAddAddress = AddWebAddressDlg()
        if(dlgAddAddress.exec_() == 1):
            self.tableWebAddress.insertRow(0)
            self.tableWebAddress.setItem(0, 0, QtWidgets.QTableWidgetItem(dlgAddAddress.WebServiceAddres))
            item = QtWidgets.QTableWidgetItem("删除")
            item.setToolTip("双击删除")
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setForeground(QtCore.Qt.blue)
            self.tableWebAddress.setItem(0, 1, item)

    def itemd_double_click(self, item):
        if(item == None):
            return

        colIndex = item.column()
        rowIndex = item.row()
        if(colIndex == 0):
            dlgAddAddress = AddWebAddressDlg()
            dlgAddAddress.editWebAddress.setText(item.text())
            if(dlgAddAddress.exec_() == 1):
                item.setText(dlgAddAddress.WebServiceAddres)
        elif(colIndex == 1 and item.text() == "删除"):
            self.tableWebAddress.removeRow(rowIndex)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlg = WebToolConfig()
    dlg.init_config_info()
    dlg.show()
    sys.exit(app.exec_())