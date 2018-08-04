# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcome.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dlgWelcome(object):
    def setupUi(self, dlgWelcome):
        dlgWelcome.setObjectName("dlgWelcome")
        dlgWelcome.resize(400, 360)
        dlgWelcome.setMinimumSize(QtCore.QSize(400, 360))
        dlgWelcome.setMaximumSize(QtCore.QSize(400, 360))
        self.boxButtons = QtWidgets.QDialogButtonBox(dlgWelcome)
        self.boxButtons.setGeometry(QtCore.QRect(50, 320, 341, 32))
        self.boxButtons.setOrientation(QtCore.Qt.Horizontal)
        self.boxButtons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.boxButtons.setObjectName("boxButtons")
        self.lblWelcome = QtWidgets.QLabel(dlgWelcome)
        self.lblWelcome.setGeometry(QtCore.QRect(20, 10, 351, 201))
        self.lblWelcome.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblWelcome.setWordWrap(True)
        self.lblWelcome.setObjectName("lblWelcome")
        self.cboHost = QtWidgets.QComboBox(dlgWelcome)
        self.cboHost.setGeometry(QtCore.QRect(20, 220, 251, 22))
        self.cboHost.setAutoFillBackground(False)
        self.cboHost.setObjectName("cboHost")
        self.txtOtherHost = QtWidgets.QLineEdit(dlgWelcome)
        self.txtOtherHost.setEnabled(False)
        self.txtOtherHost.setGeometry(QtCore.QRect(20, 250, 251, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtOtherHost.sizePolicy().hasHeightForWidth())
        self.txtOtherHost.setSizePolicy(sizePolicy)
        self.txtOtherHost.setMinimumSize(QtCore.QSize(251, 22))
        self.txtOtherHost.setMaximumSize(QtCore.QSize(251, 22))
        self.txtOtherHost.setDragEnabled(True)
        self.txtOtherHost.setPlaceholderText("")
        self.txtOtherHost.setObjectName("txtOtherHost")

        self.retranslateUi(dlgWelcome)
        self.boxButtons.accepted.connect(dlgWelcome.accept)
        self.boxButtons.rejected.connect(dlgWelcome.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgWelcome)

    def retranslateUi(self, dlgWelcome):
        _translate = QtCore.QCoreApplication.translate
        dlgWelcome.setWindowTitle(_translate("dlgWelcome", "Welcome!"))
        self.lblWelcome.setText(_translate("dlgWelcome", "<html><head/><body><p>Welcome to the Contact Siphon! This little utility will pull the email addreses from every email in your mailbox: to, from, cc, bcc. It will then clean up those addresses as much as possible, and produce a comma-separated values file that you can import into your favorite contact list.</p><p>This version of Contact Siphon only pulls addresses from IMAP accounts. POP3 accounts keep messages on your computer or device, and there are many different ways to store them. IMAP accounts keep the messages on the server, where there are more strict rules.</p><p>First up, choose your email service provider.</p></body></html>"))

