# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore
import PyQt4
from PyQt4.QtGui import QMessageBox
from collections import OrderedDict


from com.tourism.gui.ui_widget_register_travel_pack import Ui_widget_register_travel_pack 
from com.tourism.authentication.user_authentication import UserAuth
from com.tourism.webservice.webservice_handler import WebserviceHandler
from com.tourism.gui.widget_table import MyTable

class WidgetRegisterTravelPack(QWidget, Ui_widget_register_travel_pack):
    """This widget is intended for travel packages registration.
    
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
        
        self.line_edit_origem.setDisabled(True)
        self.line_edit_destination.setDisabled(True)
        self.combo_number_of_rooms.setDisabled(True)
        self.combo_age.setDisabled(True)
        self.date_edit_departure.setDisabled(True)
        self.date_edit_arrival.setDisabled(True)
        self.buton_add_guest.setDisabled(True)
        self.button_register.setDisabled(True)

        # event handling
        self.button_login.clicked.connect(self.perform_authentication)
        self.button_register.clicked.connect(self.register_travel_pack)
        self.buton_add_guest.clicked.connect(self.add_guest)

    def perform_authentication(self):
        """Check the server if user exists."""

        auth = UserAuth(self.line_edit_user_name.text(), self.line_edit_password.text())
        user_exists = auth.authenticate()

        if not user_exists:
            
            QMessageBox.about(self, "Error", "user don't exist.")
        else:

            QMessageBox.about(self, "Success", "login successfull.")
    
            self.line_edit_origem.setDisabled(False)
            self.line_edit_destination.setDisabled(False)
            self.combo_number_of_rooms.setDisabled(False)
            self.combo_age.setDisabled(False)
            self.date_edit_departure.setDisabled(False)
            self.date_edit_arrival.setDisabled(False)
            self.buton_add_guest.setDisabled(False)
            self.button_register.setDisabled(False)

    def add_guest(self):
        """Add a new guest (age) to the table."""

        new_row_index = self.table_guests.rowCount()
        self.table_guests.insertRow(new_row_index)
        self.table_guests.setItem(new_row_index , 0, QtGui.QTableWidgetItem(self.combo_age.currentText()))
        
    def register_travel_pack(self):
        """Perform the travel pack registration on the server."""

        origin = self.line_edit_origem.text()
        destination = self.line_edit_destination.text()
        departure_date = self.date_edit_departure.date().getDate()
        arrival_date = self.date_edit_arrival.date().getDate()
        number_of_rooms = int(self.combo_number_of_rooms.currentText())
        is_promo = self.check_is_promo.isChecked()
        guest_ages = self.table_guests.get_column(0)

        guest_ages = [int(i) for i in guest_ages]
        
        handler = WebserviceHandler()
        handler.register_travel_pack(origin, 
                                     destination, 
                                     departure_date, 
                                     arrival_date, 
                                     number_of_rooms, 
                                     is_promo,
                                     guest_ages)

        QMessageBox.about(self, "Success", "travel pack registered.")

        self.line_edit_origem.clear()
        self.line_edit_destination.clear()

        self.clear_layout(self.vlayout_guests)
        data = OrderedDict([('Guest age', [])])
        self.table_guests = MyTable(data, 0, 1)
        self.vlayout_guests.addWidget(self.table_guests)

        self.date_edit_arrival.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 1, 1), QtCore.QTime(0, 0, 0)))

        self.date_edit_departure.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 1, 1), QtCore.QTime(0, 0, 0)))

        self.combo_number_of_rooms.setCurrentIndex(0)
        self.combo_age.setCurrentIndex(0)

        self.check_is_promo.setChecked(False)

    def clear_layout(self, layout):
        """Remove all the widgets from the layout."""
        
        while layout.count():
            child = layout.takeAt(0)
            child.widget().deleteLater()