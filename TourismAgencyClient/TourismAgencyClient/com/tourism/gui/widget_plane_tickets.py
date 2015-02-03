# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore
import PyQt4
from PyQt4.QtGui import QMessageBox

from collections import OrderedDict

from com.tourism.gui.ui_widget_plane_tickets import Ui_widget_plane_tickets
from com.tourism.gui.widget_table import MyTable
from com.tourism.webservice.webservice_handler import WebserviceHandler

class WidgetPlaneTickets(QWidget, Ui_widget_plane_tickets):
    """This widget is intended for plane tickets display and revenue.
    
    The user can visualize the available plane tickets and purchase one of them.

    Atributes
    -----------
    guest_ages : dict
        Map the pack id to its associated guest agest
        for display in another table when the row of this
        pack is selected.

    table_plane_tickets : MyTable
        Table for displaying the avalilable plane tickets for purchase.
        Allows the user to selected one plane ticket for purchase.

    table_chosen_plane_ticket : MyTable
        This table display the plane ticket chosen by the user.
        If the user wants he can remove it and choose
        another plane ticket.

    table_guests : MyTable
        This table displays the ages for the number of 
        guests that can be acomodated at the destination.
    """
    def __init__(self):

        QWidget.__init__(self)
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        handler = WebserviceHandler()
        plane_tickets = handler.get_plane_tickets()

        ids = []
        origins = []
        destinations = []
        departure_dates = []
        arrival_dates = []
        number_of_rooms = []
        departure_only = []
        self.guest_ages = {}

        for plane_ticket in plane_tickets:

            ids.append(str(plane_ticket.id))
            origins.append(plane_ticket.origin)
            destinations.append(plane_ticket.destination)
            departure_dates.append("%d/%d/%d" % (plane_ticket.departureDay, plane_ticket.departureMonth, plane_ticket.departureYear))
            arrival_dates.append("%d/%d/%d" % (plane_ticket.arrivalDay, plane_ticket.arrivalMonth, plane_ticket.arrivalYear))
            number_of_rooms.append(str(plane_ticket.numberOfRooms))
            departure_only.append("yes" if plane_ticket.onlyDeparture else "no")
            self.guest_ages[str(plane_ticket.id)] = plane_ticket.guestAges

        data = OrderedDict([('id', ids),
                            ('origin', origins), 
                            ('destination', destinations), 
                            ('departure date', departure_dates), 
                            ('arrival date', arrival_dates),
                            ('rooms', number_of_rooms),
                            ("departure only", departure_only)])

        self.table_plane_tickets = MyTable(data, len(origins), 7)
        self.vlayout_table_content.addWidget(self.table_plane_tickets)

        data = OrderedDict([('id', []),
                            ('origin', []), 
                            ('destination', []), 
                            ('departure date', []), 
                            ('arrival date', []),
                            ('rooms', []),
                            ("departure only", [])])
        self.table_chosen_plane_ticket = MyTable(data, 0, 7)
        self.vlayout_chosen_plane_ticket.addWidget(self.table_chosen_plane_ticket)

        data = OrderedDict([('Guest age', [])])
        self.table_guests = MyTable(data, 0, 1)
        self.vlayout_guest_ages.addWidget(self.table_guests)

        # event handling
        self.button_choose_plane_ticket.clicked.connect(self.choose_plane_ticket)
        self.button_remove_plane_ticket.clicked.connect(self.remove_plane_ticket)
        self.table_plane_tickets.clicked.connect(self.display_ages)
        self.button_buy.clicked.connect(self.buy)

    def choose_plane_ticket(self):
        """Get the selected plane ticket and add it to another table.
        
        The table to wich the plane ticket is added contains the
        plane ticket that the user is intended to buy.
        """

        if self.table_chosen_plane_ticket.rowCount() == 0:
            
            row_index = self.table_plane_tickets.currentRow()
            row = self.table_plane_tickets.get_row(row_index)

            self.table_chosen_plane_ticket.insertRow(0)
            self.table_chosen_plane_ticket.setItem(0 , 0, QtGui.QTableWidgetItem(row[0]))
            self.table_chosen_plane_ticket.setItem(0 , 1, QtGui.QTableWidgetItem(row[1]))
            self.table_chosen_plane_ticket.setItem(0 , 2, QtGui.QTableWidgetItem(row[2]))
            self.table_chosen_plane_ticket.setItem(0 , 3, QtGui.QTableWidgetItem(row[3]))
            self.table_chosen_plane_ticket.setItem(0 , 4, QtGui.QTableWidgetItem(row[4]))
            self.table_chosen_plane_ticket.setItem(0 , 5, QtGui.QTableWidgetItem(row[5]))
            self.table_chosen_plane_ticket.setItem(0 , 6, QtGui.QTableWidgetItem(row[6]))

       
    def remove_plane_ticket(self):
        """Remove a chosen plane ticket so the user can choose another one."""

        row = self.table_chosen_plane_ticket.get_row(0)

        new_row_index = self.table_plane_tickets.rowCount()
        self.table_plane_tickets.insertRow(new_row_index)
        
        self.table_plane_tickets.setItem(new_row_index , 0, QtGui.QTableWidgetItem(row[0]))
        self.table_plane_tickets.setItem(new_row_index , 1, QtGui.QTableWidgetItem(row[1]))
        self.table_plane_tickets.setItem(new_row_index , 2, QtGui.QTableWidgetItem(row[2]))
        self.table_plane_tickets.setItem(new_row_index , 3, QtGui.QTableWidgetItem(row[3]))
        self.table_plane_tickets.setItem(new_row_index , 4, QtGui.QTableWidgetItem(row[4]))
        self.table_plane_tickets.setItem(new_row_index , 5, QtGui.QTableWidgetItem(row[5]))
        self.table_plane_tickets.setItem(new_row_index , 6, QtGui.QTableWidgetItem(row[6]))



    def display_ages(self):
        """Add the associated guest ages to the table when selected."""

        self.table_guests.setRowCount(0)
        self.table_guests.setColumnCount(1)

        selected_row_index = self.table_plane_tickets.currentRow()

        column = self.guest_ages[self.table_plane_tickets.item(selected_row_index, 0).text()]

        for row_index in range(len(column)):

            new_row_index = self.table_guests.rowCount()
            self.table_guests.insertRow(new_row_index)

            self.table_guests.setItem(new_row_index , 0, QtGui.QTableWidgetItem(str(column[row_index])))

    def buy(self):
        """Perform the plane ticket purchase operation."""

        credit_card_number = int (self.line_edit_credit_card.text())
        number_of_installments = int(self.combo_number_of_installments.currentText())

        chosen_plane_ticket_id = int (self.table_chosen_plane_ticket.get_row(0)[0])
        
        handler = WebserviceHandler()
        success = handler.buy_plane_ticket(credit_card_number,
                                            number_of_installments,
                                            chosen_plane_ticket_id)

        if success:

            QMessageBox.about(self, "Success", "plane ticket bought.")

        else:

            QMessageBox.about(self, "Failure", "Problem with the purchase.")
