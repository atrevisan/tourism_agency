# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_packages.ui'
#
# Created: Thu Jan 29 08:53:57 2015
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

class Ui_widget_packages(object):
    def setupUi(self, widget_packages):
        widget_packages.setObjectName(_fromUtf8("widget_packages"))
        widget_packages.resize(589, 539)
        self.verticalLayoutWidget = QtGui.QWidget(widget_packages)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 441, 121))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.vlayout_table_content = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vlayout_table_content.setMargin(0)
        self.vlayout_table_content.setObjectName(_fromUtf8("vlayout_table_content"))
        self.button_choose_package = QtGui.QPushButton(widget_packages)
        self.button_choose_package.setGeometry(QtCore.QRect(461, 71, 111, 28))
        self.button_choose_package.setObjectName(_fromUtf8("button_choose_package"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(widget_packages)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 310, 441, 101))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.vlayout_chosen_package = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vlayout_chosen_package.setMargin(0)
        self.vlayout_chosen_package.setObjectName(_fromUtf8("vlayout_chosen_package"))
        self.button_buy = QtGui.QPushButton(widget_packages)
        self.button_buy.setGeometry(QtCore.QRect(220, 500, 93, 28))
        self.button_buy.setObjectName(_fromUtf8("button_buy"))
        self.layoutWidget = QtGui.QWidget(widget_packages)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 440, 212, 24))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.line_edit_credit_card = QtGui.QLineEdit(self.layoutWidget)
        self.line_edit_credit_card.setEchoMode(QtGui.QLineEdit.Password)
        self.line_edit_credit_card.setObjectName(_fromUtf8("line_edit_credit_card"))
        self.horizontalLayout.addWidget(self.line_edit_credit_card)
        self.layoutWidget1 = QtGui.QWidget(widget_packages)
        self.layoutWidget1.setGeometry(QtCore.QRect(280, 440, 190, 24))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.combo_number_of_installments = QtGui.QComboBox(self.layoutWidget1)
        self.combo_number_of_installments.setObjectName(_fromUtf8("combo_number_of_installments"))
        self.combo_number_of_installments.addItem(_fromUtf8(""))
        self.combo_number_of_installments.addItem(_fromUtf8(""))
        self.combo_number_of_installments.addItem(_fromUtf8(""))
        self.combo_number_of_installments.addItem(_fromUtf8(""))
        self.combo_number_of_installments.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.combo_number_of_installments)
        self.button_remove_package = QtGui.QPushButton(widget_packages)
        self.button_remove_package.setGeometry(QtCore.QRect(461, 350, 111, 28))
        self.button_remove_package.setObjectName(_fromUtf8("button_remove_package"))
        self.verticalLayoutWidget_3 = QtGui.QWidget(widget_packages)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 160, 160, 121))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.vlayout_guest_ages = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.vlayout_guest_ages.setMargin(0)
        self.vlayout_guest_ages.setObjectName(_fromUtf8("vlayout_guest_ages"))

        self.retranslateUi(widget_packages)
        QtCore.QMetaObject.connectSlotsByName(widget_packages)

    def retranslateUi(self, widget_packages):
        widget_packages.setWindowTitle(_translate("widget_packages", "Packages", None))
        self.button_choose_package.setText(_translate("widget_packages", "choose package", None))
        self.button_buy.setText(_translate("widget_packages", "buy", None))
        self.label.setText(_translate("widget_packages", "credit card:", None))
        self.label_2.setText(_translate("widget_packages", "Number of installments:", None))
        self.combo_number_of_installments.setItemText(0, _translate("widget_packages", "1", None))
        self.combo_number_of_installments.setItemText(1, _translate("widget_packages", "2", None))
        self.combo_number_of_installments.setItemText(2, _translate("widget_packages", "4", None))
        self.combo_number_of_installments.setItemText(3, _translate("widget_packages", "10", None))
        self.combo_number_of_installments.setItemText(4, _translate("widget_packages", "12", None))
        self.button_remove_package.setText(_translate("widget_packages", "remove package", None))

