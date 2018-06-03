# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\pc_tool.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1172, 833)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.group_box_spi_register = QtWidgets.QGroupBox(self.centralwidget)
        self.group_box_spi_register.setGeometry(QtCore.QRect(10, 10, 1151, 191))
        self.group_box_spi_register.setObjectName("group_box_spi_register")
        self.button_read_spi_reg = QtWidgets.QPushButton(self.group_box_spi_register)
        self.button_read_spi_reg.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.button_read_spi_reg.setObjectName("button_read_spi_reg")
        self.group_box_cambridge_memory = QtWidgets.QGroupBox(self.centralwidget)
        self.group_box_cambridge_memory.setGeometry(QtCore.QRect(10, 210, 1151, 581))
        self.group_box_cambridge_memory.setObjectName("group_box_cambridge_memory")
        self.tablewidget_cambridge_mem = QtWidgets.QTableWidget(self.group_box_cambridge_memory)
        self.tablewidget_cambridge_mem.setGeometry(QtCore.QRect(10, 70, 1131, 501))
        self.tablewidget_cambridge_mem.setObjectName("tablewidget_cambridge_mem")
        self.tablewidget_cambridge_mem.setColumnCount(8)
        self.tablewidget_cambridge_mem.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_cambridge_mem.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_cambridge_mem.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_cambridge_mem.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_cambridge_mem.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_cambridge_mem.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_cambridge_mem.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_cambridge_mem.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_cambridge_mem.setHorizontalHeaderItem(7, item)
        self.button_read_cambridge_mem = QtWidgets.QPushButton(self.group_box_cambridge_memory)
        self.button_read_cambridge_mem.setGeometry(QtCore.QRect(230, 30, 93, 28))
        self.button_read_cambridge_mem.setObjectName("button_read_cambridge_mem")
        self.lineedit_address = QtWidgets.QLineEdit(self.group_box_cambridge_memory)
        self.lineedit_address.setGeometry(QtCore.QRect(110, 30, 113, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineedit_address.sizePolicy().hasHeightForWidth())
        self.lineedit_address.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineedit_address.setFont(font)
        self.lineedit_address.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineedit_address.setInputMask("")
        self.lineedit_address.setMaxLength(8)
        self.lineedit_address.setObjectName("lineedit_address")
        self.label = QtWidgets.QLabel(self.group_box_cambridge_memory)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1172, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.group_box_spi_register.setTitle(_translate("MainWindow", "SPI Register"))
        self.button_read_spi_reg.setText(_translate("MainWindow", "Read"))
        self.group_box_cambridge_memory.setTitle(_translate("MainWindow", "Cambridge memory"))
        item = self.tablewidget_cambridge_mem.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "0x00"))
        item = self.tablewidget_cambridge_mem.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "0x04"))
        item = self.tablewidget_cambridge_mem.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "0x08"))
        item = self.tablewidget_cambridge_mem.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "0x0C"))
        item = self.tablewidget_cambridge_mem.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "0x10"))
        item = self.tablewidget_cambridge_mem.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "0x14"))
        item = self.tablewidget_cambridge_mem.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "0x18"))
        item = self.tablewidget_cambridge_mem.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "0x1C"))
        self.button_read_cambridge_mem.setText(_translate("MainWindow", "Read"))
        self.label.setText(_translate("MainWindow", "Address 0x"))

