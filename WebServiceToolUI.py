# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WebServiceToolUI.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(746, 703)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/WebSerTestIcon/browser_window_38.581560283688px_1204645_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(38, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.layoutWidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comURL = QtWidgets.QComboBox(self.widget_3)
        self.comURL.setEditable(True)
        self.comURL.setObjectName("comURL")
        self.horizontalLayout_2.addWidget(self.comURL)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.splitter = QtWidgets.QSplitter(self.widget_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableFunList = QtWidgets.QTableWidget(self.groupBox)
        # self.tableFunList.setMinimumSize(150, 100)
        self.tableFunList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableFunList.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableFunList.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableFunList.setAlternatingRowColors(True)
        self.tableFunList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableFunList.setObjectName("tableFunList")
        self.tableFunList.setColumnCount(2)
        self.tableFunList.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch) # 将table的第一列设置为自适应
        self.tableFunList.horizontalHeader().setMinimumSectionSize(50)
        self.tableFunList.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableFunList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableFunList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFunList.setHorizontalHeaderItem(1, item)
        # self.tableFunList.setColumnWidth(1, 80)
        self.gridLayout_2.addWidget(self.tableFunList, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabParamList = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabParamList.setObjectName("tabParamList")
        self.gridLayout_3.addWidget(self.tabParamList, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.splitter)
        self.splitter.raise_()
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_7 = QtWidgets.QWidget(self.layoutWidget)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonLoad = QtWidgets.QPushButton(self.widget_7)
        self.buttonLoad.setObjectName("buttonLoad")
        self.verticalLayout_2.addWidget(self.buttonLoad)
        self.buttonCallFun = QtWidgets.QPushButton(self.widget_7)
        self.buttonCallFun.setObjectName("buttonCallFun")
        self.verticalLayout_2.addWidget(self.buttonCallFun)
        self.buttonFunlog = QtWidgets.QPushButton(self.widget_7)
        self.buttonFunlog.setEnabled(True)
        self.buttonFunlog.setObjectName("buttonFunlog")
        self.verticalLayout_2.addWidget(self.buttonFunlog)
        spacerItem = QtWidgets.QSpacerItem(20, 228, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.widget_7)
        self.widget_4 = QtWidgets.QWidget(self.splitter_3)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget_4)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textReturnValue = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textReturnValue.setMinimumSize(100, 100)
        self.textReturnValue.setObjectName("textReturnValue")
        self.gridLayout_5.addWidget(self.textReturnValue, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.splitter_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 746, 37))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.meunSetConfig = QtWidgets.QAction(MainWindow)
        self.meunSetConfig.setObjectName("meunSetConfig")
        self.menuAbout = QtWidgets.QAction(MainWindow)
        self.menuAbout.setObjectName("menuAbout")
        self.menuFile.addAction(self.meunSetConfig)
        self.menuHelp.addAction(self.menuAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabParamList.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WebServiceTestTool"))
        self.label.setText(_translate("MainWindow", "地址："))
        self.groupBox.setTitle(_translate("MainWindow", "接口："))
        item = self.tableFunList.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "函数名称"))
        item = self.tableFunList.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "操作"))
        self.groupBox_2.setTitle(_translate("MainWindow", "参数："))
        # self.tabParamList.setTabText(self.tabParamList.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        # self.tabParamList.setTabText(self.tabParamList.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.buttonLoad.setText(_translate("MainWindow", "加载"))
        self.buttonCallFun.setText(_translate("MainWindow", "调用"))
        self.buttonCallFun.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.buttonFunlog.setText(_translate("MainWindow", "调用日志"))
        self.groupBox_5.setTitle(_translate("MainWindow", "输出："))
        self.menuFile.setTitle(_translate("MainWindow", "文件"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助"))
        self.meunSetConfig.setText(_translate("MainWindow", "设置"))
        self.menuAbout.setText(_translate("MainWindow", "关于"))

import Resources_rc