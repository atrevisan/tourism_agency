# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore
import PyQt4
from PyQt4.QtGui import QMessageBox
from collections import OrderedDict

from com.tourism.gui.ui_widget_register_hosting import Ui_widget_register_hosting
from com.tourism.authentication.user_authentication import UserAuth
from com.tourism.webservice.webservice_handler import WebserviceHandler
from com.tourism.gui.widget_table import MyTable

class WidgetRegisterHosting(QWidget, Ui_widget_register_hosting):
    """This widget is intended for hosting registration.
    
    For the user to perform this operation is necessary to log in
    first.
    """
    def __init__(self):

        QWidget.__init__(self)
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        self.combo_number_of_rooms.addItems([str(i) for i in range(20)][1:])
        self.combo_age.addItems([str(i) for i in range(70)][1:])
        data = OrderedDict([('Guest age', [])])
        self.table_guests = MyTable(data, 0, 1)
        self.vlayout_guests.addWidget(self.table_guests)
        
        self.line_edit_destination.setDisabled(True)
        self.combo_number_of_rooms.setDisabled(True)
        self.combo_age.setDisabled(True)

        self.date_edit_input.setDisabled(True)
        self.date_edit_output.setDisabled(True)
        
        self.buton_add_guest.setDisabled(True)
        self.button_register.setDisabled(True)
        
        # event handling
        self.button_login.clicked.connect(self.perform_authentication)
        self.button_register.clicked.connect(self.register_hosting)
        self.buton_add_guest.clicked.connect(self.add_guest)

    def perform_authentication(self):
        """Check the server if user exists."""

        auth = UserAuth(self.line_edit_user_name.text(), self.line_edit_password.text())
        user_exists = auth.authenticate()

        if not user_exists:
            
            QMessageBox.about(self, "Error", "user don't exist.")
        else:

            QMessageBox.about(self, "Success", "login successfull.")
            
            self.line_edit_destination.setDisabled(False)
            self.combo_number_of_rooms.setDisabled(False)
            self.combo_age.setDisabled(False)
            self.date_edit_input.setDisabled(False)
            self.date_edit_output.setDisabled(False)
            self.buton_add_guest.setDisabled(False)
            self.button_register.setDisabled(False)

    def add_guest(self):
        """Add a new guest (age) to the table."""

        new_row_index = self.table_guests.rowCount()
        self.table_guests.insertRow(new_row_index)
        self.table_guests.setItem(new_row_index , 0, QtGui.QTableWidgetItem(self.combo_age.currentText()))
        
    def register_hosting(self):
        """Perform the hosting registration on the server."""

        destination = self.line_edit_destination.text()
        input_date = self.date_edit_input.date().getDate()
        output_date = self.date_edit_output.date().getDate()
        number_of_rooms = int(self.combo_number_of_rooms.currentText())
        guest_ages = self.table_guests.get_column(0)

        guest_ages = [int(i) for i in guest_ages]
        
        handler = WebserviceHandler()
        handler.register_hosting(destination, 
                                 input_date, 
                                 output_date, 
                                 number_of_rooms, 
                                 guest_ages)

        QMessageBox.about(self, "Success", "hosting registered.")

        self.line_edit_destination.clear()

        self.clear_layout(self.vlayout_guests)
        data = OrderedDict([('Guest age', [])])
        self.table_guests = MyTable(data, 0, 1)
        self.vlayout_guests.addWidget(self.table_guests)

        self.date_edit_input.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 1, 1), QtCore.QTime(0, 0, 0)))

        self.date_edit_output.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 1, 1), QtCore.QTime(0, 0, 0)))

        self.combo_number_of_rooms.setCurrentIndex(0)
        self.combo_age.setCurrentIndex(0)

    def clear_layout(self, layout):
        """Remove all the widgets from the layout."""
        
        while layout.count():
            child = layout.takeAt(0)
            child.widget().deleteLater()