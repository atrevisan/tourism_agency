# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_register_hosting.ui'
#
# Created: Tue Feb  3 15:30:52 2015
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

class Ui_widget_register_hosting(object):
    def setupUi(self, widget_register_hosting):
        widget_register_hosting.setObjectName(_fromUtf8("widget_register_hosting"))
        widget_register_hosting.resize(589, 539)
        self.verticalLayoutWidget = QtGui.QWidget(widget_register_hosting)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 279, 171, 81))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.vlayout_guests = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vlayout_guests.setMargin(0)
        self.vlayout_guests.setObjectName(_fromUtf8("vlayout_guests"))
        self.button_login = QtGui.QPushButton(widget_register_hosting)
        self.button_login.setGeometry(QtCore.QRect(310, 40, 93, 28))
        self.button_login.setObjectName(_fromUtf8("button_login"))
        self.line = QtGui.QFrame(widget_register_hosting)
        self.line.setGeometry(QtCore.QRect(20, 110, 531, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.layoutWidget_6 = QtGui.QWidget(widget_register_hosting)
        self.layoutWidget_6.setGeometry(QtCore.QRect(9, 260, 187, 24))
        self.layoutWidget_6.setObjectName(_fromUtf8("layoutWidget_6"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_7 = QtGui.QLabel(self.layoutWidget_6)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_6.addWidget(self.label_7)
        self.combo_number_of_rooms = QtGui.QComboBox(self.layoutWidget_6)
        self.combo_number_of_rooms.setObjectName(_fromUtf8("combo_number_of_rooms"))
        self.horizontalLayout_6.addWidget(self.combo_number_of_rooms)
        self.label_2 = QtGui.QLabel(widget_register_hosting)
        self.label_2.setGeometry(QtCore.QRect(11, 61, 60, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.layoutWidget_5 = QtGui.QWidget(widget_register_hosting)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 300, 192, 24))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.layoutWidget_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.date_edit_input = QtGui.QDateEdit(self.layoutWidget_5)
        self.date_edit_input.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_edit_input.setObjectName(_fromUtf8("date_edit_input"))
        self.horizontalLayout_3.addWidget(self.date_edit_input)
        self.label = QtGui.QLabel(widget_register_hosting)
        self.label.setGeometry(QtCore.QRect(11, 21, 67, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.line_edit_password = QtGui.QLineEdit(widget_register_hosting)
        self.line_edit_password.setGeometry(QtCore.QRect(90, 60, 137, 22))
        self.line_edit_password.setEchoMode(QtGui.QLineEdit.Password)
        self.line_edit_password.setObjectName(_fromUtf8("line_edit_password"))
        self.button_register = QtGui.QPushButton(widget_register_hosting)
        self.button_register.setGeometry(QtCore.QRect(20, 460, 93, 28))
        self.button_register.setObjectName(_fromUtf8("button_register"))
        self.line_edit_user_name = QtGui.QLineEdit(widget_register_hosting)
        self.line_edit_user_name.setGeometry(QtCore.QRect(90, 22, 137, 22))
        self.line_edit_user_name.setObjectName(_fromUtf8("line_edit_user_name"))
        self.layoutWidget_3 = QtGui.QWidget(widget_register_hosting)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 330, 191, 24))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_6 = QtGui.QLabel(self.layoutWidget_3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.date_edit_output = QtGui.QDateEdit(self.layoutWidget_3)
        self.date_edit_output.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 1, 1), QtCore.QTime(0, 0, 0)))
        self.date_edit_output.setObjectName(_fromUtf8("date_edit_output"))
        self.horizontalLayout_4.addWidget(self.date_edit_output)
        self.layoutWidget = QtGui.QWidget(widget_register_hosting)
        self.layoutWidget.setGeometry(QtCore.QRect(280, 200, 144, 24))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_5.addWidget(self.label_8)
        self.combo_age = QtGui.QComboBox(self.layoutWidget)
        self.combo_age.setObjectName(_fromUtf8("combo_age"))
        self.horizontalLayout_5.addWidget(self.combo_age)
        self.layoutWidget_4 = QtGui.QWidget(widget_register_hosting)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 200, 241, 46))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.layoutWidget_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.line_edit_destination = QtGui.QLineEdit(self.layoutWidget_4)
        self.line_edit_destination.setObjectName(_fromUtf8("line_edit_destination"))
        self.horizontalLayout_2.addWidget(self.line_edit_destination)
        self.buton_add_guest = QtGui.QPushButton(widget_register_hosting)
        self.buton_add_guest.setGeometry(QtCore.QRect(450, 200, 93, 28))
        self.buton_add_guest.setObjectName(_fromUtf8("buton_add_guest"))

        self.retranslateUi(widget_register_hosting)
        QtCore.QMetaObject.connectSlotsByName(widget_register_hosting)

    def retranslateUi(self, widget_register_hosting):
        widget_register_hosting.setWindowTitle(_translate("widget_register_hosting", "Register hosting", None))
        self.button_login.setText(_translate("widget_register_hosting", "Log in", None))
        self.label_7.setText(_translate("widget_register_hosting", "Number of rooms:", None))
        self.label_2.setText(_translate("widget_register_hosting", "Password:", None))
        self.label_5.setText(_translate("widget_register_hosting", "input date:", None))
        self.label.setText(_translate("widget_register_hosting", "User name:", None))
        self.button_register.setText(_translate("widget_register_hosting", "Register", None))
        self.label_6.setText(_translate("widget_register_hosting", "output date:", None))
        self.label_8.setText(_translate("widget_register_hosting", "Guest age:", None))
        self.label_4.setText(_translate("widget_register_hosting", "<html><head/><body><p>Destination: </p><p>(city or hotel)</p></body></html>", None))
        self.buton_add_guest.setText(_translate("widget_register_hosting", "add guest", None))

