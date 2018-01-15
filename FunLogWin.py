# -*- coding: utf-8 -*-

import os
import time
from PyQt5 import QtWidgets, QtCore
from WebServiceTestTool.FunLogUI import Ui_dlgFunLog

class FunLogDlg(QtWidgets.QDialog, Ui_dlgFunLog):
    def __init__(self):
        super(FunLogDlg, self).__init__()
        self.setupUi(self)
        self.logInfoList = []
        self.logDirName = "FunOperatlog"

        self.tableFunInfo.itemSelectionChanged.connect(self.item_change)
        self.combLogList.currentIndexChanged.connect(self.combox_change)

    def read_log_info(self):
        try:
            self.logInfoList.clear()

            logName = self.combLogList.currentText()
            # currentTime = time.strftime("%Y-%m-%d", time.localtime())
            fileName = "%s/%s"% (self.logDirName, logName)
            if(not os.path.exists(fileName)):
                return

            try:
                logFile = open(fileName, "r")
                for line in logFile:
                    line = line.strip()
                    infoList = line.split("$line$")

                    executeFunTime = infoList[0]
                    logInfo = eval(infoList[1])
                    if(not isinstance(logInfo, dict)):
                        continue

                    logInfo["executeFunTime"] = executeFunTime
                    self.logInfoList.append(logInfo)

                self.load_log_info()

            finally:
                logFile.close()

        except Exception as error:
            errorMessage = "读取%s日志文件时出错：%s" % (fileName, str(error))
            QtWidgets.QMessageBox.critical(self, "错误信息", errorMessage, QtWidgets.QMessageBox.Close)

    def load_log_info(self):
        count = len(self.logInfoList)
        self.tableFunInfo.setRowCount(count)
        if(count == 0):
            return

        for rowIndex in range(count):
            logInfo = self.logInfoList[rowIndex]
            self.tableFunInfo.setItem(rowIndex, 0, QtWidgets.QTableWidgetItem(logInfo["funName"]))
            self.tableFunInfo.setItem(rowIndex, 1, QtWidgets.QTableWidgetItem(logInfo["executeFunTime"]))

    def item_change(self):
        self.tabParamInfo.clear()

        rowIndex = self.tableFunInfo.currentRow()
        logInfo = self.logInfoList[rowIndex]
        self.editWebAddress.setText(logInfo["webAddress"])
        paramList = logInfo["prarms"]
        for param in paramList:
            editParam = QtWidgets.QTextEdit()
            editParam.setText(paramList[param])
            editParam.setReadOnly(True)
            self.tabParamInfo.addTab(editParam, param)

    def load_log_file_list(self):
        fileList = os.listdir(self.logDirName)

        logList = []
        for file in fileList:
            if not os.path.isfile("%s/%s"% (self.logDirName, file)):
                continue
            else:
                fileName, fileType = os.path.splitext(file)
                if not fileType == ".log":
                    continue

            logList.append(file)

        self.combLogList.addItems(logList)
        self.combLogList.setCurrentIndex(self.combLogList.count() - 1)

    def combox_change(self):
        self.read_log_info()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlg = FunLogDlg()
    dlg.load_log_file_list()
    dlg.show()
    sys.exit(app.exec_())