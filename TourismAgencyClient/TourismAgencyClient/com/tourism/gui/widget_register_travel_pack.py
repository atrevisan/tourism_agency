# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore
import PyQt4
from PyQt4.QtGui import QMessageBox
from suds.client import Client

from com.tourism.gui.ui_widget_register_travel_pack import Ui_widget_register_travel_pack 
from com.tourism.authentication.user_authentication import UserAuth
from com.tourism.webservice.webservice_handler import WebserviceHandler

class WidgetRegisterTravelPack(QWidget, Ui_widget_register_travel_pack):
    """This widget is intended for travel packages registration.
    
    For the user to perform this operation is necessary to log in
    first.
    """
    def __init__(self):

        QWidget.__init__(self)
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        self.line_edit_origem.setDisabled(True)
        self.line_edit_destination.setDisabled(True)
        self.line_edit_number_of_rooms.setDisabled(True)
        self.date_edit_departure.setDisabled(True)
        self.date_edit_arrival.setDisabled(True)

        # event handling
        self.button_login.clicked.connect(self.perform_authentication)
        self.button_register.clicked.connect(self.register_travel_pack)

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
            self.line_edit_number_of_rooms.setDisabled(False)
            self.date_edit_departure.setDisabled(False)
            self.date_edit_arrival.setDisabled(False)

    def register_travel_pack(self):
        """Perform the travel pack registration on the server."""

        origin = self.line_edit_origem.text()
        destination = self.line_edit_destination.text()

        departure_date = self.date_edit_departure.date().getDate()
        arrival_date = self.date_edit_arrival.date().getDate()

        number_of_rooms = self.line_edit_number_of_rooms.text()
        
        is_promo = self.check_is_promo.isChecked()
        
        handler = WebserviceHandler()
        handler.register_travel_pack(origin, destination, departure_date, arrival_date, number_of_rooms, is_promo)

        QMessageBox.about(self, "Success", "travel pack registered.")

        self.line_edit_origem.clear()
        self.line_edit_destination.clear()
        self.line_edit_number_of_rooms.clear()