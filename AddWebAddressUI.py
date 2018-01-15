# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddWebAddressUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgAddAddress(object):
    def setupUi(self, dlgAddAddress):
        dlgAddAddress.setObjectName("dlgAddAddress")
        dlgAddAddress.resize(635, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dlgAddAddress.sizePolicy().hasHeightForWidth())
        dlgAddAddress.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/WebSerTestIcon/browser_window_38.581560283688px_1204645_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlgAddAddress.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(dlgAddAddress)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(dlgAddAddress)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.editWebAddress = QtWidgets.QLineEdit(dlgAddAddress)
        self.editWebAddress.setObjectName("editWebAddress")
        self.horizontalLayout.addWidget(self.editWebAddress)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(dlgAddAddress)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonInsert = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonInsert.sizePolicy().hasHeightForWidth())
        self.buttonInsert.setSizePolicy(sizePolicy)
        self.buttonInsert.setObjectName("buttonInsert")
        self.gridLayout.addWidget(self.buttonInsert, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.listMacros = QtWidgets.QListWidget(self.splitter)
        self.listMacros.setObjectName("listMacros")
        self.textMacrosLog = QtWidgets.QTextBrowser(self.splitter)
        self.textMacrosLog.setObjectName("textMacrosLog")
        self.gridLayout.addWidget(self.splitter, 0, 0, 2, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.buttonSave = QtWidgets.QPushButton(dlgAddAddress)
        self.buttonSave.setObjectName("buttonSave")
        self.horizontalLayout_2.addWidget(self.buttonSave)
        self.buttonCancel = QtWidgets.QPushButton(dlgAddAddress)
        self.buttonCancel.setObjectName("buttonCancel")
        self.horizontalLayout_2.addWidget(self.buttonCancel)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.retranslateUi(dlgAddAddress)
        self.buttonCancel.clicked['bool'].connect(dlgAddAddress.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgAddAddress)

    def retranslateUi(self, dlgAddAddress):
        _translate = QtCore.QCoreApplication.translate
        dlgAddAddress.setWindowTitle(_translate("dlgAddAddress", "添加Web地址"))
        self.label.setText(_translate("dlgAddAddress", "Web地址："))
        self.groupBox.setTitle(_translate("dlgAddAddress", "宏列表"))
        self.buttonInsert.setText(_translate("dlgAddAddress", "插入宏"))
        self.buttonSave.setText(_translate("dlgAddAddress", "保存"))
        self.buttonCancel.setText(_translate("dlgAddAddress", "取消"))

import Resources_rc
