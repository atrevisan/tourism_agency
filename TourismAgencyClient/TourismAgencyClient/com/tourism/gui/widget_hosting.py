# Author: Allan Caminha Trevisan <allan.trvsn@gmail.com>
# (c) 2015
#
# License: MIT

from PyQt4.QtGui import QWidget
from PyQt4 import QtGui, QtCore
import PyQt4
from PyQt4.QtGui import QMessageBox

from collections import OrderedDict

from com.tourism.gui.ui_widget_hosting import Ui_widget_hosting
from com.tourism.gui.widget_table import MyTable
from com.tourism.webservice.webservice_handler import WebserviceHandler

class WidgetHosting(QWidget, Ui_widget_hosting):
    """This widget is intended for hosting facilities display and revenue.
    
    The user can visualize the available hosting facilities and purchase one of them.

    Atributes
    -----------
    guest_ages : dict
        Map the hosting id to its associated guest ages
        for display in another table when the row of this
        hosting is selected.

    table_hosts : MyTable
        Table for displaying the avalilable hosts for purchase.
        Allows the user to selected one hosting for purchase.

    table_chosen_host : MyTable
        This table display the hosting chosen by the user.
        If the user wants he can remove it and choose
        another hosting.

    table_guests : MyTable
        This table displays the ages for the number of 
        guests that can be acomodated at the destination.
    """
    def __init__(self):

        QWidget.__init__(self)
        
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        handler = WebserviceHandler()
        hosts = handler.get_hosts()

        ids = []
        destinations = []
        input_dates = []
        output_dates = []
        number_of_rooms = []
        self.guest_ages = {}

        for host in hosts:

            ids.append(str(host.id))
            destinations.append(host.destination)
            input_dates.append("%d/%d/%d" % (host.inputDay, host.inputMonth, host.inputYear))
            output_dates.append("%d/%d/%d" % (host.outputDay, host.outputMonth, host.outputYear))
            number_of_rooms.append(str(host.numberOfRooms))
            self.guest_ages[str(host.id)] = host.guestAges

        data = OrderedDict([('id', ids), 
                            ('destination', destinations), 
                            ('input date', input_dates), 
                            ('output date', output_dates),
                            ('rooms', number_of_rooms)])

        self.table_hosts = MyTable(data, len(destinations), 5)
        self.vlayout_table_content.addWidget(self.table_hosts)

        data = OrderedDict([('id', []),
                            ('destination', []), 
                            ('input date', []), 
                            ('output date', []),
                            ('rooms', [])])
        self.table_chosen_host = MyTable(data, 0, 5)
        self.vlayout_chosen_hosting.addWidget(self.table_chosen_host)

        data = OrderedDict([('Guest age', [])])
        self.table_guests = MyTable(data, 0, 1)
        self.vlayout_guest_ages.addWidget(self.table_guests)

        # event handling
        self.button_choose_hosting.clicked.connect(self.choose_hosting)
        self.button_remove_hosting.clicked.connect(self.remove_hosting)
        self.table_hosts.clicked.connect(self.display_ages)
        self.button_buy.clicked.connect(self.buy)

    def choose_hosting(self):
        """Get the selected hosting and add it to another table.
        
        The table to wich the hosting is added contains the
        hosting that the user is intended to buy.
        """

        if self.table_chosen_host.rowCount() == 0:
            
            row_index = self.table_hosts.currentRow()
            row = self.table_hosts.get_row(row_index)

            self.table_chosen_host.insertRow(0)
            self.table_chosen_host.setItem(0 , 0, QtGui.QTableWidgetItem(row[0]))
            self.table_chosen_host.setItem(0 , 1, QtGui.QTableWidgetItem(row[1]))
            self.table_chosen_host.setItem(0 , 2, QtGui.QTableWidgetItem(row[2]))
            self.table_chosen_host.setItem(0 , 3, QtGui.QTableWidgetItem(row[3]))
            self.table_chosen_host.setItem(0 , 4, QtGui.QTableWidgetItem(row[4]))

       
    def remove_hosting(self):
        """Remove a chosen hosting so the user can choose another one."""

        row = self.table_chosen_host.get_row(0)

        new_row_index = self.table_hosts.rowCount()
        self.table_hosts.insertRow(new_row_index)
        
        self.table_hosts.setItem(new_row_index , 0, QtGui.QTableWidgetItem(row[0]))
        self.table_hosts.setItem(new_row_index , 1, QtGui.QTableWidgetItem(row[1]))
        self.table_hosts.setItem(new_row_index , 2, QtGui.QTableWidgetItem(row[2]))
        self.table_hosts.setItem(new_row_index , 3, QtGui.QTableWidgetItem(row[3]))
        self.table_hosts.setItem(new_row_index , 4, QtGui.QTableWidgetItem(row[4]))

    def display_ages(self):
        """Add the associated guest ages to the table when selected."""

        self.table_guests.setRowCount(0)
        self.table_guests.setColumnCount(1)

        selected_row_index = self.table_hosts.currentRow()

        column = self.guest_ages[self.table_hosts.item(selected_row_index, 0).text()]

        for row_index in range(len(column)):

            new_row_index = self.table_guests.rowCount()
            self.table_guests.insertRow(new_row_index)

            self.table_guests.setItem(new_row_index , 0, QtGui.QTableWidgetItem(str(column[row_index])))

    def buy(self):
        """Perform the hosting purchase operation."""

        credit_card_number = int (self.line_edit_credit_card.text())
        number_of_installments = int(self.combo_number_of_installments.currentText())

        chosen_hosting_id = int (self.table_chosen_host.get_row(0)[0])
        
        handler = WebserviceHandler()
        success = handler.buy_hosting(credit_card_number,
                                      number_of_installments,
                                      chosen_hosting_id)

        if success:

            QMessageBox.about(self, "Success", "hosting bought.")

        else:

            QMessageBox.about(self, "Failure", "Problem with the purchase.")
