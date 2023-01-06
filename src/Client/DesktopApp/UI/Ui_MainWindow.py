# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowfiglqk.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(596, 753)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 211, 711))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radioButton_UsersOnline = QRadioButton(self.layoutWidget)
        self.radioButton_UsersOnline.setObjectName(u"radioButton_UsersOnline")

        self.horizontalLayout.addWidget(self.radioButton_UsersOnline)

        self.radioButton_AllUsers = QRadioButton(self.layoutWidget)
        self.radioButton_AllUsers.setObjectName(u"radioButton_AllUsers")

        self.horizontalLayout.addWidget(self.radioButton_AllUsers)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listView_Users = QListView(self.layoutWidget)
        self.listView_Users.setObjectName(u"listView_Users")

        self.verticalLayout.addWidget(self.listView_Users)

        self.pushButton_SignOut = QPushButton(self.layoutWidget)
        self.pushButton_SignOut.setObjectName(u"pushButton_SignOut")

        self.verticalLayout.addWidget(self.pushButton_SignOut)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(210, 0, 381, 641))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.listView_MessageHistory = QListView(self.layoutWidget1)
        self.listView_MessageHistory.setObjectName(u"listView_MessageHistory")
        self.listView_MessageHistory.setAutoScroll(False)

        self.horizontalLayout_4.addWidget(self.listView_MessageHistory)

        self.pushButton_SendMessage = QPushButton(self.centralwidget)
        self.pushButton_SendMessage.setObjectName(u"pushButton_SendMessage")
        self.pushButton_SendMessage.setGeometry(QRect(522, 640, 70, 70))
        self.lineEdit_SendMessageField = QLineEdit(self.centralwidget)
        self.lineEdit_SendMessageField.setObjectName(u"lineEdit_SendMessageField")
        self.lineEdit_SendMessageField.setGeometry(QRect(210, 640, 310, 70))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 596, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Time to chat", None))
        self.radioButton_UsersOnline.setText(QCoreApplication.translate("MainWindow", u"Users online", None))
        self.radioButton_AllUsers.setText(QCoreApplication.translate("MainWindow", u"All users", None))
        self.pushButton_SignOut.setText(QCoreApplication.translate("MainWindow", u"Sign out", None))
        self.pushButton_SendMessage.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi

