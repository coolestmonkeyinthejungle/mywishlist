# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameEdit)
        self.price_label = QtWidgets.QLabel(self.centralwidget)
        self.price_label.setObjectName("price_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.price_label)
        self.priceEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.priceEdit.setObjectName("priceEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.priceEdit)
        self.link_label = QtWidgets.QLabel(self.centralwidget)
        self.link_label.setObjectName("link_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.link_label)
        self.linkEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.linkEdit.setObjectName("linkEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.linkEdit)
        self.comment_label = QtWidgets.QLabel(self.centralwidget)
        self.comment_label.setObjectName("comment_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.comment_label)
        self.commentEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.commentEdit.setObjectName("commentEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.commentEdit)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.saveButton)
        self.horizontalLayout_6.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setTabletTracking(False)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_3.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.name_label.setText(_translate("MainWindow", "Название:"))
        self.price_label.setText(_translate("MainWindow", "Цена:"))
        self.link_label.setText(_translate("MainWindow", "Ссылка:"))
        self.comment_label.setText(_translate("MainWindow", "Примечание:"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить"))
