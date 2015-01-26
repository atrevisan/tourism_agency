# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore
import PyQt4
from PyQt4.QtGui import QMessageBox

from com.tourism.gui.ui_widget_register_travel_pack import Ui_widget_register_travel_pack 
from com.tourism.authentication.user_authentication import UserAuth

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
