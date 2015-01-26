# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_register_travel_pack.ui'
#
# Created: Mon Jan 26 08:38:04 2015
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

class Ui_widget_register_travel_pack(object):
    def setupUi(self, widget_register_travel_pack):
        widget_register_travel_pack.setObjectName(_fromUtf8("widget_register_travel_pack"))
        widget_register_travel_pack.resize(589, 539)
        self.label = QtGui.QLabel(widget_register_travel_pack)
        self.label.setGeometry(QtCore.QRect(11, 21, 67, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.line_edit_user_name = QtGui.QLineEdit(widget_register_travel_pack)
        self.line_edit_user_name.setGeometry(QtCore.QRect(90, 22, 137, 22))
        self.line_edit_user_name.setObjectName(_fromUtf8("line_edit_user_name"))
        self.label_2 = QtGui.QLabel(widget_register_travel_pack)
        self.label_2.setGeometry(QtCore.QRect(11, 61, 60, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line_edit_password = QtGui.QLineEdit(widget_register_travel_pack)
        self.line_edit_password.setGeometry(QtCore.QRect(90, 60, 137, 22))
        self.line_edit_password.setEchoMode(QtGui.QLineEdit.Password)
        self.line_edit_password.setObjectName(_fromUtf8("line_edit_password"))
        self.line = QtGui.QFrame(widget_register_travel_pack)
        self.line.setGeometry(QtCore.QRect(20, 110, 531, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_7 = QtGui.QLabel(widget_register_travel_pack)
        self.label_7.setGeometry(QtCore.QRect(49, 270, 111, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.line_edit_number_of_rooms = QtGui.QLineEdit(widget_register_travel_pack)
        self.line_edit_number_of_rooms.setGeometry(QtCore.QRect(179, 270, 61, 22))
        self.line_edit_number_of_rooms.setObjectName(_fromUtf8("line_edit_number_of_rooms"))
        self.layoutWidget = QtGui.QWidget(widget_register_travel_pack)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 161, 191, 24))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.line_edit_origem = QtGui.QLineEdit(self.layoutWidget)
        self.line_edit_origem.setObjectName(_fromUtf8("line_edit_origem"))
        self.horizontalLayout.addWidget(self.line_edit_origem)
        self.layoutWidget1 = QtGui.QWidget(widget_register_travel_pack)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 200, 193, 24))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.line_edit_destination = QtGui.QLineEdit(self.layoutWidget1)
        self.line_edit_destination.setObjectName(_fromUtf8("line_edit_destination"))
        self.horizontalLayout_2.addWidget(self.line_edit_destination)
        self.layoutWidget2 = QtGui.QWidget(widget_register_travel_pack)
        self.layoutWidget2.setGeometry(QtCore.QRect(289, 170, 192, 24))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.layoutWidget2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.date_edit_departure = QtGui.QDateEdit(self.layoutWidget2)
        self.date_edit_departure.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_edit_departure.setObjectName(_fromUtf8("date_edit_departure"))
        self.horizontalLayout_3.addWidget(self.date_edit_departure)
        self.layoutWidget3 = QtGui.QWidget(widget_register_travel_pack)
        self.layoutWidget3.setGeometry(QtCore.QRect(289, 200, 191, 24))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_6 = QtGui.QLabel(self.layoutWidget3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.date_edit_arrival = QtGui.QDateEdit(self.layoutWidget3)
        self.date_edit_arrival.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_edit_arrival.setObjectName(_fromUtf8("date_edit_arrival"))
        self.horizontalLayout_4.addWidget(self.date_edit_arrival)
        self.button_login = QtGui.QPushButton(widget_register_travel_pack)
        self.button_login.setGeometry(QtCore.QRect(310, 40, 93, 28))
        self.button_login.setObjectName(_fromUtf8("button_login"))
        self.button_register = QtGui.QPushButton(widget_register_travel_pack)
        self.button_register.setGeometry(QtCore.QRect(180, 340, 93, 28))
        self.button_register.setObjectName(_fromUtf8("button_register"))

        self.retranslateUi(widget_register_travel_pack)
        QtCore.QMetaObject.connectSlotsByName(widget_register_travel_pack)

    def retranslateUi(self, widget_register_travel_pack):
        widget_register_travel_pack.setWindowTitle(_translate("widget_register_travel_pack", "Register travel pack", None))
        self.label.setText(_translate("widget_register_travel_pack", "User name:", None))
        self.label_2.setText(_translate("widget_register_travel_pack", "Password:", None))
        self.label_7.setText(_translate("widget_register_travel_pack", "Number of rooms:", None))
        self.label_3.setText(_translate("widget_register_travel_pack", "Origin:", None))
        self.label_4.setText(_translate("widget_register_travel_pack", "Destination:", None))
        self.label_5.setText(_translate("widget_register_travel_pack", "Departure date:", None))
        self.label_6.setText(_translate("widget_register_travel_pack", "Arrival date:", None))
        self.button_login.setText(_translate("widget_register_travel_pack", "Log in", None))
        self.button_register.setText(_translate("widget_register_travel_pack", "Register", None))

