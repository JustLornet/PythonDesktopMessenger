# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AuthorizationWindowYmIixy.ui'
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


class Ui_AuthorizationWindow(object):
    def setupUi(self, AuthorizationWindow):
        if AuthorizationWindow.objectName():
            AuthorizationWindow.setObjectName(u"AuthorizationWindow")
        AuthorizationWindow.resize(289, 179)
        self.label = QLabel(AuthorizationWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 40, 31, 16))
        self.label_2 = QLabel(AuthorizationWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 47, 13))
        self.pushButton_SignIn = QPushButton(AuthorizationWindow)
        self.pushButton_SignIn.setObjectName(u"pushButton_SignIn")
        self.pushButton_SignIn.setGeometry(QRect(30, 130, 75, 23))
        self.pushButton_Register = QPushButton(AuthorizationWindow)
        self.pushButton_Register.setObjectName(u"pushButton_Register")
        self.pushButton_Register.setGeometry(QRect(160, 130, 75, 23))
        self.lineEdit_Login = QLineEdit(AuthorizationWindow)
        self.lineEdit_Login.setObjectName(u"lineEdit_Login")
        self.lineEdit_Login.setGeometry(QRect(90, 40, 113, 20))
        self.lineEdit_Register = QLineEdit(AuthorizationWindow)
        self.lineEdit_Register.setObjectName(u"lineEdit_Register")
        self.lineEdit_Register.setGeometry(QRect(90, 80, 113, 20))

        self.retranslateUi(AuthorizationWindow)

        QMetaObject.connectSlotsByName(AuthorizationWindow)
    # setupUi

    def retranslateUi(self, AuthorizationWindow):
        AuthorizationWindow.setWindowTitle(QCoreApplication.translate("AuthorizationWindow", u"Welcome!", None))
        self.label.setText(QCoreApplication.translate("AuthorizationWindow", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("AuthorizationWindow", u"Password", None))
        self.pushButton_SignIn.setText(QCoreApplication.translate("AuthorizationWindow", u"Sign in", None))
        self.pushButton_Register.setText(QCoreApplication.translate("AuthorizationWindow", u"Register", None))
    # retranslateUi

