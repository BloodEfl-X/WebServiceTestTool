# -*- coding: utf-8 -*-

import sys
import time
import WebServiceTestTool.FunOperatLog as FunLog
from PyQt5 import QtWidgets, QtCore, QtGui
from WebServiceTestTool.WebServiceToolUI import Ui_MainWindow
from WebServiceTestTool.WebToolAbout import WebToolAboutDlg
from WebServiceTestTool.WebServiceClient import WebServiceClint
from WebServiceTestTool.WebToolConfig import WebToolConfig
from WebServiceTestTool.FunLogWin import FunLogDlg


class WebServiceToolWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(WebServiceToolWin, self).__init__()
        self.setupUi(self)
        self.webClient = WebServiceClint()
        self.configDlg = WebToolConfig()
        self.funLogDlg = FunLogDlg()

        self.menuAbout.triggered.connect(self.show_aboutdlg)
        self.buttonLoad.clicked.connect(self.load_fun_list)
        self.tableFunList.itemSelectionChanged.connect(self.item_change)
        self.tableFunList.itemClicked.connect(self.click_fun_list_item)
        self.buttonCallFun.clicked.connect(self.execute_web_fun)
        self.comURL.currentIndexChanged.connect(self.address_combox_change)
        self.meunSetConfig.triggered.connect(self.show_config_dlg)
        self.buttonFunlog.clicked["bool"].connect(self.open_fun_log)

        self.win_center()
        self.init_win_info()
        self.init_address_combox()

    def win_center(self):
        frameRect = self.frameGeometry()
        sreenCenter = QtWidgets.QDesktopWidget().availableGeometry().center()
        frameRect.moveCenter(sreenCenter)
        self.move(frameRect.topLeft())

    def init_win_info(self):
        settingConfig = QtCore.QSettings(self.configDlg.configFileName, QtCore.QSettings.IniFormat)
        winSize = settingConfig.value("WinInfo/WinSize")
        if(winSize is not None and isinstance(winSize, QtCore.QSize) and winSize.isValid()):
            self.resize(winSize)

    def init_address_combox(self):
        self.comURL.clear()
        settingConfig = QtCore.QSettings(self.configDlg.configFileName, QtCore.QSettings.IniFormat)
        addressList = settingConfig.value("WebServiceInfo/WebServiceAddress")
        webIp = settingConfig.value("WebServiceInfo/WebServiceIP")
        port = settingConfig.value("WebServiceInfo/Port")
        self.comURL.addItem("")
        for address in addressList:
            address = address.replace("$WebIP$", webIp)
            address = address.replace("$Port$", port)
            self.comURL.addItem(address)

    def show_aboutdlg(self):
        adoutDlg = WebToolAboutDlg()
        adoutDlg.exec_()

    def show_config_dlg(self):
        self.configDlg.init_config_info()
        if(self.configDlg.exec_() == 1):
            self.init_address_combox()

    def load_fun_list(self):
        self.tableFunList.setRowCount(0)

        webAddress = self.comURL.currentText()
        if(webAddress == None or len(webAddress) == 0):
            return

        errorInfo, result = self.webClient.load_web_info(webAddress)
        if(result == False):
            self.textReturnValue.setPlainText(errorInfo)
            return

        funCount = len(self.webClient.webFunList)
        self.tableFunList.setRowCount(funCount)

        rowIndex = 0
        for webFunName in self.webClient.webFunList:
            self.tableFunList.setItem(rowIndex, 0, QtWidgets.QTableWidgetItem(webFunName))

            item = QtWidgets.QTableWidgetItem("查看")
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setForeground(QtCore.Qt.blue)
            self.tableFunList.setItem(rowIndex, 1, item)

            rowIndex += 1

        self.statusbar.showMessage("")

    def item_change(self):
        self.tabParamList.clear()
        self.textReturnValue.clear()

        item = self.tableFunList.selectedItems()
        if (item == None or len(item) == 0):
            return

        webFunName = item[0].text()

        for param in self.webClient.webFunList[webFunName]:
            paramEdit = QtWidgets.QTextEdit()
            # 设置文本框只接受纯文本，不接受文本格式（比如颜色）
            paramEdit.setAcceptRichText(False)
            self.tabParamList.addTab(paramEdit, param)

        self.statusbar.showMessage("")

    def execute_web_fun(self):
        '''

        :return:
        '''

        selectItem = self.tableFunList.selectedItems()
        if(selectItem == None or len(selectItem) == 0):
            return

        webFunName = selectItem[0].text()

        paramLsit = {}
        for tabIndex in range(self.tabParamList.count()):
            editParam = self.tabParamList.widget(tabIndex)
            paramName = self.tabParamList.tabText(tabIndex)
            paramLsit[paramName] = editParam.toPlainText()

        self.statusbar.showMessage("开始调用......")
        beginTiem = time.perf_counter()

        returnValue = self.webClient.execute_web_fun(webFunName, **paramLsit)

        self.textReturnValue.setPlainText(returnValue)

        endTiem = time.perf_counter()
        self.statusbar.showMessage("调用结束，耗时：%0.3f秒" % (endTiem - beginTiem))

        messageList = {}
        messageList["funName"] = webFunName
        messageList["webAddress"] = self.comURL.currentText()
        messageList["prarms"] = paramLsit
        self.record_log(**messageList)

    def address_combox_change(self):
        self.load_fun_list()

    def click_fun_list_item(self, item):
        if(item == None):
            return

        colIndex = item.column()
        itemText = item.text()
        if(colIndex == 1 and itemText == "查看"):
            QtWidgets.QMessageBox.information(self, "提示信息", "函数文档功能还未完成！", QtWidgets.QMessageBox.Cancel)

    def closeEvent(self, event):
        settingConfig = QtCore.QSettings(self.configDlg.configFileName, QtCore.QSettings.IniFormat)
        winSize = self.size()
        settingConfig.beginGroup("WinInfo")
        settingConfig.setValue("WinSize", winSize)
        settingConfig.endGroup()

        self.funLogDlg.close()

        event.accept()

    def record_log(self, **messageList):
        FunLog.logging.info(str(messageList))

    def open_fun_log(self):
        self.funLogDlg.load_log_file_list()
        self.funLogDlg.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    win = WebServiceToolWin()
    win.show()

    sys.exit(app.exec_())