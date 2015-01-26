# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sun Jan 25 22:17:12 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName(_fromUtf8("main_window"))
        main_window.resize(800, 600)
        self.centralwidget = QtGui.QWidget(main_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 30, 591, 541))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.vlayout_content = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vlayout_content.setMargin(0)
        self.vlayout_content.setObjectName(_fromUtf8("vlayout_content"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 127, 240))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.vlayout_buttons = QtGui.QVBoxLayout(self.widget)
        self.vlayout_buttons.setMargin(0)
        self.vlayout_buttons.setObjectName(_fromUtf8("vlayout_buttons"))
        self.button_register_travel_pack = QtGui.QPushButton(self.widget)
        self.button_register_travel_pack.setObjectName(_fromUtf8("button_register_travel_pack"))
        self.vlayout_buttons.addWidget(self.button_register_travel_pack)
        self.button_register_plane_ticket = QtGui.QPushButton(self.widget)
        self.button_register_plane_ticket.setObjectName(_fromUtf8("button_register_plane_ticket"))
        self.vlayout_buttons.addWidget(self.button_register_plane_ticket)
        self.button_register_hosting = QtGui.QPushButton(self.widget)
        self.button_register_hosting.setObjectName(_fromUtf8("button_register_hosting"))
        self.vlayout_buttons.addWidget(self.button_register_hosting)
        self.button_show_promo_packs = QtGui.QPushButton(self.widget)
        self.button_show_promo_packs.setObjectName(_fromUtf8("button_show_promo_packs"))
        self.vlayout_buttons.addWidget(self.button_show_promo_packs)
        self.button_packages = QtGui.QPushButton(self.widget)
        self.button_packages.setObjectName(_fromUtf8("button_packages"))
        self.vlayout_buttons.addWidget(self.button_packages)
        self.button_plane_tickets = QtGui.QPushButton(self.widget)
        self.button_plane_tickets.setObjectName(_fromUtf8("button_plane_tickets"))
        self.vlayout_buttons.addWidget(self.button_plane_tickets)
        self.button_hosting = QtGui.QPushButton(self.widget)
        self.button_hosting.setObjectName(_fromUtf8("button_hosting"))
        self.vlayout_buttons.addWidget(self.button_hosting)
        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("main_window", "Tourism Agency", None))
        self.button_register_travel_pack.setText(_translate("main_window", "Register travel pack", None))
        self.button_register_plane_ticket.setText(_translate("main_window", "Register plane ticket", None))
        self.button_register_hosting.setText(_translate("main_window", "Register hosting", None))
        self.button_show_promo_packs.setText(_translate("main_window", "Promo packages", None))
        self.button_packages.setText(_translate("main_window", "Packages", None))
        self.button_plane_tickets.setText(_translate("main_window", "Plane tickets", None))
        self.button_hosting.setText(_translate("main_window", "Hosting", None))

