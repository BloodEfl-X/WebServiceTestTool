# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WebTesetToolAbout.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(531, 264)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/WebSerTestIcon/browser_window_38.581560283688px_1204645_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/WebSerTestIcon/browser_window_154.32624113475px_1204645_easyicon.net.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 3, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 1, 1, 2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(141, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 4)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "版本："))
        self.label_6.setText(_translate("Dialog", "v1.0"))
        self.label_3.setText(_translate("Dialog", "作者："))
        self.label_7.setText(_translate("Dialog", "许晓晨"))
        self.label_4.setText(_translate("Dialog", "创建日期："))
        self.label_8.setText(_translate("Dialog", "2017-09"))
        self.label_9.setText(_translate("Dialog", "简介："))
        self.label_10.setText(_translate("Dialog", "主要用于测试WebCService服务是否有效"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-family:Microsoft Yahei;\">WebService测试工具</span></p></body></html>"))

import WebServiceTestTool.Resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    dlg = QtWidgets.QDialog()
    ui.setupUi(dlg)
    dlg.show()
    sys.exit(app.exec_())