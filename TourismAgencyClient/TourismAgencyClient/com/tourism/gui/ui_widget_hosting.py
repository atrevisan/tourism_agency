# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_hosting.ui'
#
# Created: Tue Feb  3 15:24:11 2015
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

class Ui_widget_hosting(object):
    def setupUi(self, widget_hosting):
        widget_hosting.setObjectName(_fromUtf8("widget_hosting"))
        widget_hosting.resize(589, 539)
        self.layoutWidget_2 = QtGui.QWidget(widget_hosting)
        self.layoutWidget_2.setGeometry(QtCore.QRect(19, 439, 212, 24))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.line_edit_credit_card = QtGui.QLineEdit(self.layoutWidget_2)
        self.line_edit_credit_card.setEchoMode(QtGui.QLineEdit.Password)
        self.line_edit_credit_card.setObjectName(_fromUtf8("line_edit_credit_card"))
        self.horizontalLayout.addWidget(self.line_edit_credit_card)
        self.verticalLayoutWidget_3 = QtGui.QWidget(widget_hosting)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(19, 159, 160, 121))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.vlayout_guest_ages = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.vlayout_guest_ages.setMargin(0)
        self.vlayout_guest_ages.setObjectName(_fromUtf8("vlayout_guest_ages"))
        self.button_buy = QtGui.QPushButton(widget_hosting)
        self.button_buy.setGeometry(QtCore.QRect(219, 499, 93, 28))
        self.button_buy.setObjectName(_fromUtf8("button_buy"))
        self.button_remove_hosting = QtGui.QPushButton(widget_hosting)
        self.button_remove_hosting.setGeometry(QtCore.QRect(460, 349, 121, 28))
        self.button_remove_hosting.setObjectName(_fromUtf8("button_remove_hosting"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(widget_hosting)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 309, 441, 101))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.vlayout_chosen_hosting = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vlayout_chosen_hosting.setMargin(0)
        self.vlayout_chosen_hosting.setObjectName(_fromUtf8("vlayout_chosen_hosting"))
        self.layoutWidget = QtGui.QWidget(widget_hosting)
        self.layoutWidget.setGeometry(QtCore.QRect(279, 439, 190, 24))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.combo_number_of_installments = QtGui.QComboBox(self.layoutWidget)
        self.combo_number_of_installments.setObjectName(_fromUtf8("combo_number_of_installments"))
        self.combo_number_of_installments.addItem(_fromUtf8(""))
        self.combo_number_of_installments.addItem(_fromUtf8(""))
        self.combo_number_of_installments.addItem(_fromUtf8(""))
        self.combo_number_of_installments.addItem(_fromUtf8(""))
        self.combo_number_of_installments.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.combo_number_of_installments)
        self.verticalLayoutWidget = QtGui.QWidget(widget_hosting)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 19, 441, 121))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.vlayout_table_content = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.vlayout_table_content.setMargin(0)
        self.vlayout_table_content.setObjectName(_fromUtf8("vlayout_table_content"))
        self.button_choose_hosting = QtGui.QPushButton(widget_hosting)
        self.button_choose_hosting.setGeometry(QtCore.QRect(460, 70, 121, 28))
        self.button_choose_hosting.setObjectName(_fromUtf8("button_choose_hosting"))

        self.retranslateUi(widget_hosting)
        QtCore.QMetaObject.connectSlotsByName(widget_hosting)

    def retranslateUi(self, widget_hosting):
        widget_hosting.setWindowTitle(_translate("widget_hosting", "Form", None))
        self.label.setText(_translate("widget_hosting", "credit card:", None))
        self.button_buy.setText(_translate("widget_hosting", "buy", None))
        self.button_remove_hosting.setText(_translate("widget_hosting", "remove hosting", None))
        self.label_2.setText(_translate("widget_hosting", "Number of installments:", None))
        self.combo_number_of_installments.setItemText(0, _translate("widget_hosting", "1", None))
        self.combo_number_of_installments.setItemText(1, _translate("widget_hosting", "2", None))
        self.combo_number_of_installments.setItemText(2, _translate("widget_hosting", "4", None))
        self.combo_number_of_installments.setItemText(3, _translate("widget_hosting", "10", None))
        self.combo_number_of_installments.setItemText(4, _translate("widget_hosting", "12", None))
        self.button_choose_hosting.setText(_translate("widget_hosting", "choose hosting", None))

